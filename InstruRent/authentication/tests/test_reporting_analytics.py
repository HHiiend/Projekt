from .models import Order
from django.contrib.auth.models import User

class ReportingTestCase(TestCase):
    def test_order_report(self):
        # Test generating a report of orders
        User.objects.create_user('user1', password='12345')
        Order.objects.create(user_id=1, total=100.00, status='Completed')
        response = self.client.get(reverse('order_report'), {'user_id': 1})
        self.assertIn('Total orders: 1', response.content.decode())
        self.assertIn('Total amount: 100.00', response.content.decode())
        self.assertEqual(response.status_code, 200)
