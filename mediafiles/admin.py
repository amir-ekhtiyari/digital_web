from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html
from .models import Image


class GenericImageInline(GenericTabularInline):  # 👈 تغییر مهم
    model = Image
    extra = 1
    fields = ('image', 'caption', 'preview')
    readonly_fields = ('preview',)
    verbose_name = "تصویر مرتبط"
    verbose_name_plural = "تصاویر مرتبط"

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:10px;" />', obj.image.url)
        return ""
    preview.short_description = "پیش‌نمایش"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'caption', 'uploaded_at')
    search_fields = ('caption',)
    ordering = ('-uploaded_at',)
