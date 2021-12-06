"""Api urls file."""

from django.urls import path
from . import views

urlpatterns = [
    # main path to api
    path('', views.apiOverview, name='api-overview'),
    path('users/', views.UserListView.as_view()),
    path('pixelarts/', views.PixelArtListView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    # FUNCTION VIEWS PATHS
    # # user paths
    # path('user/user-list/', views.userList, name='user-list'),
    # path('user/user-detail/<str:pk>/', views.userDetail, name='user-detail'),
    # path('user/user-create/', views.userCreate, name='user-create'),
    # path('user/user-update/<str:pk>/', views.userUpdate, name='user-update'),
    # path('user/user-delete/<str:pk>/', views.userDelete, name='user-delete'),
    # # pixelart paths
    # path('pixelart/pixelart-list/', views.pixelartList, name='pixelart-list'),
    # path('pixelart/pixelart-detail/<str:pk>/', views.pixelartDetail, name='pixelart-detail'),
    # path('pixelart/pixelart-create/', views.pixelartCreate, name='pixelart-create'),
    # path('pixelart/pixelart-update/<str:pk>/', views.pixelartUpdate, name='pixelart-update'),
    # path('pixelart/pixelart-delete/<str:pk>/', views.pixelartDelete, name='pixelart-delete'),
    # # order paths
    # path('order/user-list/', views.orderList, name='order-list'),
    # path('order/user-detail/<str:pk>/', views.orderDetail, name='order-detail'),
    # path('order/user-create/', views.orderCreate, name='order-create'),
    # path('order/user-update/<str:pk>/', views.orderUpdate, name='order-update'),
    # path('order/order-delete/<str:pk>/', views.orderDelete, name='order-delete'),
]
