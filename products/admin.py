from django.contrib import admin
from .models import Product, DiscountCode
from django.contrib import admin
from mediafiles.admin import GenericImageInline



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('title', 'seller__username', 'keywords')
    list_editable = ('is_active',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25
    inlines = [GenericImageInline]

    fieldsets = (
        ('مشخصات فایل', {
            'fields': ('title', 'description', 'category', 'file', 'price', 'keywords', 'is_active')
        }),
        ('فروشنده', {
            'fields': ('seller',),
        }),
    )

    readonly_fields = ('created_at',)

    def get_queryset(self, request):
        """نمایش فقط محصولات خود فروشنده اگر ادمین نباشد"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(seller=request.user)

    class Meta:
        verbose_name = "فایل دیجیتال"
        verbose_name_plural = "فایل‌های دیجیتال"


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('code',)
    ordering = ('-created_at',)
    list_editable = ('active',)
    readonly_fields = ('created_at',)
    list_per_page = 20

    fieldsets = (
        ('مشخصات تخفیف', {
            'fields': ('code', 'discount_percent', 'active')
        }),
        ('زمان ایجاد', {
            'fields': ('created_at',)
        }),
    )

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کدهای تخفیف"
