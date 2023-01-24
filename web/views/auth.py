from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView


from web.forms import UserCreationForm, AuthForm


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "web/registration.html"

    def get_success_url(self):
        return reverse("login")


class LoginView(DjangoLoginView):
    form_class = AuthForm
    template_name = "web/login.html"

    def get_success_url(self):
        return self.request.GET.get("next") or reverse("main")


class LogoutView(DjangoLogoutView):
    def get_success_url(self):
        return reverse("login")
