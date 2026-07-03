# QGroundControl — Docker

Docker-контейнер для запуска QGroundControl (GCS) в среде блимпа.

## Содержимое

- `Dockerfile` — образ на базе Ubuntu 22.04 с QGC v4.4.3 (AppImage) и всеми runtime-зависимостями
- `docker-compose.yml` — сервис с X11, PulseAudio, host-сетью и persistent-конфигом

## Зависимости

Все X11/GStreamer/SDL/PulseAudio библиотеки устанавливаются автоматически при сборке. `ldd` проверка показывает 0 неразрешённых библиотек.

## Запуск

```bash
# Разрешить Docker к X-серверу (один раз за сессию)
xhost +local:docker

# Собрать и запустить
docker compose up -d qgc

# Войти в контейнер
docker compose exec qgc bash
```

## Подключение к SITL

SITL запускается отдельно (см. `../sitl/`). QGC подключается через host-сеть:

- **UDP** `127.0.0.1:14550`
- **TCP** `127.0.0.1:5760`

## USB (реальный дрон)

Для подключения дрона по USB раскомментировать в `docker-compose.yml`:

```yaml
volumes:
  - /dev/bus/usb:/dev/bus/usb
```

## Конфигурация

Конфиг QGC сохраняется в Docker volume `qgc-config` между перезапусками.
