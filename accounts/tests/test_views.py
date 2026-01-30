from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from accounts.models import Profile

User = get_user_model()


class AccountsViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="12345",
        )
        self.profile = Profile.objects.get_or_create(user=self.user)[0]

    def test_signup_view_get(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    def test_signup_view_post_valid(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password1": "strongpass123",
            "password2": "strongpass123",
        }
        response = self.client.post(reverse("accounts:signup"), data)
        self.assertRedirects(response, reverse("accounts:login"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view_get(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_login_view_post_valid(self):
        response = self.client.post(
            reverse("accounts:login"),
            {"username_or_email": "testuser", "password": "12345"},
        )
        self.assertRedirects(response, reverse("accounts:profile"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_invalid(self):
        response = self.client.post(
            reverse("accounts:login"),
            {"username_or_email": "wrong", "password": "wrong"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "نام کاربری/ایمیل یا رمز عبور اشتباه است.")

    def test_email_login_view_get(self):
        response = self.client.get(reverse("accounts:email_login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/email_login.html")

    def test_email_login_view_post_valid(self):
        response = self.client.post(
            reverse("accounts:email_login"),
            {"email": "test@example.com", "password": "12345"},
        )
        self.assertRedirects(response, reverse("accounts:profile"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("core:home"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_profile_view_get_authenticated(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("accounts:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")
        self.assertEqual(response.context["profile"], self.profile)

    def test_profile_view_post_update(self):
        self.client.login(username="testuser", password="12345")
        data = {
            "role": "seller",
            "phone": "09123456789",
        }
        response = self.client.post(reverse("accounts:profile"), data)
        self.assertRedirects(response, reverse("accounts:profile"))
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.role, "seller")
        self.assertEqual(self.profile.phone, "09123456789")
