from django.forms import ModelForm
from .product_vehicle.models import Vehicle


class VehicleQuote(ModelForm):
    """Define the VehicleQuote form."""

    class Meta:
        """Meta data for album form."""

        model = Vehicle
        fields = ['name', 'model', 'engine', 'interior', 'audio', 'exterior', 'wheels', 'accessories']

    def __init__(self, *args, **kwargs):
        """Init for album form."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = forms.CharField(max_length=180, null=False)
        self.fields['model'].queryset = Vehicle.objects.filter('model_name')
        self.fields['engine'].queryset = Vehicle.objects.filter(model.'engine')
        self.fields['interior'].queryset = Vehicle.objects.filter(model.'interior')
        self.fields['audio'].queryset = Vehicle.objects.filter(model.'audio')
        self.fields['exterior'].queryset = Vehicle.objects.filter(model.'exterior')
        self.fields['wheels'].queryset = Vehicle.objects.filter(model.'wheels')
        self.fields['accessories'].queryset = Vehicle.objects.filter(model.'accessories')

