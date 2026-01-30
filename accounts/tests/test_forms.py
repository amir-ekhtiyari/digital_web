from django.test import TestCase

from accounts.forms import SignUpForm, ProfileUpdateForm


class SignUpFormTest(TestCase):
    def test_signup_form_valid(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password1": "strongpass123",
            "password2": "strongpass123",
        }
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())

    def test_signup_form_password_mismatch(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password1": "strongpass123",
            "password2": "wrongpass",
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_signup_form_duplicate_email(self):
        # اول یک کاربر با ایمیل خاص می‌سازیم
        user = SignUpForm(
            data={
                "username": "existing",
                "email": "existing@example.com",
                "first_name": "Existing",
                "last_name": "User",
                "password1": "12345",
                "password2": "12345",
            }
        )
        user.save()

        # حالا همان ایمیل رو دوباره می‌زنیم
        data = {
            "username": "another",
            "email": "existing@example.com",
            "first_name": "Another",
            "last_name": "User",
            "password1": "12345",
            "password2": "12345",
        }
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class ProfileUpdateFormTest(TestCase):
    def setUp(self):
        self.user = SignUpForm(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "12345",
                "password2": "12345",
            }
        )
        self.user.save()
        self.profile = self.user.profile

    def test_profile_update_form_valid(self):
        data = {
            "role": "seller",
            "phone": "09123456789",
        }
        form = ProfileUpdateForm(data=data, instance=self.profile)
        self.assertTrue(form.is_valid())
        profile = form.save()
        self.assertEqual(profile.role, "seller")
        self.assertEqual(profile.phone, "09123456789")
