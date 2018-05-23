"""Define the views for the quotes."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
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


class SelectModelName(ListView):
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
        kwargs.update({'username': self.request.user.username})
        kwargs.update({'id': self.kwargs['id']})
        return kwargs

    def form_valid(self, form):
        """Add the user to the quote."""
        form.instance.user = self.request.user
        form.instance.model_name = Vehicle.objects.filter(id=str(self.kwargs['id'])).first()
        return super().form_valid(form)


class QuoteDetailView(LoginRequiredMixin, DetailView):
    """Define the quote view class."""

    template_name = 'vehicle_quote/quote_view.html'
    model = VehicleQuote
    context_object_name = 'this_quote'
    pk_url_kwarg = 'id'
    login_url = reverse_lazy('auth_login')


class QuoteEditView(LoginRequiredMixin, UpdateView):
    """Define the quote edit view."""

    template_name = 'vehicle_quote/quote_edit.html'
    model = VehicleQuote
    form_class = VehicleQuoteForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('library')
    pk_url_kwarg = 'id'

    def get_form_kwargs(self):
        """Get the form data that is submitted by the quote to update the quote."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs
