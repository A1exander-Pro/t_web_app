#! /bin/bash
chmod +x entrypoint.sh

python manage.py makemigrations

until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done

rm -f './celerybeat.pid'


./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic

echo "Django is ready.";
gunicorn Telegram_App.wsgi:application --bind 0.0.0.0:8000

