#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cleanup() {
    docker-compose -f "$SCRIPT_DIR/sitl/docker-compose.yml" down 2>/dev/null || true
    docker-compose -f "$SCRIPT_DIR/QGC/docker-compose.yml" down 2>/dev/null || true
}
trap cleanup EXIT

xhost +local:docker 2>/dev/null || true

docker-compose -f "$SCRIPT_DIR/sitl/docker-compose.yml" up -d sitl-auto
docker-compose -f "$SCRIPT_DIR/QGC/docker-compose.yml" up -d qgc

echo "[+] Done. Ctrl+C to stop."
sleep infinity
