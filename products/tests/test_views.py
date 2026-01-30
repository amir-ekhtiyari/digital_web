from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.models import Product, DiscountCode

User = get_user_model()


class ProductsViewsTest(TestCase):
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
        self.discount = DiscountCode.objects.create(
            code="DISCOUNT10",
            discount_percent=10,
            active=True,
        )

    def test_product_list(self):
        url = reverse("products:list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/list.html")
        self.assertIn("products", response.context)
        products = list(response.context["products"])
        self.assertIn(self.product, products)

    def test_product_detail(self):
        url = reverse("products:detail", args=[self.product.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/detail.html")
        self.assertIn("product", response.context)
        self.assertEqual(response.context["product"], self.product)

    def test_product_by_type(self):
        url = reverse("products:by_type", args=[self.discount.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/list.html")
        self.assertIn("products", response.context)
        self.assertIn("type", response.context)
        self.assertEqual(response.context["type"], self.discount)
