from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from orders.models import Order
from products.models import Product
from mediafiles.models import Image

User = get_user_model()


class MediafilesViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="12345",
        )
        self.product = Product.objects.create(
            title="محصول تست",
            description="توضیحات محصول تست",
            price=10000,
            is_active=True,
        )
        self.image = Image.objects.create(
            product=self.product,
            image="images/test.jpg",
            caption="تصویر تست",
        )
        self.product_ct = ContentType.objects.get_for_model(Product)

    def test_gallery_view(self):
        url = reverse("mediafiles:mediafiles")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mediafiles/list.html")
        self.assertIn("files", response.context)
        self.assertEqual(list(response.context["files"]), [self.image])

    def test_downloads_view_unauthenticated(self):
        url = reverse("mediafiles:downloads")
        response = self.client.get(url)

        # چون login_required هست، باید به صفحه لاگین ریدایرکت بشه
        login_url = reverse("accounts:login")
        self.assertRedirects(response, f"{login_url}?next={url}")

    def test_downloads_view_authenticated_no_orders(self):
        self.client.login(username="testuser", password="12345")
        url = reverse("mediafiles:downloads")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mediafiles/downloads.html")
        self.assertEqual(list(response.context["orders"]), [])
        self.assertEqual(list(response.context["files"]), [])

    def test_downloads_view_authenticated_with_paid_orders(self):
        self.client.login(username="testuser", password="12345")
        url = reverse("mediafiles:downloads")

        order = Order.objects.create(
            buyer=self.user,
            product=self.product,
            paid=True,
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mediafiles/downloads.html")

        orders = list(response.context["orders"])
        files = list(response.context["files"])

        self.assertIn(order, orders)
        self.assertIn(self.image, files)
