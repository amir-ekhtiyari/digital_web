from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from products.models import Product, DiscountCode

User = get_user_model()


class ProductModelTest(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(
            username="seller",
            email="seller@example.com",
            password="12345",
        )
        self.product = Product.objects.create(
            seller=self.seller,
            title="محصول تست",
            description="توضیحات محصول تست",
            category="book",
            file="uploads/test.pdf",
            price=Decimal("10000.00"),
            is_active=True,
        )

    def test_str_representation(self):
        expected = f"{self.product.title} - {self.seller.username}"
        self.assertEqual(str(self.product), expected)

    def test_meta_verbose_name(self):
        self.assertEqual(Product._meta.verbose_name, "محصولات")
        self.assertEqual(Product._meta.verbose_name_plural, "محصولات")

    def test_meta_ordering(self):
        product1 = Product.objects.create(
            seller=self.seller,
            title="محصول ۱",
            description="توضیحات محصول ۱",
            category="book",
            file="uploads/1.pdf",
            price=Decimal("10000.00"),
            is_active=True,
        )
        product2 = Product.objects.create(
            seller=self.seller,
            title="محصول ۲",
            description="توضیحات محصول ۲",
            category="book",
            file="uploads/2.pdf",
            price=Decimal("20000.00"),
            is_active=True,
        )
        qs = Product.objects.all()
        self.assertEqual(list(qs), [product2, product1])

    def test_get_absolute_url(self):
        url = self.product.get_absolute_url()
        expected = f"/products/{self.product.pk}/"
        self.assertEqual(url, expected)

    def test_get_main_image(self):
        # این تست فرض می‌کنه که مدل Image از mediafiles ایجاد شده باشه
        # اگر نیاز داشتی، می‌تونیم بعداً تست‌های mediafiles رو هم اضافه کنیم
        pass  # برای الان اینجا فقط یک مثال داریم


class DiscountCodeModelTest(TestCase):
    def setUp(self):
        self.discount = DiscountCode.objects.create(
            code="DISCOUNT10",
            discount_percent=10,
            active=True,
        )

    def test_str_representation(self):
        expected = "DISCOUNT10 (10%)"
        self.assertEqual(str(self.discount), expected)

    def test_meta_verbose_name(self):
        self.assertEqual(DiscountCode._meta.verbose_name, "کد تخفیف")
        self.assertEqual(DiscountCode._meta.verbose_name_plural, "کدهای تخفیف")

    def test_meta_ordering(self):
        discount1 = DiscountCode.objects.create(
            code="DISCOUNT5",
            discount_percent=5,
            active=True,
        )
        discount2 = DiscountCode.objects.create(
            code="DISCOUNT15",
            discount_percent=15,
            active=True,
        )
        qs = DiscountCode.objects.all()
        self.assertEqual(list(qs), [discount2, discount1])
