from django.db import models
from django.forms import ModelForm, ModelChoiceField
from product_vehicle.models import Vehicle
from .models import VehicleQuote
from django.contrib.auth.mixins import LoginRequiredMixin


class VehicleQuoteForm(ModelForm):
    """Define the VehicleQuote form."""

    class Meta:
        """Meta data for VehicleQuote form."""

        model = VehicleQuote
        fields = ['name', 'engine', 'interior_package', 'audio_system', 'exterior_color', 'wheels']
        widgets = {
            'engine': ModelChoiceField,
            'interior_package': ModelChoiceField,
            'audio_system': ModelChoiceField,
            'exterior_color': ModelChoiceField,
            'wheels': ModelChoiceField,
        }

    def __init__(self, *args, **kwargs):
        """Init for VehicleQuote form."""
        user = kwargs.pop('username')
        model_name = Vehicle.objects.filter(id=str(kwargs.pop('id'))).first()
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
        # import pdb; pdb.set_trace()

        super().__init__(*args, **kwargs)
        
        self.fields['engine'].queryset = model_name.engine.all()
        self.fields['interior_package'].queryset = model_name.interior_package.all()
        self.fields['audio_system'].queryset = model_name.audio_system.all()
        self.fields['exterior_color'].queryset = model_name.exterior_color.all()
        self.fields['wheels'].queryset = model_name.wheels.all()




# BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
# FAVORITE_COLORS_CHOICES = (
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# )

# class SimpleForm(forms.Form):
#     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     model_name = forms.MultipleChoiceField(
#         required=true,
#         widget=forms.CheckboxSelectMultiple,
#         choices=model_name_choices,
#     )

# User.objects.all().values('username')
# >>> [{'username': u'u1'}, {'username': u'u2'}]

# >>> User.objects.all().values_list('username')
# >>> [(u'u1',), (u'u2',)]
