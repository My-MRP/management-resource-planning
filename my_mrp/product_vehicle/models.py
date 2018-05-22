from django.db import models

# ADMIN: Create Vehicle
class Vehicle(models.Model):
    model_name =        models.CharField(max_length=100, null=False)
    engine =            models.ManyToManyField('Engine', related_name='vehicles', null=False)
    exterior_color =    models.ManyToManyField('ExteriorColor', related_name='vehicles', null=False)
    wheels =            models.ManyToManyField('Wheel', related_name='vehicles', null=False)
    interior_package =  models.ManyToManyField('InteriorColor', related_name='vehicles', null=False)
    audio_system =      models.ManyToManyField('AudioSound', related_name='vehicles', null=False)


class Engine(models.Model):
    """Allows Admin to create new engine type."""
    name =           models.CharField(max_length=100)
    description =    models.CharField(max_length=100)
    cost =           models.IntegerField()


class ExteriorColor(models.Model):
    """Allows Admin to add new exterior color."""
    name =           models.CharField(max_length=50)
    cost =           models.IntegerField()


class InteriorColor(models.Model):
    """Allows Admin to create add new interior color."""
    name =           models.CharField(max_length=50)
    cost =           models.IntegerField()


class Wheel(models.Model):
    """Allows Admin to create add new wheel to options."""
    name =           models.CharField(max_length=50)
    description =    models.CharField(max_length=100)
    cost =           models.IntegerField()


class AudioSound(models.Model):
    """Allows Admin to create add new audio system."""
    name =           models.CharField(max_length=50)
    description =    models.CharField(max_length=100)
    cost =           models.IntegerField()
