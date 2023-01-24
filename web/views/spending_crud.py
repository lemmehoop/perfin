from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView

from web.forms import SpendingForm
from web.models import Spending


def main(request):
    return redirect("spendings")


class SpendingsListView(ListView):
    template_name = "web/spendings.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Spending.objects.filter(user=self.request.user)
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
    category_id = request.POST.get("category")
    spending = Spending.objects.create(
        title=title,
        amount=amount,
        category_id=category_id,
        user=request.user
    )

    return JsonResponse({
        "title": spending.title,
        "amount": spending.amount,
        "category": spending.category.title,
        "csrftoken": request.POST.get("csrfmiddlewaretoken")
    })
