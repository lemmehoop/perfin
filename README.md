# perfin

Для работы с проектом нужно установить [python](http://python.org)

## Запуск на локальном сервере (Windows)
- `python -m venv venv` - создать виртуальное окружение
- `venv\Scripts\activate` - войти в виртуальное окружение
- `pip install -r requirements.txt` - установить зависимости
- `docker compose up -d` - поднять PostgreSQL и Redis через докер
- `python manage.py migrate` - запуск миграций базы данных
- `python manage.py runserver` - запуск локального сервера
- `celery --app perfin worker --pool=solo --loglevel=INFO` - запуск воркера celery
- `celery --app perfin beat` - запуск расписания django-celery-beat
- `python polling.py` - запуск поллинга бота
