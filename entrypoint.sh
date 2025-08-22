#!/bin/sh

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Database is up!"

python notebook/manage.py migrate --noinput

echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').exists() or \
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" \
| python notebook/manage.py shell

exec "$@"