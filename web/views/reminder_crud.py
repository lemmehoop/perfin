import json

from pytz import timezone as tz
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.timezone import make_aware
from django.views.generic import ListView
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from web.forms import ReminderForm
from web.models import Reminder


class RemindersListView(ListView):
    template_name = "web/reminders.html"

    def get_queryset(self):
        queryset = Reminder.objects.filter(user=self.request.user).order_by("remind_at")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        if not self.request.user.is_authenticated:
            return {}
        return {
            **super(RemindersListView, self).get_context_data(),
            "form": ReminderForm,
        }


def add_reminder(request):
    title = request.POST.get("title")
    remind_at = request.POST.get("remind_at")
    text = request.POST.get("text")
    category = request.POST.get("category")
    amount = request.POST.get("amount")

    naive_datetime = datetime.strptime(remind_at, '%Y-%m-%dT%H:%M')
    aware_datetime = make_aware(naive_datetime, timezone=tz(settings.TIME_ZONE))

    reminder = Reminder.objects.create(
        title=title,
        remind_at=aware_datetime,
        text=text,
        category=category,
        amount=amount,
        user=request.user
    )

    crontab, _ = CrontabSchedule.objects.get_or_create(
        minute=remind_at[-2:],
        hour=remind_at[-5:-3],
        day_of_week="*",
        day_of_month=remind_at[-8:-6],
        month_of_year="*",
    )

    PeriodicTask.objects.create(
        name=f"send_notification_{reminder.id}",
        task="send_notification",
        crontab=crontab,
        kwargs=json.dumps({"id": reminder.id}),
        start_time=timezone.now(),
    )

    return JsonResponse({
        "title": reminder.title,
        "text": reminder.text,
        "category": reminder.category,
        "remind_at": reminder.remind_at,
        "amount": reminder.amount
    })
