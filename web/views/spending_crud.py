from django.http import JsonResponse
from django.views.generic import ListView

from web.forms import SpendingForm
from web.models import Spending


class SpendingsListView(ListView):
    template_name = "web/spendings.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Spending.objects.filter(user=self.request.user).order_by("-created_at")
        return Spending.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        if not self.request.user.is_authenticated:
            return {}
        return {
            **super(SpendingsListView, self).get_context_data(),
            "form": SpendingForm,
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
