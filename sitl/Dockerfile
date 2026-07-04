FROM ubuntu:22.04

# ---------------------------------------------------------------------------
# Blimp SITL image
#   - ArduPilot SITL is COMPILED INTO the image at a pinned stable tag.
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

# --- base tooling -----------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo git wget curl ca-certificates gnupg lsb-release \
    nano tree iputils-ping net-tools iproute2 \
    python3 python3-pip python3-dev \
    build-essential \
 && ln -s /usr/bin/python3 /usr/bin/python \
 && rm -rf /var/lib/apt/lists/*
# --- create user (matches host UID so mounted files stay writable) ----------
RUN groupadd --gid $USER_GID $USERNAME \
 && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
 && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME

# --- clone ArduPilot at the pinned tag --------------------------------------
# Shallow clone of just the tag, then init submodules. This is the heavy step.
USER $USERNAME
WORKDIR /home/$USERNAME

RUN git clone --depth 1 --branch ${ARDUPILOT_TAG} \
        https://github.com/ArduPilot/ardupilot.git \
 && cd ardupilot \
 && git submodule update --init --recursive --depth 1

# --- install ArduPilot prerequisites ----------------------------------------
# The official script installs MAVProxy, pymavlink, the arm toolchain bits,
# empy, future, etc. -y answers yes; we skip the editor/gcc-arm prompts.
WORKDIR /home/$USERNAME/ardupilot
RUN bash Tools/environment_install/install-prereqs-ubuntu.sh -y || true
# Install ALL required Python packages at once
RUN pip3 install --default-timeout=1000 \
    mavproxy \
    pymavlink \
    empy==3.3.4 \
    pexpect \
    future \
    lxml
# Make sim_vehicle.py / mavproxy available on PATH for every shell.
RUN echo 'export PATH=$PATH:/home/'"$USERNAME"'/ardupilot/Tools/autotest' >> /home/$USERNAME/.bashrc \
 && echo 'export PATH=$PATH:/home/'"$USERNAME"'/.local/bin' >> /home/$USERNAME/.bashrc
ENV PATH="/home/${USERNAME}/ardupilot/Tools/autotest:/home/${USERNAME}/.local/bin:${PATH}"

# --- pre-build the SITL Copter binary ---------------------------------------
# Building here means container start is fast (no compile on first run).
# waf configure for SITL, then build copter.
RUN . /home/$USERNAME/.profile 2>/dev/null; \
    ./waf configure --board sitl \
 && ./waf copter

# Sanity: confirm the binary exists where sim_vehicle expects it.
RUN test -f /home/$USERNAME/ardupilot/build/sitl/bin/arducopter

WORKDIR /home/$USERNAME
CMD ["bash"]

