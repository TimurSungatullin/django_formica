from django.contrib.auth.models import User
from django.core import validators
from django import forms


class LoginForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput, label='Пароль')
    username1 = forms.CharField(label='Логин', validators=[])

    class Meta:
        model = User
        fields = ["username1", "password"]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput, label='Пароль')
    username = forms.CharField(label='Логин')
    email = forms.CharField(validators=[validators.validate_email], label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]
