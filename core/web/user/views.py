from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from core.web.user.forms import UserModelForm, UserLoginForm, UserRegistrationForm


def login(request):
    """
    Login view
    """

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
            else:
                form.add_error(None, "Invalid credentials")
                return render(request, "user/login.html", {"form": form})
            return redirect("index")
        else:
            return render(request, "user/login.html", {"form": form})

    form = UserLoginForm()

    return render(request, "user/login.html", {"form": form})


def register(request):
    """
    Register view
    """

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
        else:
            return render(request, "user/register.html", {"form": form})

    form = UserRegistrationForm()

    return render(request, "user/register.html", {"form": form})


@login_required(login_url="/user/login/")
def logout(request):
    """
    Logout view
    """

    auth_logout(request)

    return redirect("user:login")


@login_required(login_url="/user/login/")
def profile(request):
    """
    Profile view
    """

    user = request.user

    if request.method == "POST":
        form = UserModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        else:
            return render(request, "user/profile.html", {"form": form})

    form = UserModelForm(instance=user)

    return render(request, "user/profile.html", {"form": form})
