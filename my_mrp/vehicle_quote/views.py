"""Define the views for the quotes."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import VehicleQuote
from product_vehicle.models import Vehicle
from .forms import VehicleQuoteForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class QuoteListView(LoginRequiredMixin, ListView):
    """Define the library view class."""

    template_name = 'quote_list.html'
    context_object_name = 'quotes'

    login_url = reverse_lazy('auth_login')

    def get_queryset(self):
        """Get the context to display."""
        username = self.request.user.get_username()
        quotes = VehicleQuote.objects.filter(user__username=username)

        return quotes

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)
        quotes = context['quotes']

        context.update({
            'quotes': quotes,
        })

        return context


class SelectModelName(LoginRequiredMixin, ListView):
    """Get the model names to create a quote."""

    template_name = 'select_model.html'
    context_object_name = 'model_names'

    login_url = reverse_lazy('auth_login')

    def get_queryset(self):
        """Get the context to display."""
        model_names = Vehicle.objects.all()

        return model_names

    def get_context_data(self, **kwargs):
        """Filter the context for display."""
        context = super().get_context_data(**kwargs)
        model_names = context['model_names']
        context.update({
            'model_names': model_names,
        })

        return context


class AddQuoteView(LoginRequiredMixin, CreateView):
    """Define the add quote view class."""

    model = VehicleQuote
    form_class = VehicleQuoteForm
    success_url = reverse_lazy('quote_list')
    login_url = reverse_lazy('auth_login')

    def get_form_kwargs(self):
        """Get the username."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'id': self.kwargs['id']})
        return kwargs

    def form_valid(self, form):
        """Add the user to the quote."""
        form.instance.user = self.request.user
        form.instance.model_name = Vehicle.objects.filter(id=self.kwargs['id']).first()
        return super().form_valid(form)


class QuoteDetailView(LoginRequiredMixin, DetailView):
    """Define the quote view class."""

    template_name = 'quote_detail.html'
    context_object_name = 'quote'
    login_url = reverse_lazy('auth_login')

    def get_object(self):
        """Create quote price if doesn't exist."""
        car = VehicleQuote.objects.filter(id=self.kwargs['id']).first()
        if not car.quoted_price and not car.manufacture_cost:
            car.manufacture_cost = (
                car.engine.first().cost + car.exterior_color.first().cost +
                car.interior_package.first().cost + car.wheels.first().cost +
                car.audio_system.first().cost + car.model_name.body_cost
            )
            car.quoted_price = (
                car.manufacture_cost * car.model_name.markup_multiplier
            )
            car.save()
        car.e = car.engine.first().name
        car.c = car.exterior_color.first().name
        car.i = car.interior_package.first().name
        car.w = car.wheels.first().name
        car.a = car.audio_system.first().name
        return car

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context
