from datetime import date, timedelta

from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Q

from web.enums import Category
from web.models import Spending


class StatsView(View):
    def get_values(self, request, start_date, end_date):
        res = []
        aggregated = Spending.objects.filter(user=request.user)\
            .filter(Q(created_at__gte=start_date) & Q(created_at__lte=end_date))\
            .values("category")\
            .annotate(count=Sum("amount")).order_by("-count")
        for spending in aggregated:
            res.append([Category[spending["category"]].label, spending["count"]])

        return res

    def get(self, request):
        context = {
            "values": self.get_values(request, date.today() - timedelta(days=31), date.today() + timedelta(days=1)),
            "categories": Category.choices,
            "result": Spending.objects.filter(Q(created_at__gte=date.today() - timedelta(days=31)) &
                                              Q(user=request.user)).order_by("-created_at")
        }

        return render(self.request, "web/stats.html", context)

    def post(self, request):
        search = request.POST.get("search")
        category = request.POST.get("category")
        start_date = request.POST.get("start_date") or date.today()
        end_date = request.POST.get("end_date") or date.today() + timedelta(days=1)

        result = Spending.objects.filter(Q(user=request.user) & Q(title__icontains=search)
                                         & Q(category__icontains=category) & Q(created_at__gte=start_date)
                                         & Q(created_at__lte=end_date)).order_by("-created_at")

        context = {
            "values": self.get_values(request, start_date, end_date),
            "categories": Category.choices,
            "result": result,
            "search": search,
            "category": category,
            "start": start_date,
            "end": end_date,
        }

        return render(self.request, "web/stats.html", context)
