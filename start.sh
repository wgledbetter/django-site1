#!/bin/bash

# exec ping -c 25 db

python manage.py makemigrations
python manage.py migrate

exec gunicorn site1.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3 \
    --reload