from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=120, verbose_name="اسم")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=200, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "تماس ها"
        verbose_name_plural = "تماس ها"
