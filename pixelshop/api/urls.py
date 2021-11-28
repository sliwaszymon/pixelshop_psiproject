"""Api urls file."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('user/user-list/', views.userList, name='user-list'),
    path('user/user-detail/<str:pk>/', views.userDetail, name='user-detail'),

]
