#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

DOCKER_CONFIG="${DOCKER_CONFIG:-$HOME/.docker}"

if grep -q "desktop" "$DOCKER_CONFIG/config.json" 2>/dev/null; then
    export DOCKER_CONFIG="/tmp/blimp-sim-docker-config"
    mkdir -p "$DOCKER_CONFIG"
    echo '{}' > "$DOCKER_CONFIG/config.json"
fi

docker compose -f "$SCRIPT_DIR/docker-compose.yml" up --build "$@"
