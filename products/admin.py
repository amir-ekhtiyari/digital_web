from django.contrib import admin
from .models import Product, DiscountCode
from mediafiles.models import Image


class ImageInline(admin.TabularInline):
    model = Image
    fk_name = "product"      # خیلی مهم: دقیقاً اسم FK تو مدل Image
    extra = 1
    fields = ("image", "caption")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ("id", "title", "seller", "category", "price", "is_active", "created_at")


@admin.register(DiscountCode)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "discount_percent", "active", "created_at")
