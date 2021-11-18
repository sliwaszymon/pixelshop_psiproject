"""Pixelshop urls file."""

from django.urls import path
from models import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
