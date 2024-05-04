from .models import Message

class MessagingSystemTestCase(TestCase):
    def test_message_sending(self):
        # Test sending a message
        sender = User.objects.create_user(username='sender', password='12345')
        receiver = User.objects.create_user(username='receiver', password='12345')
        self.client.login(username='sender', password='12345')
        response = self.client.post(reverse('send_message'), {'receiver_id': receiver.id, 'content': 'Hello!'})
        message = Message.objects.get(sender_id=sender.id, receiver_id=receiver.id)
        self.assertEqual(message.content, 'Hello!')
        self.assertEqual(response.status_code, 200)
