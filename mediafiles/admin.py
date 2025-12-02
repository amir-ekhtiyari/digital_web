from django.contrib import admin
from .models import Image
from django.contrib.contenttypes.admin import GenericTabularInline, GenericInlineModelAdmin

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'caption', 'uploaded_at')
    search_fields = ('caption',)
