[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
# yetiMP3

Django App to download music from YouTube.

## Dev notes
Use python 3.6! For now...

### run application 
```
$ python --version
Python 3.6.x
$ source venv/bin/activate
$ python manage.py runserver 8080
```

### start redis
```
redis server
```

### start celery worker
```
celery -A yetiMP3 worker -l info
```


## Tech used

- Django
- Redis
- SQLite3
- Heroku