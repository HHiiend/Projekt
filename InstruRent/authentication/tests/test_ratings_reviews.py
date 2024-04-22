from .models import Review, Product

class RatingsAndReviewsTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product')

    def test_create_review(self):
        # Test creating a review
        self.client.post(reverse('add_review'), {'product_id': self.product.id, 'rating': 5, 'comment': 'Great!'})
        review = Review.objects.get(product_id=self.product.id)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great!')
