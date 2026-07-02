# SITL для ArduMotorBlimp
# Источники:
#   - ArduPilot (базовый фреймворк): https://github.com/ArduPilot/ardupilot
#   - ArduMotorBlimp (vehicle-код):  https://github.com/DaniK-51/ArduMotorBlimp

FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Зависимости для сборки
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo git python3 python3-pip python3-dev build-essential \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# Пользователь (запуск от root небезопасен для ArduPilot)
RUN groupadd --gid 1000 blimp \
    && useradd --uid 1000 --gid 1000 -m blimp \
    && echo "blimp ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/blimp \
    && chmod 0440 /etc/sudoers.d/blimp

USER blimp
WORKDIR /home/blimp

# Клонируем ArduPilot и кастомный vehicle
RUN git clone --depth 1 --branch Copter-4.6.3 https://github.com/ArduPilot/ardupilot.git \
    && git clone --depth 1 https://github.com/DaniK-51/ArduMotorBlimp.git /tmp/blimp \
    && cp -rn /tmp/blimp/* /home/blimp/ardupilot/ArduCopter/ \
    && rm -rf /tmp/blimp

WORKDIR /home/blimp/ardupilot

# Подмодули + Python-зависимости
RUN git submodule update --init --recursive --depth 1 \
    && pip3 install --no-cache-dir empy==3.3.4 pexpect future lxml pymavlink MAVProxy

# PATH для sim_vehicle.py
RUN echo 'export PATH=$PATH:/home/blimp/ardupilot/Tools/autotest' >> /home/blimp/.bashrc

# Сборка ArduBlimp
RUN ./waf configure --board sitl && ./waf blimp

WORKDIR /home/blimp

CMD ["bash"]
