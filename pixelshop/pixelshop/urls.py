"""Pixelshop urls file."""

from django.urls import path, include
from .views import AboutusView, ContactView, ProductView, ProfileView, RegisterView, ShopView, ProfileUpdateView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<pk>', ProductView.as_view(), name='prodct'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('aboutus/', AboutusView.as_view(), name='aboutus'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<pk>/update', ProfileUpdateView.as_view(), name='profile-update'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('authenticate/', include('django.contrib.auth.urls'))
]
