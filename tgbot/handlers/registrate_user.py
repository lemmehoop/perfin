import os
import django
from asgiref.sync import sync_to_async

from telegram import Update
from telegram.ext import ContextTypes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perfin.settings')
django.setup()

from web.models import User

REGISTRATION, WAIT = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Привет {user.name}!\nВведи почту, на которую зарегистрирован аккаунт в perfin",
    )

    return REGISTRATION


async def registrate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    email = update.message.text
    try:
        user = await sync_to_async(User.objects.get)(email=email)
    except User.DoesNotExist:
        user = None

    if user:
        await update.message.reply_text(
            f"Аккаунт с почтой {user.email} привязан к этому чату\nОжидаю уведомления...",
        )
    else:
        await update.message.reply_text("Пользователя с такой почтой не существует\nПопробуйте еще раз")
        return REGISTRATION


# async def wait_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(
#         f"Все завершено! Ожидаю уведомления...",
#     )
