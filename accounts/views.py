# accounts/views.py
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login, logout




def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "با موفقیت وارد شدی.")
            return redirect("accounts:profile")
        else:
            print(form.errors)  # این خط را اضافه کن
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("core:home")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user, defaults={"role": "buyer"})
            login(request, user)
            messages.success(request, "حسابت با موفقیت ساخته شد.")
            return redirect("accounts:profile")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "پروفایل به‌روزرسانی شد.")
            return redirect("accounts:profile")
    else:
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        "profile": profile,
        "p_form": p_form,
    }
    return render(request, "accounts/profile.html", context)

