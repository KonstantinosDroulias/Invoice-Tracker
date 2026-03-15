#!/bin/bash
set -e

echo "Waiting for database..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.5
done
echo "Database is up."

echo "Running migrations..."
python manage.py migrate --noinput

echo "Building Tailwind and collecting static..."
bash build.sh

echo "Creating superuser..."
python scripts/create_superuser.py

echo "Starting server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
