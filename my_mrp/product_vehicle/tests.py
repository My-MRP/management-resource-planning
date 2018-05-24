from django.test import TestCase
from models import Vehicle
from random import randint
import factory


class Engine(factory.django.DjangoModelFactory):
    """Creates Dummy Engine instance for testing."""

    class Meta:
        model = Engine

    name = factory.Faker('name')
    description = 'v8 full injection tailored for an aggressive driver.'
    cost = random.randint(7000, 50000)



class ExteriorColor(factory.django.DjangoModelFactory):
    """Creates Dummy ExteriorColor instance for testing."""
    class Meta:
        model = ExteriorColor

    name = factory.Faker('name')
    cost = random.randint(7000, 50000)


class InteriorColor(factory.django.DjangoModelFactory):
    """Creates Dummy InteriorColor instance for testing."""
    class Meta:
        model = InteriorColor

    name = factory.Faker('name')
    cost = random.randint(7000, 50000)


class Wheel(factory.django.DjangoModelFactory):
    """Creates Dummy Wheel instance for testing."""
    class Meta:
        model = Wheel

    name = factory.Faker('name')
    description = 'Chrome with a silver finish.'
    cost = random.randint(7000, 50000)


class AudioSound(factory.django.DjangoModelFactory):
    """Creates Dummy AudioSound instance for testing."""
    class Meta:
        model = AudioSound

    name = factory.Faker('name')
    description = 'Clear sound.'
    cost = random.randint(7000, 50000)


# FAKER GENERATED INSTANCE
class VehicleModelFactory(factory.django.DjangoModelFactory):
    pass

# STATIC CREATED INSTANCE
class StaticVehicleModel(factory.django.DjangoModelFactory):
    """
    Creates Vehicle Object using Admin preiveldges. POSTS to DATABASE for quoting
    tool application.
    """
    class Meta:
        model = Vehicle

    mustang = Vehicle(
        model_name="mustang",
        engine=Engine("v8", "clean cut", 19000),
        exterior_color=ExteriorColor("white", 2500),
        wheels=Wheel("chrome", "shiny", 4000),
        interior_package=InteriorColor("default", 2000),
        audio_system=AudioSound("radio", "simple system", 1000)
    )
    mustang.save()
