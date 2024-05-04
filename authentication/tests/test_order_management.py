from .models import Order

class OrderManagementTestCase(TestCase):
    def test_order_creation(self):
        # Test creating an order
        response = self.client.post(reverse('create_order'), {'user_id': 1, 'total': 50.00})
        order = Order.objects.first()
        self.assertEqual(order.total, 50.00)
        self.assertEqual(response.status_code, 200)

    def test_order_cancellation(self):
        # Test cancelling an order
        self.client.post(reverse('create_order'), {'user_id': 1, 'total': 50.00})
        response = self.client.post(reverse('cancel_order'), {'order_id': 1})
        order = Order.objects.get(id=1)
        self.assertEqual(order.status, 'Cancelled')
        self.assertEqual(response.status_code, 200)
