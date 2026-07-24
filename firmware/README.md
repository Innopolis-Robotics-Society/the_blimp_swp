# Firmware — ArduMotorBlimp для MicoAir H743 V2

Сборка кастомной прошивки ArduMotorBlimp на базе ArduPilot Copter-4.6.3.

## Предварительные требования

- SSH-доступ к Ubuntu VM (configured in `~/.ssh/config`) — для режима по умолчанию
- VM с правами sudo (для `setup.sh`)

## Быстрый старт

```bash
# 1. Создай свой config.env из шаблона
cp config.env.example config.env
# правь VM_HOST, WORKSPACE под себя

# 2. Настрой (один раз)
./setup.sh

# 3. Собери прошивку
./build.sh
```

## Флаги

### `-v` — verbose output

Заменяет компактный вывод на полный (аналог старых `-full` скриптов).

```bash
./setup.sh -v          # полный вывод при настройке
./build.sh -v          # полный вывод при сборке
```

### `-a` — auto-setup

Build автоматически запускает `setup.sh` если ArduPilot не найден.

```bash
./build.sh -a          # если нет ArduPilot — сначала ставит, потом собирает
./build.sh -a -v       # то же, но с полным выводом
```

### `-l` — local mode

Все команды выполняются локально вместо SSH на VM. Если комбинация `-a -l`, то setup тоже запускается с `-l`.

```bash
./setup.sh -l          # локальная настройка
./build.sh -l          # локальная сборка
./build.sh -a -l       # локальная сборка + auto-setup локально
```

## Файлы

| Файл | Описание |
|------|----------|
| `config.env.example` | Шаблон настроек (копируй в `config.env`) |
| `config.env` | Твои настройки (не коммитится) |
| `setup.sh` | Первичная настройка (`-v`, `-l`) |
| `build.sh` | Сборка прошивки (`-v`, `-a`, `-l`) |
| `flash.md` | Инструкция прошивки через MicoAir Configurator |
| `build/` | Собранные `.apj` файлы |

## Настройки (config.env)

| Параметр | Описание | Дефолт |
|----------|----------|--------|
| `VM_HOST` | SSH-хост или alias | `my_vm` |
| `VM_USER` | SSH-пользователь | `daniyar` |
| `WORKSPACE` | Путь к рабочей директории | `~/blimp_workspace` |
| `VEHICLE_BRANCH` | Ветка ArduMotorBlimp | `feat/manual-only` |
| `BOARD` | Платформа сборки | `MicoAir743v2` |

## Что делает setup.sh

1. Проверяет SSH-доступ к VM (или работает локально с `-l`)
2. Проверяет/устанавливает системные зависимости (gcc-arm-none-eabi, python3, cmake)
3. Проверяет ArduPilot — если нет Copter-4.6.3, клонирует
4. Проверяет Python venv — если нет, создаёт с нужными зависимостями
5. Клонирует/обновляет ArduMotorBlimp
6. Патчит build-систему ArduPilot (vehicles list + APM_BUILD макрос)
7. Копирует ArduMotorBlimp в дерево ArduPilot

Все шаги идемпотентны — повторный запуск не ломает существующую настройку.
