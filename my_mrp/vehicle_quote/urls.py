"""Define the paths for the vehicle quote views."""

from django.urls import path
from .views import QuoteListView, AddQuoteView, QuoteDetailView, QuoteEditView, SelectModelName

urlpatterns = [
    path('quotes/', QuoteListView.as_view(), name='quote_list'),
    path('quotes/<int:id>', QuoteDetailView.as_view(), name='quote_detail'),
    path('quotes/<int:id>/edit/', QuoteEditView.as_view(), name='quote_edit'),
    path('model_names/', SelectModelName.as_view(), name='select_model'),
    path('vehiclequote_form/', AddQuoteView.as_view(), name='vehicle_quote'),
]
