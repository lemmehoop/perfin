import os

from dotenv import load_dotenv, find_dotenv
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters

from tgbot.handlers import start, registrate, REGISTRATION

load_dotenv(find_dotenv())

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Application.builder().token(BOT_TOKEN).build()

bot.add_handler(ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        REGISTRATION: [MessageHandler(filters.TEXT, registrate)],
    },
    fallbacks=[]
))

if __name__ == "__main__":
    bot.run_polling()
