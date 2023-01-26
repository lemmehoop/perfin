from datetime import date, timedelta

from django.shortcuts import render
from django.views import View
from django.db.models import Sum

from web.enums import Category
from web.models import Spending


class StatsView(View):
    def get_values(self, request):
        res = []
        aggregated = Spending.objects.filter(user=request.user)\
            .filter(created_at__gt=date.today()-timedelta(days=31))\
            .values("category")\
            .annotate(count=Sum("amount")).order_by("-count")
        for spending in aggregated:
            res.append([Category[spending["category"]].label, spending["count"]])

        return res

    def get(self, request):
        context = {
            "values": self.get_values(request),
        }

        return render(self.request, "web/stats.html", context)
