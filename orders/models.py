from django.db import models
from django.contrib.auth.models import User
from products.models import Product, DiscountCode


class PaidOrderManager(models.Manager):
    def paid_orders(self):
        return self.filter(paid=True)

    def unpaid_orders(self):
        return self.filter(paid=False)

    def by_user(self, user):
        return self.filter(buyer=user)


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='خریدار')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='فایل')
    discount = models.ForeignKey(DiscountCode, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='کد تخفیف')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت نهایی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')

    objects = PaidOrderManager()

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username}"

    @property
    def status(self):
        return "پرداخت شده" if self.paid else "در انتظار پرداخت"
