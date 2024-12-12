from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import *


class CreateUser(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


class LoginUser(AuthenticationForm):

    class Meta:

        model = User
        fields = ['username', 'password']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = []
