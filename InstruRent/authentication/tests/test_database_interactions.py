from django.test import TestCase
from django.db import IntegrityError
from .models import UserProfile

class DatabaseInteractionTestCase(TestCase):
    def test_create_user_profile(self):
        # Test successful creation
        profile = UserProfile.objects.create(user_id=1, username='testuser', email='user@example.com')
        self.assertEqual(UserProfile.objects.count(), 1)

    def test_duplicate_username(self):
        # Test that duplicate usernames are not allowed
        UserProfile.objects.create(user_id=1, username='testuser', email='user@example.com')
        with self.assertRaises(IntegrityError):
            UserProfile.objects.create(user_id=2, username='testuser', email='another@example.com')
