# Quickstart for Windows (PowerShell)
Write-Host "Building and starting services..."
docker-compose up --build -d
Start-Sleep -s 8
Write-Host "To seed admin run inside backend container: docker exec -it <backend_container> python seed_admin.py"
Write-Host "Backend: http://localhost:8000  Dashboard: http://localhost:8501"
