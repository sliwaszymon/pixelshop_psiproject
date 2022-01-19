"""Pixelshop urls file."""

# Django
from django.urls import include
from django.urls import path

# Local
from .views import AboutusView
from .views import OrderCompleteView
from .views import ProductView
from .views import ProfileUpdateView
from .views import ProfileView
from .views import RegisterView
from .views import RegulationsView
from .views import ShopView

app_name = 'pixelshop'
urlpatterns = [
    path(
        'shop/',
        ShopView.as_view(),
        name='shop',
        ),
    path(
        'shop/<pk>/',
        ProductView.as_view(),
        name='product',
        ),
    path(
        'shop/ordercomplete/',
        OrderCompleteView,
        name='order-complete',
        ),
    path(
        'aboutus/',
        AboutusView.as_view(),
        name='aboutus',
        ),
    path(
        'profile/<pk>/',
        ProfileView.as_view(),
        name='profile',
        ),
    path(
        'profile/update/<pk>/',
        ProfileUpdateView.as_view(),
        name='profile-update',
        ),
    path(
        'register/',
        RegisterView,
        name='registration',
        ),
    path(
        'register/regulations/',
        RegulationsView.as_view(),
        name='regulations',
        ),
    path(
        'authenticate/',
        include(
            'django.contrib.auth.urls',
            ),
        ),
]
