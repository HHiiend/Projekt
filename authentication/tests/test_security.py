from django.test import TestCase
from django.urls import reverse
from .models import User
from django.middleware.csrf import CsrfViewMiddleware

class SecurityTestCase(TestCase):
    def test_csrf_protection(self):
        # Ensure CSRF protection is enforced
        response = self.client.post(reverse('update_profile'), {})
        # Check CSRF failure response (without proper CSRF token)
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_attack(self):
        # Simulate an SQL Injection attack and ensure it fails
        User.objects.create(username='user', password='safe_password')
        response = self.client.post(reverse('login'), {'username': 'user', 'password': "' OR '1'='1"})
        self.assertNotEqual(response.status_code, 200)
