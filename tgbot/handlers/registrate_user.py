import os
import django
from asgiref.sync import sync_to_async
from django.contrib.auth.hashers import check_password

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perfin.settings')
django.setup()

from web.models import User

REGISTRATION, = range(1)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Привет {user.name}!\nВведите почту и пароль аккаунта perfin через пробел",
    )

    return REGISTRATION


async def registrate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    email, password = update.message.text.split()
    try:
        user = await sync_to_async(User.objects.get)(email=email)
    except User.DoesNotExist:
        user = None

    if user and check_password(password, user.password):
        await update.message.reply_text(
            f"Аккаунт с почтой {user.email} привязан к этому чату\nОжидаю уведомления...",
        )
        user.chat_id = update.message.chat_id
        await sync_to_async(user.save)()
        return ConversationHandler.END
    else:
        await update.message.reply_text("Пароль или почта неправильные\nПопробуйте еще раз")
        return REGISTRATION


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text="Останавливаюсь"
    )
    return ConversationHandler.END
