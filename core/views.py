from django.shortcuts import render, get_object_or_404
from products.models import Product


def home(request):
    products = Product.objects.all()[:6]
    return render(request, "core/home.html", {"products": products})

def about(request):
    return render(request, "core/about.html")
