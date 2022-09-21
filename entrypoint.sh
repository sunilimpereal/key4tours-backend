#!/bin/sh
python manage.py migrate
python manage.py collectstatic --no-input

gunicorn key4tours_backend.wsgi:application --bind 0.0.0:8000
