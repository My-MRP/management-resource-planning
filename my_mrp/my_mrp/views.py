"""Define the My MRP home view."""

from django.views.generic.base import TemplateView
from .models import Quote


class HomeView(TemplateView):
    """Make the HomeView class."""

    pass
 
    # template_name = 'generic/home.html'
    # context_object_name = 'quotes'

    # def get_queryset(self, **kwargs):
    #     """Get the context to display."""
    #     username = self.request.user.get_username()
    #     quotes = Quote.objects.filter(user__username=username)

    #     return quotes

    # def get_context_data(self, **kwargs):
    #     """Filter the context for display."""
    #     context = super().get_context_data(**kwargs)
    #     quotes = context['quotes'][0]

    #     context.update({
    #         'quotes': quotes,
    #     })

    #     return context
