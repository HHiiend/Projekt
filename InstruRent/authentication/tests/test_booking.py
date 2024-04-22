from .models import Booking

class BookingTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Django Course', price=100)
        self.user = User.objects.create_user(username='testuser', password='12345')
        Booking.objects.create(product=self.product, user=self.user, status='confirmed')

    def test_booking_status(self):
        booking = Booking.objects.get(user=self.user)
        self.assertEqual(booking.status, 'confirmed')
