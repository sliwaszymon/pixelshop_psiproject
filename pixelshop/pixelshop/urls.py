"""Pixelshop urls file."""

from django.urls import path, include
from .views import AboutusView, ContactView, HomePageView, ProfileView, RegisterView, ShopView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    
    path('contact/', ContactView.as_view(), name='contact'),
    path('aboutus/', AboutusView.as_view(), name='aboutus'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('authenticate/', include('django.contrib.auth.urls'))
]
