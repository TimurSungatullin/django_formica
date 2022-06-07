from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from authorization.forms import LoginForm, RegisterForm


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse("posts:main"))

    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data["username1"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse("posts:main"))
    return render(request, 'authorization/login.html', {"form": form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("authorization:login"))


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("posts:main"))

    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect(reverse("posts:main"))
    return render(request, 'authorization/registration.html', {"form": form})
