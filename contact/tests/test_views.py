from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from contact.models import ContactMessage

User = get_user_model()


class ContactViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="12345",
        )
        self.url = reverse("contact:form")

    def test_contact_view_get_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={self.url}"
        )

    def test_contact_view_get_authenticated(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsInstance(response.context["form"], ContactForm)

    def test_contact_view_post_valid(self):
        self.client.login(username="testuser", password="12345")
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "ali@example.com",
            "subject": "درخواست همکاری",
            "message": "می‌خوام با شما همکاری کنم.",
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, self.url)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.first_name, "علی")
        self.assertEqual(msg.last_name, "احمدی")
        self.assertEqual(msg.email, "ali@example.com")
        self.assertEqual(msg.subject, "درخواست همکاری")
        self.assertEqual(msg.message, "می‌خوام با شما همکاری کنم.")

    def test_contact_view_post_invalid(self):
        self.client.login(username="testuser", password="12345")
        data = {
            "first_name": "علی",
            "last_name": "احمدی",
            "email": "",  # ایمیل خالی
            "subject": "درخواست همکاری",
            "message": "می‌خوام با شما همکاری کنم.",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertContains(response, "این فیلد الزامی است")
