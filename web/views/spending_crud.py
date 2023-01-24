from django.views.generic import ListView

from web.models import Spending


class SpendingsListView(ListView):
    template_name = "web/spendings.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Spending.objects.filter(user=self.request.user)
        return Spending.objects.none()
