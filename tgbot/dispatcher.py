from django.conf.global_settings import DEBUG
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters, Dispatcher

from tgbot.handlers import start, REGISTRATION, registrate, stop
from tgbot.main import bot


def setup_dispatcher(dp: Dispatcher):
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            REGISTRATION: [MessageHandler(Filters.text, registrate)],
        },
        fallbacks=[CommandHandler("stop", stop)]
    ))

    return dp


n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(
    bot=bot,
    update_queue=None,
    workers=n_workers,
    use_context=True
))
