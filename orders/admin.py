from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'product', 'total_price', 'paid', 'created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('buyer__username', 'product__title')
