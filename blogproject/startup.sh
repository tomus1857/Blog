#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn blogproject.wsgi --bind=0.0.0.0 --timeout 600
