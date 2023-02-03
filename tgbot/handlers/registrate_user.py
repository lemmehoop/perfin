import os
import django
from django.contrib.auth.hashers import check_password

from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perfin.settings')
django.setup()

from web.models import User

REGISTRATION, = range(1)


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    update.message.reply_text(
        f"Привет {user.name}!\nВведите почту и пароль аккаунта perfin через пробел",
    )

    return REGISTRATION


def registrate(update: Update, context: CallbackContext) -> None:
    email, password = update.message.text.split()
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None

    if user and check_password(password, user.password):
        update.message.reply_text(
            f"Аккаунт с почтой {user.email} привязан к этому чату\nОжидаю уведомления...",
        )
        user.chat_id = update.message.chat_id
        user.save()
        return ConversationHandler.END
    else:
        update.message.reply_text("Пароль или почта неправильные\nПопробуйте еще раз")
        return REGISTRATION


async def stop(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Останавливаюсь"
    )
    return ConversationHandler.END
