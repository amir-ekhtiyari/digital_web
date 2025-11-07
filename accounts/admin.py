from django.contrib import admin
from .models import Profile
from mediafiles.admin import GenericImageInline


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'get_email')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'phone')
    ordering = ('user__username',)
    list_per_page = 20
    fieldsets = (
        ('اطلاعات کاربری', {
            'fields': ('user', 'role', 'phone')
        }),
    )
    readonly_fields = ('get_email',)
    inlines = [GenericImageInline]


    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'ایمیل کاربر'

    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"
