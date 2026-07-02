FROM ubuntu:22.04

# ---------------------------------------------------------------------------
# Blimp SITL image
#   - ArduPilot SITL + custom ArduMotorBlimp vehicle COMPILED into the image.
#   - Your repo (params + Lua scripts) is NOT baked in — it is mounted at
#     runtime via docker-compose volume, so edits on the host are picked up
#     immediately without rebuilding.
# ---------------------------------------------------------------------------

ARG USERNAME=blimp
ARG USER_UID=1000
ARG USER_GID=1000
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Pin to a stable Copter release tag. Do NOT use master — it breaks.
# Bump this deliberately, not by accident.
ARG ARDUPILOT_TAG=Copter-4.6.3

# Custom vehicle repo (ArduMotorBlimp)
ARG VEHICLE_REPO=DaniK-51/ArduMotorBlimp
ARG VEHICLE_BRANCH=fix/adapting-repo-for-build

# --- base tooling -----------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo git wget curl ca-certificates gnupg lsb-release \
    nano tree iputils-ping net-tools \
    python3 python3-pip python3-dev \
    build-essential \
 && ln -s /usr/bin/python3 /usr/bin/python \
 && rm -rf /var/lib/apt/lists/*
# --- create user (matches host UID so mounted files stay writable) ----------
RUN groupadd --gid $USER_GID $USERNAME \
 && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
 && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME

# --- copy patch script (before USER switch so it's owned by root) -----------
COPY scripts/patch-ardupilot.sh /tmp/patch-ardupilot.sh
RUN chmod +x /tmp/patch-ardupilot.sh

# --- clone ArduPilot at the pinned tag --------------------------------------
USER $USERNAME
WORKDIR /home/$USERNAME

RUN git clone --depth 1 --branch ${ARDUPILOT_TAG} \
        https://github.com/ArduPilot/ardupilot.git \
 && cd ardupilot \
 && git submodule update --init --recursive --depth 1

# --- install ArduPilot prerequisites ----------------------------------------
WORKDIR /home/$USERNAME/ardupilot
RUN bash Tools/environment_install/install-prereqs-ubuntu.sh -y || true
RUN pip3 install --default-timeout=1000 \
    empy==3.3.4 \
    pexpect \
    future \
    lxml
RUN echo 'export PATH=$PATH:/home/'"$USERNAME"'/ardupilot/Tools/autotest' >> /home/$USERNAME/.bashrc \
 && echo 'export PATH=$PATH:/home/'"$USERNAME"'/.local/bin' >> /home/$USERNAME/.bashrc

# --- clone custom vehicle (ArduMotorBlimp) into ArduPilot --------------------
RUN git clone --depth 1 --branch ${VEHICLE_BRANCH} \
        https://github.com/${VEHICLE_REPO}.git \
        /home/$USERNAME/ardupilot/ArduMotorBlimp

# Register ArduMotorBlimp in ArduPilot build system and sim_vehicle.py
RUN sudo /tmp/patch-ardupilot.sh /home/$USERNAME/ardupilot \
 && grep "vehicles = " /home/$USERNAME/ardupilot/wscript \
 && sudo rm /tmp/patch-ardupilot.sh

# --- pre-build the SITL ArduMotorBlimp binary -------------------------------
RUN . /home/$USERNAME/.profile 2>/dev/null; \
    ./waf configure --board sitl \
 && ./waf build --target bin/ardublimp

# Sanity: confirm the binary exists where sim_vehicle expects it.
RUN test -f /home/$USERNAME/ardupilot/build/sitl/bin/ardublimp

WORKDIR /home/$USERNAME
CMD ["bash"]
