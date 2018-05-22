from django.urls import path
from .views import (
    AddVehicleView,
    AddEngineView,
    AddAudioView,
    AddExteriorColorView,
    AddInteriorColorView,
    AddWheelView,
)


urlpatterns = [
    path('vehicle/', AddVehicleView.as_view(), name='add_vehicle'),
    path('engine/', AddEngineView.as_view(), name='add_engine'),
    path('exterior/', AddExteriorColorView.as_view(), name='add_exterior_color'),
    path('interior/', AddInteriorColorView.as_view(), name='add_interior_color'),
    path('audio/', AddAudioView.as_view(), name='add_audio'),
    path('wheel/', AddWheelView.as_view(), name='add_wheel'),
]
