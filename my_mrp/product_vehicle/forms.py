from .models import Vehicle, Engine, ExteriorColor, InteriorColor, Wheel, AudioSound
from django.forms import ModelForm


class AddVehicleForm(ModelForm):
    """Add vehicle form."""

    class Meta:
        """Meta."""

        model = Vehicle
        fields = ['model_name', 'engine', 'exterior_color', 'wheels', 'interior_package', 'audio_system', 'cost']

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.fields['engine'].queryset = Engine.objects.all()
        self.fields['exterior_color'].queryset = ExteriorColor.objects.all()
        self.fields['interior_package'].queryset = InteriorColor.objects.all()
        self.fields['wheels'].queryset = Wheel.objects.all()
        self.fields['audio_system'].queryset = AudioSound.objects.all()
