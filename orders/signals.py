# """
# signals.py
# این فایل سیگنال‌های مربوط به مدل Order را شامل می‌شود.
# وقتی یک سفارش با وضعیت پرداخت‌شده ساخته می‌شود،
# یک ایمیل و یک پیامک خرید موفق به کاربر ارسال می‌شود.
# """
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
#
# from .models import Order
# from digital_web.config.sms import send_sms  # ← ایمپورت تابع پیامک
#
#
# @receiver(post_save, sender=Order)
# def send_order_success_email_and_sms(sender, instance, created, **kwargs):
#     """
#     سیگنالی که پس از ذخیره Order فراخوانی می‌شود.
#     اگر سفارش جدید و پرداخت‌شده باشد،
#     یک ایمیل و یک پیامک خرید موفق به کاربر ارسال می‌شود.
#     """
#     if created and instance.paid:
#         # --- ارسال ایمیل ---
#         subject = "خرید شما با موفقیت انجام شد"
#         message = f"""
#         سلام {instance.buyer.username}
#
#         سفارش شما برای محصول "{instance.product.title}" با موفقیت ثبت و پرداخت شد.
#
#         قیمت نهایی: {instance.total_price} تومان
#
#         با تشکر از خرید شما
#         """
#         recipient_list = [instance.buyer.email]
#         from_email = settings.DEFAULT_FROM_EMAIL
#
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=from_email,
#             recipient_list=recipient_list,
#             fail_silently=False,
#         )
#
#         # --- ارسال پیامک ---
#         phone = instance.buyer.profile.phone
#         if phone:
#             sms_message = f"خرید شما برای محصول {instance.product.title} با موفقیت انجام شد."
#             send_sms(phone=phone, message=sms_message)
