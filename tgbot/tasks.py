from telegram import Update

from perfin.celery import app
from tgbot.dispatcher import dispatcher
from tgbot.main import bot


@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot)
    print(update.message.text)
    dispatcher.process_update(update)
