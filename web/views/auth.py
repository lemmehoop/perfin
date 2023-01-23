from django.shortcuts import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView

from web.forms import UserCreationForm


def main(request):
    return HttpResponse(f"{request.user.is_authenticated}")


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "web/registration.html"

    def get_success_url(self):
        return self.request.GET.get("next") or reverse("main")
