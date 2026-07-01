#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate

echo "Loading course fixture..."
python manage.py loaddata courses_data.json || true

echo "Starting Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:10000