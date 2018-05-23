"""Make the model for a vehicle quote."""

from django.db import models
from django.contrib.auth.models import User
from product_vehicle.models import Vehicle, Engine, ExteriorColor, InteriorColor, Wheel, AudioSound


class VehicleQuote(models.Model):
    """This is the Quote model."""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='vehicle_quotes')
    name = models.CharField(max_length=100, null=False)
    model_name = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING, related_name='vehicle_quotes', null=False)
    engine = models.ManyToManyField(Engine, related_name='vehicle_quotes')
    exterior_color = models.ManyToManyField(ExteriorColor, related_name='vehicle_quotes')
    wheels = models.ManyToManyField(Wheel, related_name='vehicle_quotes')
    interior_package = models.ManyToManyField(InteriorColor, related_name='vehicle_quotes')
    audio_system = models.ManyToManyField(AudioSound, related_name='vehicle_quotes')
    cost = models.IntegerField()
    list_price = 
    date_created = models.DateField(auto_now_add=True, null=False)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        """Show a string representation of the quote name."""
        return '{}'.format(self.name)
