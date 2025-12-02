from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "با موفقیت وارد شدید.")
            return redirect("core:home")
        messages.error(request, "اطلاعات نادرست است.")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("core:home")

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")
