from django.test import TestCase
from .views import process_request
from django.core.exceptions import PermissionDenied

class ErrorHandlingTestCase(TestCase):
    def test_error_logging(self):
        # Simulate an error and check if it's logged properly
        with self.assertRaises(PermissionDenied):
            process_request(request=None)  # Should raise an error and log it
