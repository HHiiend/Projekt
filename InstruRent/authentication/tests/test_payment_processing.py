from django.test import TestCase
from .models import Payment, Order
from django.urls import reverse

class PaymentProcessingTestCase(TestCase):
    def setUp(self):
        # Simulate an order creation
        Order.objects.create(user_id=1, total=100.00)

    def test_payment_creation(self):
        # Test that a payment can be processed
        response = self.client.post(reverse('process_payment'), {'order_id': 1, 'amount': 100.00})
        self.assertEqual(response.status_code, 200)
        payment = Payment.objects.get(order_id=1)
        self.assertEqual(payment.amount, 100.00)

    def test_payment_status(self):
        # Test payment status update
        self.client.post(reverse('process_payment'), {'order_id': 1, 'amount': 100.00})
        response = self.client.post(reverse('update_payment_status'), {'order_id': 1, 'status': 'Completed'})
        payment = Payment.objects.get(order_id=1)
        self.assertEqual(payment.status, 'Completed')
