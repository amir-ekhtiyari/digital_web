from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.models import Product
from orders.models import Order

User = get_user_model()


class OrdersViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="12345",
        )
        self.product = Product.objects.create(
            title="محصول تست",
            description="توضیحات محصول تست",
            price=Decimal("10000.00"),
            is_active=True,
        )
        self.order = Order.objects.create(
            buyer=self.user,
            product=self.product,
            total_price=Decimal("10000.00"),
            paid=True,
        )

    def test_order_list_unauthenticated(self):
        url = reverse("orders:list")
        response = self.client.get(url)

        # چون login_required هست، باید به صفحه لاگین ریدایرکت بشه
        login_url = reverse("accounts:login")
        self.assertRedirects(response, f"{login_url}?next={url}")

    def test_order_list_authenticated(self):
        self.client.login(username="testuser", password="12345")
        url = reverse("orders:list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/list.html")
        self.assertIn("orders", response.context)
        orders = list(response.context["orders"])
        self.assertIn(self.order, orders)

    def test_checkout_unauthenticated(self):
        url = reverse("orders:checkout")
        response = self.client.get(url)

        # چون login_required هست، باید به صفحه لاگین ریدایرکت بشه
        login_url = reverse("accounts:login")
        self.assertRedirects(response, f"{login_url}?next={url}")

    def test_checkout_authenticated(self):
        self.client.login(username="testuser", password="12345")
        url = reverse("orders:checkout")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/detail.html")
