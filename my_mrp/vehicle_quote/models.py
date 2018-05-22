"""Make the model for a vehicle quote."""

from django.db import models
from django.contrib.auth.models import User


class VehicleQuote(models.Model):
    """This is the Quote model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle_quotes')
    name = models.CharField(max_length=100, null=False)
    model_name = models.CharField(max_length=100, null=False)
    engine = models.CharField(max_length=100, null=False)
    exterior_color = models.CharField(max_length=100, null=False)
    wheels = models.CharField(max_length=100, null=False)
    interior_package = models.CharField(max_length=100, null=False)
    audio_system = models.CharField(max_length=100, null=False)
    date_quoted = models.DateField(auto_now_add=True, null=False)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        """Show a string representation of the quote name."""
        return '{}'.format(self.name)
