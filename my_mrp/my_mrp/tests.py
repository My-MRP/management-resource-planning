from django.test import TestCase, Client


class ViewTests(TestCase):
    """Test View routing."""

    def setUp(self):
        """Create client."""
        self.client() = Client()

    def test_home_route_status_code(self):
        """Route home."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_route_template(self):
        response = self.client.get('/')
        self.assertIn('Welcome', response.content.decode('utf-8'))

    
