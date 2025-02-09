#!/bin/bash

# Ждем, пока база данных не станет доступной
echo "Waiting for database..."
while ! pg_isready -U $POSTGRES_USER -d $POSTGRES_DB -h db -p 5432; do
  sleep 1
done
echo "Database is ready!"

# Применяем миграции
echo "Running migrations..."
python manage.py migrate --noinput

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Запускаем сервер Django, если не указана другая команда
if [ -z "$1" ]; then
  echo "Starting Django server..."
  python manage.py runserver 0.0.0.0:8000
else
  echo "Running command: $@"
  exec "$@"
fi
