from django.http import JsonResponse
from django.views.generic import ListView

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

    reminder = Reminder.objects.create(
        title=title,
        remind_at=remind_at,
        text=text,
        category=category,
        amount=amount,
        user=request.user
    )

    return JsonResponse({
        "title": reminder.title,
        "text": reminder.text,
        "category": reminder.category,
        "remind_at": reminder.remind_at,
        "amount": reminder.amount
    })
