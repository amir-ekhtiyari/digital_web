from django.db import models
from django.conf import settings
from django.urls import reverse

class ActiveProductManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def by_category(self, category_name):
        return self.filter(category=category_name, is_active=True)


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('book', 'کتاب'),
        ('music', 'موسیقی'),
        ('article', 'مقاله'),
        ('image', 'تصویر'),
        ('other', 'سایر'),
    )

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='فروشنده', related_name='products')
    title = models.CharField(max_length=100, verbose_name='عنوان فایل')
    description = models.TextField(verbose_name='توضیحات')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='دسته‌بندی')
    file = models.FileField(upload_to='uploads/', verbose_name='فایل')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت (تومان)')
    keywords = models.CharField(max_length=200, blank=True, verbose_name='کلمات کلیدی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    objects = ActiveProductManager()

    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.seller.username}"

    def get_absolute_url(self):
        return reverse('products:detail', args=[self.pk])

    def get_main_image(self):
        from django.contrib.contenttypes.models import ContentType
        from mediafiles.models import Image

        ct = ContentType.objects.get_for_model(self.__class__)
        img = Image.objects.filter(content_type=ct, object_id=self.pk).first()
        if img:
            return img.image
        return None


class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name='کد تخفیف')
    discount_percent = models.IntegerField(verbose_name='درصد تخفیف')
    active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کدهای تخفیف"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.code} ({self.discount_percent}%)"
