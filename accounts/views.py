from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("core:home")
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html",context)
    else:
        return redirect("core:home")

# @login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("core:home")

@login_required
def singup_view(request):
    return render(request, "accounts/singup.html")
