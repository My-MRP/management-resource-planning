"""Define the vehicle quote form."""

from django.forms import ModelForm
from product_vehicle.models import Vehicle
from .models import VehicleQuote


class VehicleQuoteForm(ModelForm):
    """Define the VehicleQuote form."""

    class Meta:
        """Meta data for VehicleQuote form."""

        model = VehicleQuote
        fields = ['name', 'engine', 'interior_package', 'audio_system', 'exterior_color', 'wheels']

    def __init__(self, *args, **kwargs):
        """Init for VehicleQuote form."""
        model_name = Vehicle.objects.filter(id=str(kwargs.pop('id'))).first()

        super().__init__(*args, **kwargs)

        self.fields['engine'].queryset = model_name.engine.all()
        self.fields['interior_package'].queryset = model_name.interior_package.all()
        self.fields['audio_system'].queryset = model_name.audio_system.all()
        self.fields['exterior_color'].queryset = model_name.exterior_color.all()
        self.fields['wheels'].queryset = model_name.wheels.all()
