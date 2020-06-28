#!/bin/sh
FILE=/home/setup_done

wait_for_db() {
  while ! nc -z $DJANGO_DB_HOST:$DJANGO_DB_PORT; do
    echo "waiting for $DJANGO_DB_HOST"
    sleep 1
  done
}

setup_db() {
  wait_for_db
  python /code/chat_backend/manage.py migrate
  echo "setup_db done"
  touch $FILE
}

if [ ! -f $FILE ]; then
  setup_db
fi

python /code/chat_backend/manage.py runserver 0.0.0.0:8000
