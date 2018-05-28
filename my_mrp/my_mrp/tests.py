from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Test user."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')

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

    def test_vehicle_route_not_logged_in(self):
        response = self.client.get('/vehicles/vehicle')
        self.assertEqual(response.status_code, 301)

    def test_component_route_not_logged_in(self):
        response = self.client.get('/component')
        self.assertEqual(response.status_code, 302)

    def test_engine_route_not_logged_in(self):
        response = self.client.get('/vehicles/engine')
        self.assertEqual(response.status_code, 301)

    def test_exterior_route_not_logged_in(self):
        response = self.client.get('/vehicles/exterior')
        self.assertEqual(response.status_code, 301)

    def test_interior_route_not_logged_in(self):
        response = self.client.get('/vehicles/interior')
        self.assertEqual(response.status_code, 301)

    def test_wheel_route_not_logged_in(self):
        response = self.client.get('/vehicles/wheel')
        self.assertEqual(response.status_code, 301)

    def test_audio_route_not_logged_in(self):
        response = self.client.get('/vehicles/audio')
        self.assertEqual(response.status_code, 301)
