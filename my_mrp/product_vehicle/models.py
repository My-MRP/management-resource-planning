"""Define the models for the vehicle and parts."""

from django.db import models


# ADMIN: Create Vehicle
class Vehicle(models.Model):
    """Allow Admin to create new vehicle type."""

    model_name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
    )
    engine = models.ManyToManyField(
        'Engine',
        related_name='vehicles',
    )
    exterior_color = models.ManyToManyField(
        'ExteriorColor',
        related_name='vehicles',
    )
    wheels = models.ManyToManyField(
        'Wheel',
        related_name='vehicles',
    )
    interior_package = models.ManyToManyField(
        'InteriorColor',
        related_name='vehicles',
    )
    audio_system = models.ManyToManyField(
        'AudioSound',
        related_name='vehicles',
    )
    body_cost = models.FloatField(null=False)
    markup_multiplier = models.FloatField(null=False)

    def __str__(self):
        """String."""
        return '{}'.format(self.model_name)


class Engine(models.Model):
    """Allow Admin to create new engine type."""

    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        """String."""
        return '{}'.format(self.name)


class ExteriorColor(models.Model):
    """Allow Admin to add new exterior color."""

    name = models.CharField(max_length=50, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        """String."""
        return '{}'.format(self.name)


class InteriorColor(models.Model):
    """Allow Admin to create add new interior color."""

    name = models.CharField(max_length=50, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        """String."""
        return '{}'.format(self.name)


class Wheel(models.Model):
    """Allow Admin to create add new wheel to options."""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        """String."""
        return '{}'.format(self.name)


class AudioSound(models.Model):
    """Allow Admin to create add new audio system."""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    cost = models.FloatField(null=False)

    def __str__(self):
        """String."""
        return '{}'.format(self.name)
