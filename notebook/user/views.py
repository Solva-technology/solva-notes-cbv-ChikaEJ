from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView

from .forms.form import RegisterForm
from .models import UserProfile


class UserMixin(LoginRequiredMixin):
    model = UserProfile


class UserProfileListView(UserMixin, ListView):
    template_name = 'users/all_users.html'
    context_object_name = 'users'


class UserProfileDetailView(UserMixin, DetailView):
    template_name = 'users/user_detail.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile
                                 .objects
                                 .select_related('user'),
                                 user__id=self.kwargs['pk']
                                 )


class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = 'notes:my_notes'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return redirect('/')
