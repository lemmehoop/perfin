from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from web.models import User, Spending


class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(
        label=_("Почта"),
        label_suffix="",
        widget=forms.EmailInput(attrs={"class": "form-control mb-3"}))
    password1 = forms.CharField(
        label=_("Пароль"),
        label_suffix="",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control mb-3"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control mb-3"}),
        label_suffix="",
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ["email"]


class AuthForm(forms.Form):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    email = forms.EmailField(
        label=_("Почта"),
        widget=forms.EmailInput(attrs={"autofocus": True, "class": "form-control mb-3"}))
    password = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control mb-3"}),
    )
    remember_me = forms.BooleanField(
        label="Запомнить меня",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mb-3"}),
        required=False
    )

    error_messages = {
        "invalid_login": _("Удостоверьтесь, что вы правильно ввели почту и пароль"),
    }

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        remember_me = self.cleaned_data.get("remember_me")

        if self.is_valid():
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                if not remember_me:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                else:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"email": self.cleaned_data["email"]},
        )


class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ("title", "amount", "category")
