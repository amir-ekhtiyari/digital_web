# """
# sms.py
# این فایل تنظیمات و توابع مربوط به ارسال پیامک (مثل Kavenegar) را شامل می‌شود.
# """
# import requests
# from django.conf import settings
#
#
# def send_sms(phone, message):
#     """
#     ارسال پیامک به کاربر از طریق سرویس Kavenegar.
#
#     Args:
#         phone (str): شماره موبایل کاربر.
#         message (str): متن پیامک.
#
#     Returns:
#         None
#     """
#     url = f"https://api.kavenegar.com/v1/{settings.KAVENEGAR_API_KEY}/sms/send.json"
#     data = {
#         "receptor": phone,
#         "message": message,
#     }
#     try:
#         response = requests.post(url, data=data)
#         # در حالت توسعه می‌توان پاسخ را لاگ کرد
#         print("SMS response:", response.json())
#     except Exception as e:
#         print("SMS send failed:", e)
