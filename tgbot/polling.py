from telegram.ext import Updater

from tgbot.dispatcher import setup_dispatcher
from tgbot.main import BOT_TOKEN

if __name__ == "__main__":
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    updater.start_polling()
    updater.idle()
