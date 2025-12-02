from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def order_list(request):
    orders = Order.objects.filter(buyer=request.user)
    return render(request, "orders/list.html", {"orders": orders})

@login_required
def checkout(request):
    return render(request, "orders/detail.html")
