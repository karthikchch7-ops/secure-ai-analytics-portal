#!/bin/bash
# Quickstart script (Linux/macOS) to build and run the project using Docker Compose
set -e

echo "Building and starting services..."
docker-compose up --build -d

echo "Seeding admin user (wait a few seconds for DB and backend)..."
sleep 8
# Run seed script inside backend container
BACKEND_CONTAINER=$(docker ps --filter "ancestor=secure-ai-analytics-portal_backend" --format "{{.ID}}" | head -n1)
if [ -n "$BACKEND_CONTAINER" ]; then
  docker exec -it $BACKEND_CONTAINER python seed_admin.py || true
else
  echo "Could not find backend container to seed admin. Seed manually using seed_admin.py"
fi

echo "All services started. Backend: http://localhost:8000  Dashboard: http://localhost:8501"
