"""my_mrp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, AboutUsView, ComponentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('component', ComponentView.as_view(), name='component'),
    path('accounts/', include('registration.backends.hmac.urls')),
    path('sales/', include('vehicle_quote.urls')),
    path('vehicles/', include('product_vehicle.urls')),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]
