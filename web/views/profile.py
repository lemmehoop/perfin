from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from web.forms import UserForm
from web.models import User


class ProfileFormView(LoginRequiredMixin, UpdateView):
    template_name = "web/profile.html"
    form_class = UserForm
    model = User
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        super(ProfileFormView, self).form_valid(form)
        update_session_auth_hash(self.request, self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return self.request.user
