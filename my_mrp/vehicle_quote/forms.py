from django.db import models
from django.forms import ModelForm
from django import forms
from product_vehicle.models import Vehicle
from .models import VehicleQuote
from django.contrib.auth.mixins import LoginRequiredMixin


class VehicleQuoteForm(ModelForm, forms.Form):
    """Define the VehicleQuote form."""

    class Meta:
        """Meta data for VehicleQuote form."""

        model = VehicleQuote
        fields = ['model_name', 'engine', 'exterior_color', 'wheels',
                  'interior_package', 'audio_system']

    def __init__(self, *args, **kwargs):
        """Init for VehicleQuote form."""
        username = kwargs.pop('username')
        # import pdb; pdb.set_trace()
        model_name_choices = Vehicle.objects.all()

        super().__init__(*args, **kwargs)
        self.fields['model_name'] = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=model_name_choices)
        # self.fields['Engine'].queryset = Vehicle.objects.filter(model.'engine')
        # self.fields['Interior'].queryset = Vehicle.objects.filter(model.'interior')
        # self.fields['Audio'].queryset = Vehicle.objects.filter(model.'audio')
        # self.fields['Exterior'].queryset = Vehicle.objects.filter(model.'exterior')
        # self.fields['Wheels'].queryset = Vehicle.objects.filter(model.'wheels')
        # self.fields['Accessories'].queryset = Vehicle.objects.filter(model.'accessories')
        # self.fields['Date Created'].queryset = Vehicle.objects.filter(model.'accessories')
        # self.fields['Expiration Date'].queryset = Vehicle.objects.filter(model.'accessories')




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
