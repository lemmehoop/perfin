from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from web.models import User


class UserCreationForm(DjangoUserCreationForm):

    class Meta:
        model = User
        fields = ["email"]
