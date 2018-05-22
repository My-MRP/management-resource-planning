from django.forms import ModelForm
from .product_vehicle.models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin


class VehicleQuote(ModelForm):
    """Define the VehicleQuote form."""

    class Meta:
        """Meta data for VehiucleQuote form."""

        model = Vehicle
        fields = ['Name', 'Model Name', 'Engine', 'Interior', 'Audio', 'Exterior', 'Wheels', 'Accessories', 'Date Created', 'Expiration Date']

    def __init__(self, *args, **kwargs):
        """Init for VehiucleQuote form."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['Name'].queryset = forms.CharField(max_length=180, null=False)
        self.fields['Model'].queryset = Vehicle.objects.filter('model_name')
        self.fields['Engine'].queryset = Vehicle.objects.filter(model.'engine')
        self.fields['Interior'].queryset = Vehicle.objects.filter(model.'interior')
        self.fields['Audio'].queryset = Vehicle.objects.filter(model.'audio')
        self.fields['Exterior'].queryset = Vehicle.objects.filter(model.'exterior')
        self.fields['Wheels'].queryset = Vehicle.objects.filter(model.'wheels')
        self.fields['Accessories'].queryset = Vehicle.objects.filter(model.'accessories')
        self.fields['Date Created'].queryset = Vehicle.objects.filter(model.'accessories')
        self.fields['Expiration Date'].queryset = Vehicle.objects.filter(model.'accessories')

