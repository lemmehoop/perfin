from datetime import date, timedelta

from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import ListView

from web.enums import Category
from web.forms import SpendingForm
from web.models import Spending


class SpendingsListView(ListView):
    template_name = "web/spendings.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Spending.objects.filter(user=self.request.user).order_by("-created_at")
        return Spending.objects.none()

    def get_values(self):
        res = []
        aggregated = Spending.objects.filter(user=self.request.user)\
            .filter(created_at__gt=date.today()-timedelta(days=31))\
            .values("category")\
            .annotate(count=Count("id")).order_by("-count")
        for spending in aggregated:
            res.append([Category[spending["category"]].label, spending["count"]])

        return res

    def get_context_data(self, *, object_list=None, **kwargs):
        if not self.request.user.is_authenticated:
            return {}
        return {
            **super(SpendingsListView, self).get_context_data(),
            "form": SpendingForm,
            "values": self.get_values()
        }


def add_spending(request):
    title = request.POST.get("title")
    amount = request.POST.get("amount")
    category = request.POST.get("category")
    spending = Spending.objects.create(
        title=title,
        amount=amount,
        category=category,
        user=request.user
    )

    return JsonResponse({
        "title": spending.title,
        "amount": spending.amount,
        "category": spending.category,
    })
