# Blimp Physics Simulator

Физический движок для дирижабля (blimp) как внешний симулятор для ArduPilot SITL.

Реализует протокол **SIM_JSON** — ArduPilot SITL отправляет PWM значения моторов по UDP, движок рассчитывает физику и возвращает JSON с показаниями датчиков.

## Физика

- Масса и инерция по осям вращения (Ix, Iy, Iz)
- Выталкивающая сила (гелий)
- Тяга 4 моторов (векторная)
- Аэродинамическое сопротивление по осям (Cd_x, Cd_y, Cd_z)
- Площади поперечного сечения по осям (Ax, Ay, Az)
- Гравитация
- Интегрирование: RK4, 250 Гц

## Структура

```
simulator/
├── blimp_sim.py         # Движок + UDP-сервер
├── blimp_config.yaml    # Параметры (масса, моторы, аэродинамика)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── PROTOCOL.md          # Протокол ввода/вывода
└── README.md
```

## Запуск

### Docker

```bash
cd simulator
docker compose up -d --build
```

### Без Docker

```bash
cd simulator
pip install -r requirements.txt
python3 blimp_sim.py --config blimp_config.yaml
```

## Подключение к ArduPilot SITL

1. Запустите симулятор (см. выше)
2. Запустите ArduPilot SITL:

```bash
sim_vehicle.py -v ArduBlimp --no-mavproxy --model JSON
```

3. Проверьте логи:

```bash
docker logs -f simulator-blimp-sim-1
```

## Конфигурация

Параметры в `blimp_config.yaml`:

| Секция    | Параметр               | По умолчанию      | Описание                        |
|-----------|------------------------|-------------------|---------------------------------|
| `blimp`   | `mass`                 | 0.5 кг            | Масса дирижабля                 |
| `blimp`   | `volume`               | 0.06 м³           | Объём оболочки                  |
| `blimp`   | `drag_coefficients`    | [0.4, 0.4, 0.3]  | Cd по осям [X, Y, Z]           |
| `blimp`   | `cross_section_areas`  | [0.05, 0.05, 0.08] | Площади м² по осям [X, Y, Z]  |
| `blimp`   | `inertia`              | [0.004, 0.004, 0.002] | Моменты инерции кг·м² [Ix, Iy, Iz] |
| `motors`  | `max_thrust`           | 0.15 Н            | Тяга одного мотора              |
| `physics` | `dt`                   | 0.004 с           | Шаг симуляции (250 Гц)          |
| `sim_json`| `listen_port`          | 9002              | UDP-порт                        |
