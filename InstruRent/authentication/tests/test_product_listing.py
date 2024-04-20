from .models import Product

class ProductListingTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Django Book', description='Learn Django', price=39.99)

    def test_product_list(self):
        response = self.client.get(reverse('product_list'))
        self.assertIn('Django Book', response.content.decode())
