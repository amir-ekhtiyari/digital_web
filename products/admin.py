from django.contrib import admin
from .models import Product, DiscountCode
from mediafiles.models import Image
from django.contrib.contenttypes.admin import GenericTabularInline

class ImageInline(GenericTabularInline):
    model = Image
    ct_field = "content_type"
    ct_fk_field = "object_id"
    extra = 1
    readonly_fields = ()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'description', 'seller__username')
    inlines = [ImageInline]

@admin.register(DiscountCode)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('code',)
