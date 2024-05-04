from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class APITestCase(TestCase):
    def test_user_authentication_api(self):
        # Test API endpoint for user authentication
        response = self.client.post(reverse('api_login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.json())
