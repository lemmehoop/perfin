import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from pytz import timezone as tz
from django.http import JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.utils.timezone import make_aware
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, UpdateView, DeleteView
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from web.models import Reminder
from web.forms import ReminderForm


class RemindersListView(LoginRequiredMixin, ListView):
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


class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    slug_field = "id"
    slug_url_kwarg = "id"
    form_class = ReminderForm
    template_name = "web/single_obj_update.html"

    def get_queryset(self):
        queryset = Reminder.objects.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        super(ReminderUpdateView, self).form_valid(form)
        task = PeriodicTask.objects.filter(name=f"send_notification_{self.object.id}").first()
        cron = CrontabSchedule.objects.filter(pk=task.crontab_id).first()
        cron.minute = str(self.object.remind_at.minute)
        self.object.remind_at -= self.object.remind_at.utcoffset()  # to contain datetime in UTC
        cron.hour = str(self.object.remind_at.hour)
        cron.day_of_month = str(self.object.remind_at.day)
        cron.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("reminders")


class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_success_url(self):
        return reverse("reminders")

    def form_valid(self, form):
        task = PeriodicTask.objects.filter(name=f"send_notification_{self.object.id}").first()
        CrontabSchedule.objects.filter(pk=task.crontab_id).first().delete()
        task.delete()
        super(ReminderDeleteView, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


@login_required
def add_reminder(request):
    title = request.POST.get("title")
    remind_at = request.POST.get("remind_at")
    text = request.POST.get("text")
    category = request.POST.get("category")
    amount = request.POST.get("amount")
    interval = request.POST.get("interval")

    naive_datetime = datetime.strptime(remind_at, '%Y-%m-%dT%H:%M')
    aware_datetime = make_aware(naive_datetime, timezone=tz(str(timezone.get_current_timezone())))

    reminder = Reminder.objects.create(
        title=title,
        remind_at=aware_datetime,
        text=text,
        category=category,
        amount=amount,
        user=request.user
    )
    aware_datetime -= aware_datetime.utcoffset()

    crontab, _ = CrontabSchedule.objects.get_or_create(
        minute=str(aware_datetime.minute),
        hour=str(aware_datetime.hour),
        day_of_week="*" if interval != "week" else str(aware_datetime.weekday()),
        day_of_month="*" if interval != "month" else str(aware_datetime.day),
        month_of_year="*",
    )

    # PeriodicTask.objects.create(
    #     name=f"send_notification_{reminder.id}",
    #     task="send_notification",
    #     crontab=crontab,
    #     kwargs=json.dumps({"id": reminder.id}),
    #     start_time=timezone.now(),
    # )

    return JsonResponse({
        "title": reminder.title,
        "text": reminder.text,
        "category": reminder.category,
        "remind_at": reminder.remind_at,
        "amount": reminder.amount
    })
