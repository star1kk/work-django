from django.urls import reverse_lazy
from django.views import generic

from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'edit_user.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'
    fields = ["username", "email", "first_name", "last_name"]
