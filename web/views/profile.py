from django.urls import reverse_lazy
from django.views.generic import UpdateView

from web.forms import UserForm
from web.models import User


class ProfileFormView(UpdateView):
    template_name = "web/profile.html"
    form_class = UserForm
    model = User
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
