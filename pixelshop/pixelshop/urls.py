"""Pixelshop urls file."""

from django.urls import path, include
from .views import AboutusView, ContactView, ProductView, ProfileView, registerView, ShopView, ProfileUpdateView, RegulationsView, orderCompleteView

app_name = 'pixelshop'
urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<pk>/', ProductView.as_view(), name='product'),
    path('shop/ordercomplete/', orderCompleteView, name='order-complete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('aboutus/', AboutusView.as_view(), name='aboutus'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('register/', registerView, name='registration'),
    path('register/regulations/', RegulationsView.as_view(), name='regulations'),
    path('authenticate/', include('django.contrib.auth.urls'))
]
