from celery import shared_task

from web.models import Reminder


@shared_task(name="send_notification")
def send_notification(id: int):
    reminder = Reminder.objects.get(pk=id)
    print("------------------------------------------")
    print(reminder.title, reminder.text)
    print("------------------------------------------")
