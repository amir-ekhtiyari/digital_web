from django.test import TestCase

from products.models import Product
from mediafiles.models import Image


class ImageModelTest(TestCase):
    def setUp(self):
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

    def test_str_representation(self):
        expected = f"{self.product.id} - {self.image.id}"
        self.assertEqual(str(self.image), expected)

    def test_meta_ordering(self):
        img1 = Image.objects.create(
            product=self.product,
            image="images/1.jpg",
        )
        img2 = Image.objects.create(
            product=self.product,
            image="images/2.jpg",
        )
        qs = Image.objects.all()
        self.assertEqual(list(qs), [img2, img1])
