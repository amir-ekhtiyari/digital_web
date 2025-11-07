from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100, blank=True, verbose_name="توضیح تصویر")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"تصویر برای {self.content_object} ({self.id})"
