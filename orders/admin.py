from django.contrib import admin
from .models import Order
from mediafiles.admin import GenericImageInline



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'product', 'total_price', 'paid', 'status', 'created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('buyer__username', 'product__title')
    list_editable = ('paid',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'status')
    inlines = [GenericImageInline]

    list_per_page = 25

    fieldsets = (
        ('اطلاعات سفارش', {
            'fields': ('buyer', 'product', 'discount', 'total_price', 'paid')
        }),
        ('وضعیت و تاریخ', {
            'fields': ('status', 'created_at')
        }),
    )

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"
