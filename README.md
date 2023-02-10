# perfin

Для работы с проектом нужно установить [python](http://python.org)

## Запуск на локальном сервере (Windows)

### Файл .env
- `BOT_TOKEN=<ваш токен>` - необходимо вставить токен вашего бота (получить его можно у @BotFather)
- `HOST=<ваш хост>` - если хотите использовать WebHook

Если хотите использовать вебхук без своего хоста, можете использовать **ngrok**
- https://ngrok.com/download - скачать архив с консольным приложением
- `ngrok http 8000` - команда, которая создаст туннель для вашего локального хоста(его нужно добавить в .env)

### Запуск самого приложения
- `python -m venv venv` - создать виртуальное окружение
- `venv\Scripts\activate` - войти в виртуальное окружение
- `pip install -r requirements.txt` - установить зависимости
- `docker compose up -d` - поднять PostgreSQL и Redis через докер
- `python manage.py migrate` - запуск миграций базы данных
- `python manage.py runserver` - запуск локального сервера
- `celery --app perfin worker --pool=solo --loglevel=INFO` - запуск воркера celery
- `celery --app perfin beat` - запуск расписания django-celery-beat

В зависимости от того, как вы хотите запустить бота:
- `python polling.py` - запуск поллинга бота
- `python tgbot/webhook.py` - установка вебхука с вашего хоста
