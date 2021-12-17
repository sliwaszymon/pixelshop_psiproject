"""Api urls file."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiIndexView.as_view(), name=views.ApiIndexView.name),
    path('users/', views.UserListView.as_view(), name=views.UserListView.name),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name=views.UserDetailView.name),
    path('pixelarts/', views.PixelArtListView.as_view(), name=views.PixelArtListView.name),
    path('pixelarts/<int:pk>/', views.PixelArtDetailView.as_view(), name=views.PixelArtDetailView.name),
    path('orders/', views.OrderListView.as_view(), name=views.OrderListView.name),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name=views.OrderDetailView.name),
]
