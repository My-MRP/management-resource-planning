"""Define the paths for the vehicle quote views."""

from django.urls import path
from .views import (
    QuoteListView,
    AddQuoteView,
    QuoteDetailView,
    SelectModelName,
)

urlpatterns = [
    path('quotes/', QuoteListView.as_view(), name='quote_list'),
    path('quotes/<int:id>', QuoteDetailView.as_view(), name='quote_detail'),
    path('model_names/', SelectModelName.as_view(), name='select_model'),
    path('vehiclequote_form/<int:id>', AddQuoteView.as_view(), name='vehicle_quote'),
]
