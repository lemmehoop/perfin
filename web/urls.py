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

from web.views import RegistrationView, LoginView, LogoutView, MainView, SpendingsListView, add_spending, \
    SpendingUpdateView, StatsView, ProfileFormView, RemindersListView, add_reminder, ReminderUpdateView, \
    ReminderDeleteView, SpendingDeleteView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("spendings/", SpendingsListView.as_view(), name="spendings"),
    path("spendings/add_spending", add_spending, name="add_spending"),
    path("spendings/<int:id>/", SpendingUpdateView.as_view(), name="update_spending"),
    path("spendings/<int:id>/delete/", SpendingDeleteView.as_view(), name="delete_spending"),
    path("stats/", StatsView.as_view(), name="stats"),
    path("profile/", ProfileFormView.as_view(), name="profile"),
    path("reminders/", RemindersListView.as_view(), name="reminders"),
    path("reminders/add_reminder", add_reminder, name="add_reminder"),
    path("reminders/<int:id>/", ReminderUpdateView.as_view(), name="update_reminder"),
    path("reminders/<int:id>/delete/", ReminderDeleteView.as_view(), name="delete_reminder"),
]
