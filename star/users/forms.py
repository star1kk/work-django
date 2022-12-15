from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'textinput textInput form-control is-invalid', 'pattern': '[a-zA-Zа-яА-Я]+'}),
            'last_name': forms.TextInput(attrs={'class': 'textinput textInput form-control is-invalid', 'pattern': '[a-zA-Zа-яА-Я]+'})
        }
        fields = ("username", "email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")
