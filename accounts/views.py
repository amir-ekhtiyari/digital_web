from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileUpdateForm, LoginForm, EmailLoginForm
from .models import Profile


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)

        # DEV: ایمیل/اکانت پیش‌فرض فعال
        user.is_active = True
        user.save()

        Profile.objects.get_or_create(user=user, defaults={"role": "buyer"})

        messages.success(request, "ثبت‌نام انجام شد. حالا می‌تونی وارد شوی.")
        return redirect("accounts:login")

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        identifier = form.cleaned_data["username_or_email"].strip()
        password = form.cleaned_data["password"].strip()

        user_obj = User.objects.filter(username__iexact=identifier).first()
        if user_obj is None:
            user_obj = User.objects.filter(email__iexact=identifier).first()

        if not user_obj:
            messages.error(request, "نام کاربری/ایمیل یا رمز عبور اشتباه است.")
            return render(request, "accounts/login.html", {"form": form})

        user = authenticate(request, username=user_obj.username, password=password)
        if user is None:
            messages.error(request, "نام کاربری/ایمیل یا رمز عبور اشتباه است.")
            return render(request, "accounts/login.html", {"form": form})

        login(request, user)
        return redirect("accounts:profile")

    return render(request, "accounts/login.html", {"form": form})


def email_login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    form = EmailLoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"].strip()
        password = form.cleaned_data["password"].strip()

        user_obj = User.objects.filter(email__iexact=email).first()
        if not user_obj:
            messages.error(request, "ایمیل یا رمز عبور اشتباه است.")
            return render(request, "accounts/email_login.html", {"form": form})

        user = authenticate(request, username=user_obj.username, password=password)
        if user is None:
            messages.error(request, "ایمیل یا رمز عبور اشتباه است.")
            return render(request, "accounts/email_login.html", {"form": form})

        login(request, user)
        return redirect("accounts:profile")

    return render(request, "accounts/email_login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("core:home")


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user, defaults={"role": "buyer"})

    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "پروفایل به‌روزرسانی شد.")
            return redirect("accounts:profile")
    else:
        p_form = ProfileUpdateForm(instance=profile)

    return render(request, "accounts/profile.html", {"profile": profile, "p_form": p_form})
