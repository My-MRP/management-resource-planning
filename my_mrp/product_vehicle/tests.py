from django.test import TestCase, RequestFactory
from .models import Vehicle, Engine, ExteriorColor, InteriorColor, AudioSound, Wheel
from django.contrib.auth.models import User
from random import randint
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Test user."""

    class Meta:
        """Meta."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class EngineFactory(factory.django.DjangoModelFactory):
    """Creates Dummy Engine instance for testing."""

    class Meta:
        model = Engine

    name = factory.Faker('name')
    description = 'v8 full injection tailored for an aggressive driver.'
    cost = randint(7000, 50000)


class ExteriorFactory(factory.django.DjangoModelFactory):
    """Creates Dummy ExteriorColor instance for testing."""
    class Meta:
        model = ExteriorColor

    name = factory.Faker('name')
    cost = randint(7000, 50000)


class InteriorFactory(factory.django.DjangoModelFactory):
    """Creates Dummy InteriorColor instance for testing."""
    class Meta:
        model = InteriorColor

    name = factory.Faker('name')
    cost = randint(7000, 50000)


class WheelFactory(factory.django.DjangoModelFactory):
    """Creates Dummy Wheel instance for testing."""
    class Meta:
        model = Wheel

    name = factory.Faker('name')
    description = 'Chrome with a silver finish.'
    cost = randint(7000, 50000)


class AudioSoundFactory(factory.django.DjangoModelFactory):
    """Creates Dummy AudioSound instance for testing."""
    class Meta:
        model = AudioSound

    name = factory.Faker('name')
    description = 'Clear sound.'
    cost = randint(7000, 50000)


class VehicleModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    model_name = factory.Faker('name')
    body_cost = randint(7000, 50000)
    markup_multiplier = randint(7000, 50000)


class UnitTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCase, cls)
        cls.request = RequestFactory()
        user = UserFactory(username='test', email='test@test.com')
        user.set_password('test1234')
        user.save()
        cls.test_user = user
        engine = EngineFactory.create()
        exterior = ExteriorFactory.create()
        interior = InteriorFactory.create()
        wheel = WheelFactory.create()
        audio = AudioSoundFactory.create()
        vehicle = VehicleModelFactory.create()
        engine.save()
        exterior.save()
        interior.save()
        wheel.save()
        audio.save()
        vehicle.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down test database."""
        User.objects.all().delete()
        super(TestCase, cls)

    def test_engine(self):
        one_engine = Engine.objects.first()
        self.assertIsNotNone(one_engine)

    def test_exterior(self):
        one_exterior = ExteriorColor.objects.first()
        self.assertIsNotNone(one_exterior)

    def test_interior(self):
        one_interior = InteriorColor.objects.first()
        self.assertIsNotNone(one_interior)

    def test_wheel(self):
        one_wheel = Wheel.objects.first()
        self.assertIsNotNone(one_wheel)

    def test_audio(self):
        one_audio = AudioSound.objects.first()
        self.assertIsNotNone(one_audio)

    def test_vehicle(self):
        one_vehicle = Vehicle.objects.first()
        self.assertIsNotNone(one_vehicle)
