
set -e

echo "Esperando a que la base de datos esté lista..."
sleep 5


python manage.py makemigrations || true
python manage.py migrate --noinput


python manage.py collectstatic --noinput || true


exec python manage.py runserver 0.0.0.0:8000
