"""Pixelshop urls file."""

from django.urls import path
from .views import HomePageView, RegisterView

urlpatterns = [
    path('shop/', HomePageView.as_view(), name='shop'),
    path('contact/', HomePageView.as_view(), name='contact'),
    path('aboutus/', HomePageView.as_view(), name='aboutus'),
    path('profile/', HomePageView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='registration')
]
