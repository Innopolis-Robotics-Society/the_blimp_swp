FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Install base packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo git wget curl \
    python3 python3-pip python3-dev \
    build-essential g++ gcc \
    rsync \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# Create user
RUN groupadd --gid 1000 blimp \
    && useradd --uid 1000 --gid 1000 -m blimp \
    && echo "blimp ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/blimp \
    && chmod 0440 /etc/sudoers.d/blimp

USER blimp
WORKDIR /home/blimp

# Clone ArduPilot
RUN git clone --depth 1 --branch Copter-4.6.3 https://github.com/ArduPilot/ardupilot.git

# Clone Blimp files
RUN git clone --depth 1 https://github.com/DaniK-51/ArduMotorBlimp.git /tmp/blimp

# Copy Blimp files (only new files, don't overwrite)
RUN cp -rn /tmp/blimp/* /home/blimp/ardupilot/ArduCopter/

WORKDIR /home/blimp/ardupilot

# Initialize submodules
RUN git submodule update --init --recursive --depth 1

# Install Python packages
RUN pip3 install --no-cache-dir \
    empy==3.3.4 \
    pexpect \
    future \
    lxml \
    pymavlink \
    MAVProxy

# Setup PATH
RUN echo 'export PATH=$PATH:/home/blimp/ardupilot/Tools/autotest' >> /home/blimp/.bashrc

# Configure and build
RUN ./waf configure --board sitl

RUN ./waf blimp

WORKDIR /home/blimp

CMD ["bash"]