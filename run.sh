#!/bin/bash

echo "Iniciando o Kanban Board em Docker..."
cd "$(dirname "$0")"
docker compose up --build