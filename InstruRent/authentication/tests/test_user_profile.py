class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', email='user@example.com')

    def test_profile_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('edit_profile'), {'email': 'newemail@example.com'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'newemail@example.com')
