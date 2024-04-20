class SearchTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Django Book', description='A book on Django', price=40)
        Product.objects.create(name='Flask Book', description='A book on Flask', price=30)

    def test_search_product(self):
        response = self.client.get(reverse('search_products'), {'query': 'Django'})
        self.assertIn('Django Book', response.content.decode())
        self.assertNotIn('Flask Book', response.content.decode())
