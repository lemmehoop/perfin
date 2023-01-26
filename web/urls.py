"""perfin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from web.views.auth import RegistrationView, LoginView, LogoutView
from web.views.main import MainView
from web.views.spending_crud import SpendingsListView, add_spending, SpendingUpdateView
from web.views.stats import StatsView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("spendings/", SpendingsListView.as_view(), name="spendings"),
    path("spendings/add_spending", add_spending, name="add_spending"),
    path("spendings/<int:id>/", SpendingUpdateView.as_view(), name="update_spending"),
    path("stats/", StatsView.as_view(), name="stats"),
]
