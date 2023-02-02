import os

import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TELEGRAM_URL = "https://api.telegram.org/bot"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
HOST = os.environ.get("HOST")


def set_webhook():
    requests.get(
        url=f"{TELEGRAM_URL}{BOT_TOKEN}/setWebhook",
        params={"url": f"{HOST}/tg/webhook/"}
    )


if __name__ == "__main__":
    set_webhook()
