#!/usr/bin/env sh
# entrypoint.sh - compatible con Windows + Docker

set -e

echo "Esperando a que la base de datos esté lista..."
sleep 5

# Migraciones
python manage.py makemigrations || true
python manage.py migrate --noinput

# Collect static (opcional)
python manage.py collectstatic --noinput || true

# Levantar servidor Django
exec python manage.py runserver 0.0.0.0:8000
