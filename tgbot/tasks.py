from telegram import Update

from perfin.celery import app
from tgbot.main import bot_app


@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot_app.bot)
    print(update.message.text)
    bot_app.process_update(update)
