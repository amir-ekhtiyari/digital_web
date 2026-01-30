from django.test import TestCase

from contact.models import ContactMessage


class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.msg = ContactMessage.objects.create(
            first_name="علی",
            last_name="احمدی",
            email="ali@example.com",
            subject="درخواست همکاری",
            message="می‌خوام با شما همکاری کنم.",
        )

    def test_str_representation(self):
        expected = "علی احمدی - درخواست همکاری"
        self.assertEqual(str(self.msg), expected)

    def test_meta_verbose_name(self):
        self.assertEqual(ContactMessage._meta.verbose_name, "پیام تماس")
        self.assertEqual(ContactMessage._meta.verbose_name_plural, "پیام‌های تماس")

    def test_ordering(self):
        msg1 = ContactMessage.objects.create(
            email="a@example.com",
            subject="a",
            message="a",
        )
        msg2 = ContactMessage.objects.create(
            email="b@example.com",
            subject="b",
            message="b",
        )
        # جدیدترین اول بیاد
        qs = ContactMessage.objects.all()
        self.assertEqual(list(qs), [msg2, msg1])
