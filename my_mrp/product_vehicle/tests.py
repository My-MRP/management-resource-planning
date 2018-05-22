from django.test import TestCase
import factory


class VehicleModelFactory(factory.django.DjangoModelFactory):
    """
    Creates Vehicle Object using Admin preiveldges. POSTS to DATABASE for quoting
    tool application.
    """
    mustang = Vehicle(
                model_name="mustang", engine=Engine("v8", "clean cut", 19000),
                exterior_color=ExteriorColor("white", 2500),
                wheels=Wheel("chrome", "shiny", 4000),
                interior_package=InteriorColor("default", 2000),
                audio_system=AudioSound("radio", "simple system", 1000)
            )
    mustang.save()

class Engine(factory.django.DjangoModelFactory):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

class ExteriorColor(factory.django.DjangoModelFactory):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg


class InteriorColor(factory.django.DjangoModelFactory):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

class Wheel(factory.django.DjangoModelFactory):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg


class AudioSound(factory.django.DjangoModelFactory):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
