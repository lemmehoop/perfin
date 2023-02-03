from celery import shared_task

from tgbot.functions.messages import send_message
from web.models import Reminder


@shared_task(name="send_notification")
def send_notification(id: int):
    reminder = Reminder.objects.get(pk=id)
    send_message(chat_id=reminder.user.chat_id, text=reminder.title + "\n" + reminder.text)
    print("Notification was sent.")
