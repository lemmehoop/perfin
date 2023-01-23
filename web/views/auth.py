from django.urls import reverse
from django.shortcuts import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as DjangoLoginView


from web.forms import UserCreationForm, AuthForm


def main(request):
    return HttpResponse(f"{request.user.is_authenticated}")


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "web/registration.html"

    def get_success_url(self):
        return self.request.GET.get("next") or reverse("main")


class LoginView(DjangoLoginView):
    form_class = AuthForm
    template_name = "web/login.html"

    def get_success_url(self):
        return self.request.GET.get("next") or reverse("main")
