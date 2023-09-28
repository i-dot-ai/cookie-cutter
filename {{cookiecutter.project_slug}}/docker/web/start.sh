#!/bin/sh

set -o errexit
set -o nounset

python manage.py migrate --noinput

echo "Migrations completed"

echo "Starting app"

echo "Using '$ENVIRONMENT' environment settings"

if [ "$ENVIRONMENT" = "LOCAL" ]
then
    gunicorn --reload --workers 3 {{cookiecutter.package_name}}.wsgi:application
else
    gunicorn --workers 3 {{cookiecutter.package_name}}.wsgi:application
fi
