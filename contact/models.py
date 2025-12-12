from django.db import models


class ContactMessage(models.Model):
    first_name = models.CharField(
        max_length=120,
        verbose_name="نام",
        blank=True,
        default="",
    )
    last_name = models.CharField(
        max_length=120,
        verbose_name="نام خانوادگی",
        blank=True,
        default="",
    )
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ["-created_at"]
