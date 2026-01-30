from django.test import TestCase
from django.urls import reverse

from products.models import Product


class CoreViewsTest(TestCase):
    def setUp(self):
        # چند محصول تستی می‌سازیم تا ویو home چیزی برای نمایش داشته باشه
        self.product1 = Product.objects.create(
            title="محصول ۱",
            description="توضیحات محصول ۱",
            price=10000,
            is_active=True,
        )
        self.product2 = Product.objects.create(
            title="محصول ۲",
            description="توضیحات محصول ۲",
            price=20000,
            is_active=True,
        )
        self.product3 = Product.objects.create(
            title="محصول ۳",
            description="توضیحات محصول ۳",
            price=30000,
            is_active=True,
        )
        # اگر بیشتر از ۳ محصول بسازیم، تست مطمئن می‌شه که فقط ۳ تا نمایش داده می‌شه
        self.product4 = Product.objects.create(
            title="محصول ۴",
            description="توضیحات محصول ۴",
            price=40000,
            is_active=True,
        )

    def test_home_view(self):
        url = reverse("core:home")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")

        # فقط ۳ محصول اول باید بیاد
        self.assertEqual(len(response.context["products"]), 3)
        products = list(response.context["products"])
        self.assertIn(self.product4, Product.objects.all())  # وجود داره
        self.assertNotIn(self.product4, products)  # ولی توی context نیست

    def test_about_view(self):
        url = reverse("core:about")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/about.html")
