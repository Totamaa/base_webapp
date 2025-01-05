#!/bin/sh
set -e
set -x

if [ "$ENVIRONMENT" = "dev" ]; then
    fastapi dev --port "$API_PORT" --host 0.0.0.0 main.py
else
    fastapi run --port "$API_PORT" --workers "$API_WORKERS" main.py
fi