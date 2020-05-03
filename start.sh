#!/bin/bash

# Django migrations
python manage.py makemigrations
python manage.py migrate

# Build the python stuff with whatever the local version is
cd astro/cpp
source ./build.sh
cd ../..

# Start gunicorn server
exec gunicorn site1.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3 \
    --reload