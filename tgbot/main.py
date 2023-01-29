import os

from dotenv import load_dotenv, find_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from tgbot.handlers import start, echo

load_dotenv(find_dotenv())

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Application.builder().token(BOT_TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

bot.run_polling()
