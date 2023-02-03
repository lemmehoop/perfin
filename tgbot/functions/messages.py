from tgbot.dispatcher import dispatcher


def send_message(chat_id, text):
    dispatcher.bot.send_message(chat_id=chat_id, text=text)
