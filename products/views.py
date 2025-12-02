from django.shortcuts import render, get_object_or_404
from .models import *

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/detail.html", {"product": product})

def product_by_type(request, type_id):
    type_obj = get_object_or_404(DiscountCode, pk=type_id)
    products = Product.objects.filter(type=type_obj)
    return render(request, "products/list.html", {"products": products, "type": type_obj})
