from django.contrib import admin
from .models import Vehicle, Engine, ExteriorColor, InteriorColor, Wheel, AudioSound

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Engine)
admin.site.register(ExteriorColor)
admin.site.register(InteriorColor)
admin.site.register(Wheel)
admin.site.register(AudioSound)
