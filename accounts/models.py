from django.conf import settings
from django.db import models


class ProfileManager(models.Manager):
    def sellers(self):
        return self.filter(role='seller')

    def buyers(self):
        return self.filter(role='buyer')


class Profile(models.Model):
    ROLE_CHOICES = (
        ('seller', 'فروشنده'),
        ('buyer', 'خریدار'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
        related_name='profile',
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        verbose_name='نقش کاربر',
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        verbose_name='شماره تماس',
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='عکس پروفایل',
    )

    objects = ProfileManager()

    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"
        ordering = ['user__username']

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
