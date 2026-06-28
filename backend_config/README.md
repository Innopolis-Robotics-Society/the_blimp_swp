# Airship MAVLink Backend

## Summary of changes

MAVLink backend для автономного дирижабля (Indoor Navigation Project, Innopolis Robotics Lab).

**Что реализовано:**
- MAVLink-мост между планировщиком маршрутов (RPi 5) и полётным контроллером (ArduPilot на MicoAir H743)
- REST API для управления дирижаблем (получение телеметрии, отправка setpoint'ов, загрузка миссий)
- WebSocket стриминг телеметрии в реальном времени (10 Hz)
- Поддержка двух режимов командования:
  - **AUTO/Mission**: загрузка миссии целиком (lat/lon с фейк-origin для indoor)
  - **Guided**: отправка отдельных целевых точек (локальный NED)
- Логирование всех событий в файл `airship_backend.log`

**Архитектура:**
- `mavlink_backend.py` — ядро MAVLink (подключение, телеметрия, команды)
- `api.py` — FastAPI сервер (REST + WebSocket)

## Testing performed

### Локальное тестирование (SITL)
- [x] Запуск сервера: `uvicorn api:app --reload --host 0.0.0.0 --port 8000`
- [x] Swagger UI доступен: `http://localhost:8000/docs`
- [x] GET `/telemetry` — возврат структуры данных (503 без подключения к FC)
- [x] POST `/setpoint` — отправка целевой точки (локальные координаты x,y,z)
- [x] POST `/mission` — загрузка миссии (список точек lat/lon/alt)
- [x] WebSocket `/ws/telemetry` — стриминг телеметрии 10 Hz
- [x] Логирование в `airship_backend.log`

### Интеграция с ArduPilot SITL
- [x] Подключение к симулятору: `udp:127.0.0.1:14550`
- [x] Приём телеметрии (GLOBAL_POSITION_INT, SYS_STATUS, HEARTBEAT)
- [x] Отправка SET_POSITION_TARGET_LOCAL_NED (Guided mode)
- [x] Загрузка миссии через MISSION_ITEM_INT (AUTO mode)

### Тесты на реальном железе (планируется)
- [ ] Подключение к MicoAir H743 V2 AIO (ELRS Backpack, UDP/MAVLink)
- [ ] Интеграция с UWB-дашбордом на RPi 5
- [ ] Полевые тесты в лаборатории 105а (UWB-локализация Nooploop)

## Reviewer checklist

- [x] Changes work as described
- [x] No sensitive data committed
- [x] Links are valid (if documentation changed)

