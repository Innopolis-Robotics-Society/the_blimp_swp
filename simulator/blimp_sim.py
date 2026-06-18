#!/usr/bin/env python3
"""
ArduPilot SITL external physics engine for indoor blimp/dirigible.

Receives motor PWM values from ArduPilot via SIM_JSON UDP protocol,
simulates blimp dynamics (buoyancy, thrust, drag), and returns
sensor data as JSON.
"""

import argparse
import socket
import struct
import yaml
import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class BlimpConfig:
    mass: float = 0.5
    volume: float = 0.06
    drag_coefficients: List[float] = field(default_factory=lambda: [0.4, 0.4, 0.3])
    cross_section_areas: List[float] = field(default_factory=lambda: [0.05, 0.05, 0.08])
    inertia: List[float] = field(default_factory=lambda: [0.004, 0.004, 0.002])
    motor_count: int = 4
    max_thrust: float = 0.15
    motor_positions: List[List[float]] = field(default_factory=lambda: [
        [0.1, 0.0, 0.0],
        [-0.1, 0.0, 0.0],
        [0.0, 0.0, 0.1],
        [0.0, 0.1, 0.0],
    ])
    motor_directions: List[List[float]] = field(default_factory=lambda: [
        [1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0],
        [0.0, 0.0, -1.0],
        [0.0, 1.0, 0.0],
    ])
    air_density: float = 1.225
    gravity: float = 9.81
    dt: float = 0.004
    listen_port: int = 9002
    listen_address: str = "127.0.0.1"
    home_lat: float = 47.9945
    home_lon: float = 55.9638
    home_alt: float = 0.0


@dataclass
class BlimpState:
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))
    orientation: np.ndarray = field(default_factory=lambda: np.array([1.0, 0.0, 0.0, 0.0]))
    angular_velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))
    timestamp: float = 0.0


class BlimpPhysics:
    def __init__(self, config: BlimpConfig):
        self.config = config
        self.state = BlimpState()
        self.motor_positions = np.array(config.motor_positions)
        self.motor_directions = np.array(config.motor_directions)
        self.Cd = np.array(config.drag_coefficients)
        self.A = np.array(config.cross_section_areas)
        self.inertia = np.diag(config.inertia)
        self.inertia_inv = np.linalg.inv(self.inertia)

    def _net_buoyancy_force(self) -> np.ndarray:
        rho_air = self.config.air_density
        V = self.config.volume
        g = self.config.gravity
        rho_helium = 0.1786
        m = self.config.mass
        F_buoy = rho_air * V * g
        F_grav = m * g
        net = F_buoy - F_grav
        return np.array([0.0, 0.0, -net])

    def _thrust_forces(self, motors: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        F_total = np.zeros(3)
        tau_total = np.zeros(3)
        for i in range(self.config.motor_count):
            if i >= len(motors):
                break
            T = self.config.max_thrust * motors[i]
            d = self.motor_directions[i]
            r = self.motor_positions[i]
            F_i = T * d
            F_total += F_i
            tau_total += np.cross(r, F_i)
        return F_total, tau_total

    def _drag_force(self, velocity: np.ndarray) -> np.ndarray:
        rho = self.config.air_density
        v_abs = np.abs(velocity)
        F = -0.5 * rho * self.Cd * self.A * v_abs * velocity
        return F

    def _quaternion_multiply(self, q: np.ndarray, r: np.ndarray) -> np.ndarray:
        w1, x1, y1, z1 = q
        w2, x2, y2, z2 = r
        return np.array([
            w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2,
        ])

    def _quaternion_derivative(self, q: np.ndarray, omega: np.ndarray) -> np.ndarray:
        q_omega = np.array([0.0, omega[0], omega[1], omega[2]])
        return 0.5 * self._quaternion_multiply(q, q_omega)

    def _quaternion_normalize(self, q: np.ndarray) -> np.ndarray:
        n = np.linalg.norm(q)
        if n < 1e-12:
            return np.array([1.0, 0.0, 0.0, 0.0])
        return q / n

    def _body_to_earth_rotation(self, q: np.ndarray) -> np.ndarray:
        w, x, y, z = q
        R = np.array([
            [1 - 2*(y*y + z*z), 2*(x*y - w*z), 2*(x*z + w*y)],
            [2*(x*y + w*z), 1 - 2*(x*x + z*z), 2*(y*z - w*x)],
            [2*(x*z - w*y), 2*(y*z + w*x), 1 - 2*(x*x + y*y)],
        ])
        return R

    def _body_to_earth_velocity(self, v_body: np.ndarray, q: np.ndarray) -> np.ndarray:
        R = self._body_to_earth_rotation(q)
        return R @ v_body

    def _derivs(self, pos, vel, quat, angvel, t, motors_arr):
        F_buoy = self._net_buoyancy_force()
        F_thrust, tau_thrust = self._thrust_forces(motors_arr)
        F_drag = self._drag_force(vel)
        F_total = F_buoy + F_thrust + F_drag
        a = F_total / self.config.mass
        alpha = self.inertia_inv @ tau_thrust
        q_dot = self._quaternion_derivative(quat, angvel)
        return vel, a, q_dot, alpha

    def step_rk4(self, motors: np.ndarray, dt: float) -> BlimpState:
        s = self.state
        orig_pos = s.position.copy()
        orig_vel = s.velocity.copy()
        orig_quat = s.orientation.copy()
        orig_angvel = s.angular_velocity.copy()
        orig_t = s.timestamp

        k1_v, k1_a, k1_qd, k1_ad = self._derivs(
            orig_pos, orig_vel, orig_quat, orig_angvel, orig_t, motors)

        p2 = orig_pos + 0.5*dt*k1_v
        v2 = orig_vel + 0.5*dt*k1_a
        q2 = self._quaternion_normalize(orig_quat + 0.5*dt*k1_qd)
        w2 = orig_angvel + 0.5*dt*k1_ad
        k2_v, k2_a, k2_qd, k2_ad = self._derivs(
            p2, v2, q2, w2, orig_t+0.5*dt, motors)

        p3 = orig_pos + 0.5*dt*k2_v
        v3 = orig_vel + 0.5*dt*k2_a
        q3 = self._quaternion_normalize(orig_quat + 0.5*dt*k2_qd)
        w3 = orig_angvel + 0.5*dt*k2_ad
        k3_v, k3_a, k3_qd, k3_ad = self._derivs(
            p3, v3, q3, w3, orig_t+0.5*dt, motors)

        p4 = orig_pos + dt*k3_v
        v4 = orig_vel + dt*k3_a
        q4 = self._quaternion_normalize(orig_quat + dt*k3_qd)
        w4 = orig_angvel + dt*k3_ad
        k4_v, k4_a, k4_qd, k4_ad = self._derivs(
            p4, v4, q4, w4, orig_t+dt, motors)

        self.state = BlimpState(
            position=orig_pos + (dt/6.0)*(k1_v + 2*k2_v + 2*k3_v + k4_v),
            velocity=orig_vel + (dt/6.0)*(k1_a + 2*k2_a + 2*k3_a + k4_a),
            orientation=self._quaternion_normalize(
                orig_quat + (dt/6.0)*(k1_qd + 2*k2_qd + 2*k3_qd + k4_qd)
            ),
            angular_velocity=orig_angvel + (dt/6.0)*(k1_ad + 2*k2_ad + 2*k3_ad + k4_ad),
            timestamp=orig_t + dt,
        )
        return self.state


class SIMJsonServer:
    MAGIC_16 = 18458
    MAGIC_32 = 29569
    SERVO_PACKET_FMT_16 = "<HHI16H"
    SERVO_PACKET_FMT_32 = "<HHI32H"

    def __init__(self, config: BlimpConfig, physics: BlimpPhysics):
        self.config = config
        self.physics = physics
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(0.01)
        self.sock.bind((config.listen_address, config.listen_port))
        self.frame_count = 0
        self.frame_rate = int(1.0 / config.dt)

    def recv_servo_packet(self) -> Tuple[List[int], int]:
        try:
            data, addr = self.sock.recvfrom(1024)
        except socket.timeout:
            return [], 0

        if len(data) < 4:
            return [], 0

        magic = struct.unpack("<H", data[:2])[0]

        if magic == self.MAGIC_16:
            if len(data) < struct.calcsize(self.SERVO_PACKET_FMT_16):
                return [], 0
            _, frame_rate, frame_count, *pwm = struct.unpack(
                self.SERVO_PACKET_FMT_16, data[:struct.calcsize(self.SERVO_PACKET_FMT_16)]
            )
            return list(pwm), frame_rate
        elif magic == self.MAGIC_32:
            if len(data) < struct.calcsize(self.SERVO_PACKET_FMT_32):
                return [], 0
            _, frame_rate, frame_count, *pwm = struct.unpack(
                self.SERVO_PACKET_FMT_32, data[:struct.calcsize(self.SERVO_PACKET_FMT_32)]
            )
            return list(pwm[:16]), frame_rate
        else:
            return [], 0

    def pwm_to_motors(self, pwm_list: List[int]) -> np.ndarray:
        motors = np.zeros(self.config.motor_count)
        for i in range(min(len(pwm_list), self.config.motor_count)):
            motors[i] = max(0.0, min(1.0, (pwm_list[i] - 1000) / 1000.0))
        return motors

    def build_json_response(self, state: BlimpState) -> str:
        q = state.orientation
        w, x, y, z = q

        v_earth = self.physics._body_to_earth_velocity(state.velocity, state.orientation)

        pos = state.position

        g_earth = np.array([0.0, 0.0, self.config.gravity])
        R = self.physics._body_to_earth_rotation(q)
        accel_body = R.T @ g_earth

        json_str = (
            '{"timestamp":%.6f,'
            '"imu":{"gyro":[%.6f,%.6f,%.6f],"accel_body":[%.6f,%.6f,%.6f]},'
            '"velocity":[%.6f,%.6f,%.6f],'
            '"quaternion":[%.8f,%.8f,%.8f,%.8f],'
            '"position":[%.4f,%.4f,%.4f],'
            '"latitude":%.8f,"longitude":%.8f,"altitude":%.4f,'
            '"no_time_sync":true,"no_lockstep":true}\n'
        ) % (
            state.timestamp,
            state.angular_velocity[0], state.angular_velocity[1], state.angular_velocity[2],
            accel_body[0], accel_body[1], accel_body[2],
            v_earth[0], v_earth[1], v_earth[2],
            w, x, y, z,
            pos[0], pos[1], pos[2],
            self.config.home_lat,
            self.config.home_lon,
            self.config.home_alt + (-pos[2]),
        )
        return json_str

    def send_json(self, json_str: str):
        self.sock.sendto(json_str.encode(), (self.config.listen_address, self.config.listen_port))

    def close(self):
        self.sock.close()


def load_config(path: str) -> BlimpConfig:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)

    cfg = BlimpConfig()
    b = raw.get("blimp", {})
    cfg.mass = b.get("mass", cfg.mass)
    cfg.volume = b.get("volume", cfg.volume)
    cfg.drag_coefficients = b.get("drag_coefficients", cfg.drag_coefficients)
    cfg.cross_section_areas = b.get("cross_section_areas", cfg.cross_section_areas)
    cfg.inertia = b.get("inertia", cfg.inertia)

    m = raw.get("motors", {})
    cfg.motor_count = m.get("count", cfg.motor_count)
    cfg.max_thrust = m.get("max_thrust", cfg.max_thrust)
    cfg.motor_positions = m.get("positions", cfg.motor_positions)
    cfg.motor_directions = m.get("directions", cfg.motor_directions)

    p = raw.get("physics", {})
    cfg.air_density = p.get("air_density", cfg.air_density)
    cfg.gravity = p.get("gravity", cfg.gravity)
    cfg.dt = p.get("dt", cfg.dt)

    s = raw.get("sim_json", {})
    cfg.listen_port = s.get("listen_port", cfg.listen_port)
    cfg.listen_address = s.get("listen_address", cfg.listen_address)

    h = raw.get("home", {})
    cfg.home_lat = h.get("lat", cfg.home_lat)
    cfg.home_lon = h.get("lon", cfg.home_lon)
    cfg.home_alt = h.get("alt", cfg.home_alt)

    return cfg


def main():
    parser = argparse.ArgumentParser(description="Blimp physics engine for ArduPilot SITL (SIM_JSON)")
    parser.add_argument("--config", default="blimp_config.yaml", help="Path to config YAML")
    args = parser.parse_args()

    config = load_config(args.config)
    physics = BlimpPhysics(config)
    server = SIMJsonServer(config, physics)

    print(f"Blimp physics engine started on {config.listen_address}:{config.listen_port}")
    print(f"  Mass: {config.mass} kg, Volume: {config.volume} m^3")
    print(f"  Drag Cd: {config.drag_coefficients}, Area: {config.cross_section_areas}")
    print(f"  Inertia: {config.inertia}")
    print(f"  Motors: {config.motor_count}, Max thrust: {config.max_thrust} N")
    print(f"  Physics step: {config.dt} s ({int(1/config.dt)} Hz)")
    print("Waiting for ArduPilot SITL SIM_JSON connection...")

    try:
        while True:
            pwm_list, frame_rate = server.recv_servo_packet()
            if not pwm_list:
                continue

            motors = server.pwm_to_motors(pwm_list)
            state = physics.step_rk4(motors, config.dt)
            json_str = server.build_json_response(state)
            server.send_json(json_str)

            server.frame_count += 1
            if server.frame_count % 250 == 0:
                pos = state.position
                print(f"  frame={server.frame_count} pos=[{pos[0]:.2f},{pos[1]:.2f},{pos[2]:.2f}] "
                      f"motors=[{motors[0]:.2f},{motors[1]:.2f},{motors[2]:.2f},{motors[3]:.2f}]")

    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        server.close()


if __name__ == "__main__":
    main()
