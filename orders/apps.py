"""
apps.py
تنظیمات اپلیکیشن orders.
در اینجا سیگنال‌ها رجیستر می‌شوند.
"""
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "orders"
    #
    # def ready(self):
    #     import orders.signals  # ← رجیستر سیگنال‌ها
