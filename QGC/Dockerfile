# QGroundControl — контейнер для запуска GCS
# Используем AppImage (рекомендованный способ для контейнеров).
# Сборка из исходников в Docker нестабильна из-за Qt6/GStreamer зависимостей.

FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG QGC_VERSION=v4.4.3

ENV TZ=Etc/UTC
ENV QGC_APPIMAGE=/opt/qgroundcontrol/QGroundControl.AppImage

# Runtime-зависимости QGC (AppImage всё несёт внутри, но нужны системные либы)
RUN apt-get update && apt-get install -y --no-install-recommends \
    # FUSE для AppImage
    libfuse2 \
    # X11 / GUI
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxcb-xkb1 \
    libxcomposite1 \
    libxinerama1 \
    libxrandr2 \
    libxi6 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libfontconfig1 \
    libdbus-1-3 \
    # Сеть / MAVLink
    net-tools \
    iputils-ping \
    # SDL2 (нужен QGC для Joystick)
    libsdl2-2.0-0 \
    # GStreamer (нужен для видеопотока)
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libgstreamer-gl1.0-0 \
    # PulseAudio (для звука/аудио)
    libpulse0 \
    libpulse-mainloop-glib0 \
    # Утилиты
    wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем QGC AppImage
RUN mkdir -p /opt/qgroundcontrol && \
    wget -q "https://github.com/mavlink/qgroundcontrol/releases/download/${QGC_VERSION}/QGroundControl.AppImage" \
         -O ${QGC_APPIMAGE} && \
    chmod +x ${QGC_APPIMAGE}

# Пользователь (не root — AppImage так требует)
RUN groupadd --gid 1000 qgc \
    && useradd --uid 1000 --gid 1000 -m -s /bin/bash qgc \
    && mkdir -p /home/qgc/.config/QGroundControl.org \
    && chown -R qgc:qgc /home/qgc /opt/qgroundcontrol

USER qgc
WORKDIR /home/qgc

# XDG_RUNTIME_DIR для D-Bus
ENV XDG_RUNTIME_DIR=/tmp/runtime-qgc
RUN mkdir -p ${XDG_RUNTIME_DIR} && chmod 700 ${XDG_RUNTIME_DIR}

CMD ["bash", "-c", "/opt/qgroundcontrol/QGroundControl.AppImage --appimage-extract-and-run"]
