from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import List, User

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
