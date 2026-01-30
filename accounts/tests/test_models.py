from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Profile

User = get_user_model()


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="12345",
        )
        self.profile = Profile.objects.get_or_create(user=self.user)[0]

    def test_profile_str(self):
        expected = f"{self.user.username} (خریدار)"
        self.assertEqual(str(self.profile), expected)

    def test_profile_role_choices(self):
        self.assertEqual(self.profile.role, "buyer")
        self.profile.role = "seller"
        self.profile.save()
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.role, "seller")

    def test_profile_manager_sellers(self):
        seller_user = User.objects.create_user(
            username="seller",
            email="seller@example.com",
            password="12345",
        )
        Profile.objects.create(user=seller_user, role="seller")

        buyers = Profile.objects.buyers()
        sellers = Profile.objects.sellers()

        self.assertEqual(buyers.count(), 1)
        self.assertEqual(sellers.count(), 1)
        self.assertIn(self.profile, buyers)
        self.assertIn(seller_user.profile, sellers)
