import os
import sys
import logging

import telegram
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telegram.Bot(BOT_TOKEN)
TELEGRAM_BOT_USERNAME = bot.get_me()["username"]

try:
    pass
except telegram.error.Unauthorized:
    logging.error("Invalid TELEGRAM_TOKEN.")
    sys.exit(1)
