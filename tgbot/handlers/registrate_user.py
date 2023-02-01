from telegram import Update
from telegram.ext import ContextTypes

from web.models import User

REGISTRATION = range(1)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Привет {user.name}!\nВведи почту, на которую зарегстрирован аккаунт в perfin:",
    )

    return REGISTRATION


async def registrate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    email = update.message.text
    user = User.objects.get(email=email)
    if user:
        await update.message.reply_text(
            f"Аккаунт с почтой {user.email} привязан к этому чату",
        )
