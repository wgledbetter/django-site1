#!/bin/bash

exec gunicorn site1.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3