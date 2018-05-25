from django.test import TestCase, Client
from django.urls import reverse_lazy


class BasicViewTests(TestCase):
    """Test view routing."""

    def setup(self):
        """Create client."""
        self.client = Client()

    def test_home_route(self):
        """Route to home."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_route2(self):
        """Display home."""
        response = self.client.get('/')
        self.assertIn('MRP', response.content.decode('utf-8'))
