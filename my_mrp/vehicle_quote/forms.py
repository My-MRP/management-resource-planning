from django.forms import ModelForm
from .product_vehicle.models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin


class VehicleQuote(ModelForm):
    """Define the VehicleQuote form."""

    class Meta:
        """Meta data for VehicleQuote form."""

        model = Vehicle
        fields = ['Name', 'Model', 'Engine', 'Interior', 'Audio', 'Exterior', 'Wheels', 'Accessories', 'Date Created', 'Expiration Date']

    def __init__(self, *args, **kwargs):
        """Init for VehicleQuote form."""
        username = kwargs.pop('username')
        model_name_choices = Vehicle.objects.all().values_list('model_name')

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

model_name_choices = Vehicle.objects.all().values_list('model_name')
engine_choices = Vehicle.objects.filter(model_name=Model).values_list('engine', flat=True)



Name
Model = forms.MultipleChoiceField(choices=model_name_choices)
Engine = forms.MultipleChoiceField(choices=model_name_choices)
Interior = forms.MultipleChoiceField(choices=model_name_choices)
Audio = forms.MultipleChoiceField(choices=model_name_choices)
Exterior = forms.MultipleChoiceField(choices=model_name_choices)
Wheels = forms.MultipleChoiceField(choices=model_name_choices)
Accessories = forms.MultipleChoiceField(choices=model_name_choices)
Date Created
Expiration Date'



# BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
# FAVORITE_COLORS_CHOICES = (
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# )

# class SimpleForm(forms.Form):
#     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     favorite_colors = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_COLORS_CHOICES,
#     )

# User.objects.all().values('username')
# >>> [{'username': u'u1'}, {'username': u'u2'}]

# >>> User.objects.all().values_list('username')
# >>> [(u'u1',), (u'u2',)]