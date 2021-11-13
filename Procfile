web: gunicorn yetiMP3.wsgi --timeout 15 --log-file -
worker: celery -A yetiMP3 worker -B --loglevel=info
release: python manage.py migrate