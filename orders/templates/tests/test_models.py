from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from products.models import Product, DiscountCode
from orders.models import Order

User = get_user_model()


class OrderModelTest(TestCase):
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
        self.discount = DiscountCode.objects.create(
            code="DISCOUNT10",
            discount_percent=10,
        )
        self.order = Order.objects.create(
            buyer=self.user,
            product=self.product,
            discount=self.discount,
            total_price=Decimal("9000.00"),
            paid=True,
        )

    def test_str_representation(self):
        expected = f"Order #{self.order.id} by {self.user.username}"
        self.assertEqual(str(self.order), expected)

    def test_meta_verbose_name(self):
        self.assertEqual(Order._meta.verbose_name, "سفارش")
        self.assertEqual(Order._meta.verbose_name_plural, "سفارش‌ها")

    def test_meta_ordering(self):
        order1 = Order.objects.create(
            buyer=self.user,
            product=self.product,
            total_price=Decimal("10000.00"),
            paid=False,
        )
        order2 = Order.objects.create(
            buyer=self.user,
            product=self.product,
            total_price=Decimal("20000.00"),
            paid=True,
        )
        qs = Order.objects.all()
        self.assertEqual(list(qs), [order2, order1])

    def test_status_property_paid(self):
        self.order.paid = True
        self.order.save()
        self.assertEqual(self.order.status, "پرداخت شده")

    def test_status_property_unpaid(self):
        self.order.paid = False
        self.order.save()
        self.assertEqual(self.order.status, "پرداخت نشده")

    def test_paid_order_manager_paid_orders(self):
        paid_order = Order.objects.create(
            buyer=self.user,
            product=self.product,
            total_price=Decimal("10000.00"),
            paid=True,
        )
        unpaid_order = Order.objects.create(
            buyer=self.user,
            product=self.product,
            total_price=Decimal("20000.00"),
            paid=False,
        )

        paid_qs = Order.objects.paid_orders()
        unpaid_qs = Order.objects.unpaid_orders()

        self.assertIn(paid_order, paid_qs)
        self.assertNotIn(unpaid_order, paid_qs)

        self.assertIn(unpaid_order, unpaid_qs)
        self.assertNotIn(paid_order, unpaid_qs)

    def test_paid_order_manager_by_user(self):
        user1 = User.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="12345",
        )
        user2 = User.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="12345",
        )

        order1 = Order.objects.create(
            buyer=user1,
            product=self.product,
            total_price=Decimal("10000.00"),
            paid=True,
        )
        order2 = Order.objects.create(
            buyer=user2,
            product=self.product,
            total_price=Decimal("20000.00"),
            paid=True,
        )

        qs = Order.objects.by_user(user1)
        self.assertIn(order1, qs)
        self.assertNotIn(order2, qs)
