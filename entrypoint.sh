#!/bin/sh
set -e

echo "Running Django migrations..."
python manage.py migrate

echo "Starting Django with Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:10000