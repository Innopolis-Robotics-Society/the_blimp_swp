# Firmware — ArduMotorBlimp для MicoAir H743 V2

Сборка кастомной прошивки ArduMotorBlimp на базе ArduPilot Copter-4.6.3.

## Предварительные требования

- SSH-доступ к Ubuntu VM (configured in `~/.ssh/config`)
- VM с правами sudo (для `setup.sh`)

## Быстрый старт

```bash
# 1. Создай свой config.env из шаблона
cp config.env.example config.env
# правь VM_HOST, WORKSPACE под себя

# 2. Настрой VM (один раз)
./setup.sh

# 3. Собери прошивку
./build-full.sh                  # полный вывод
# или
./build.sh                       # компактный вывод

# 4. Прошей (см. flash.md)
```

## Файлы

| Файл | Описание |
|------|----------|
| `config.env.example` | Шаблон настроек (копируй в `config.env`) |
| `config.env` | Твои настройки (не коммитится) |
| `setup.sh` | Первичная настройка VM (зависимости, ArduPilot, venv, vehicle) |
| `build.sh` | Сборка прошивки (компактный вывод) |
| `build-full.sh` | Сборка прошивки (полный вывод) |
| `flash.md` | Инструкция прошивки через MicoAir Configurator |
| `build/` | Собранные `.apj` файлы |

## Настройки (config.env)

| Параметр | Описание | Дефолт |
|----------|----------|--------|
| `VM_HOST` | SSH-хост или alias | `my_vm` |
| `VM_USER` | SSH-пользователь | `daniyar` |
| `WORKSPACE` | Путь к рабочей директории на VM | `~/blimp_workspace` |
| `VEHICLE_BRANCH` | Ветка ArduMotorBlimp | `feat/manual-only` |
| `BOARD` | Платформа сборки | `MicoAir743v2` |

## Что делает setup.sh

1. Проверяет SSH-доступ к VM
2. Проверяет/устанавливает системные зависимости (gcc-arm-none-eabi, python3, cmake)
3. Проверяет ArduPilot — если нет Copter-4.6.3, клонирует
4. Проверяет Python venv — если нет, создаёт с нужными зависимостями
5. Клонирует/обновляет ArduMotorBlimp
6. Патчит build-систему ArduPilot (vehicles list + APM_BUILD макрос)
7. Копирует ArduMotorBlimp в дерево ArduPilot

Все шаги идемпотентны — повторный запуск не ломает существующую настройку.
