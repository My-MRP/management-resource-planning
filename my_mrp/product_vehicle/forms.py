"""Define the add vehicle form."""

from .models import Vehicle, Engine, ExteriorColor, InteriorColor, Wheel, AudioSound
from django.forms import ModelForm


class AddVehicleForm(ModelForm):
    """Make the form to add a vehicle from the Vehicle model."""

    class Meta:
        """Meta."""

        model = Vehicle
        fields = ['model_name', 'engine', 'exterior_color', 'wheels', 'interior_package', 'audio_system', 'body_cost', 'markup_multiplier']

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.fields['engine'].queryset = Engine.objects.all()
        self.fields['exterior_color'].queryset = ExteriorColor.objects.all()
        self.fields['interior_package'].queryset = InteriorColor.objects.all()
        self.fields['wheels'].queryset = Wheel.objects.all()
        self.fields['audio_system'].queryset = AudioSound.objects.all()
