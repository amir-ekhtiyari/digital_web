from django.contrib import admin
from django.utils.html import format_html
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product_id", "product", "file_name", "file_url", "preview", "uploaded_at")
    list_filter = ("uploaded_at",)
    search_fields = ("product__title", "caption", "image")

    @admin.display(description="File")
    def file_name(self, obj):
        return obj.image.name

    @admin.display(description="URL")
    def file_url(self, obj):
        return obj.image.url if obj.image else "-"

    @admin.display(description="Preview")
    def preview(self, obj):
        if not obj.image:
            return "-"
        return format_html('<img src="{}" style="height:40px;width:auto;border-radius:6px;" />', obj.image.url)
