"""Define the classes to add new vehicles and components."""

from django.shortcuts import render
from django.views.generic import CreateView
from product_vehicle.models import Vehicle, Engine, ExteriorColor, InteriorColor, Wheel, AudioSound
from product_vehicle.forms import AddVehicleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AddVehicleView(LoginRequiredMixin, CreateView):
    """Add new vehicle."""

    template_name = 'vehicle/add_vehicle.html'
    model = Vehicle
    form_class = AddVehicleForm
    success = reverse_lazy('quote_list')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddEngineView(LoginRequiredMixin, CreateView):
    """Add new engine."""

    template_name = 'components/add_engine.html'
    model = Engine
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy('add_vehicle')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddExteriorColorView(LoginRequiredMixin, CreateView):
    """Add new exterior color."""

    template_name = 'components/add_exterior.html'
    model = ExteriorColor
    fields = ['name', 'cost']
    success_url = reverse_lazy('add_vehicle')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddWheelView(LoginRequiredMixin, CreateView):
    """Add new wheel."""

    template_name = 'components/add_wheel.html'
    model = Wheel
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy('add_vehicle')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddInteriorColorView(LoginRequiredMixin, CreateView):
    """Add new interior color."""

    template_name = 'components/add_interior.html'
    model = InteriorColor
    fields = ['name', 'cost']
    success_url = reverse_lazy('add_vehicle')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddAudioView(LoginRequiredMixin, CreateView):
    """Add new audio system."""

    template_name = 'components/add_audio.html'
    model = AudioSound
    fields = ['name', 'description', 'cost']
    success_url = reverse_lazy('add_vehicle')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)
