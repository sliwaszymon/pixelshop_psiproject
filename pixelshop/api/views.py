"""Rest API Views file."""

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.reverse import reverse

from .serializers import UserSerializer, OrderSerializer, PixelArtSerializer
from pixelshop.models import User, Order, PixelArt
from .filters import PixelArtFilter


class ApiIndexView(GenericAPIView):
    name = 'root-api'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(f"api:{UserListView.name}", request=request),
            'pixelarts': reverse(f"api:{PixelArtListView.name}", request=request),
            'orders': reverse(f"api:{OrderListView.name}", request=request)
        })


class UserListView(generics.ListCreateAPIView):
    """UserListView class. You can see all users and also you can create new one."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    filter_fields = ['username', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering_fields = ['date_joined', 'last_login']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserSerializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = UserSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    name = 'user-detail'


class PixelArtListView(generics.ListCreateAPIView, PixelArtFilter):
    """PixelArtListView class. You can see all pixelarts and also you can create new one."""
    queryset = PixelArt.objects.filter()
    serializer_class = PixelArtSerializer
    name = 'pixelart-list'
    filter_class = PixelArtFilter
    search_fields = ['title', 'certificate_id', 'desc']
    ordering_fields = ['price']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PixelArtSerializer(page, context={'request': request},  many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PixelArtSerializer(queryset, context={'request': request},  many=True)
        return Response(serializer.data)


class PixelArtDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PixelArt.objects.filter()
    serializer_class = PixelArtSerializer
    name = 'pixelart-detail'


class OrderListView(generics.ListCreateAPIView):
    """OrdertListView class. You can see all orders and also you can create new one."""
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    name = 'order-list'
    filter_fields = ['status']
    search_fields = ['user', 'pixelart']
    ordering_fields = ['date_purchased']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = OrderSerializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = OrderSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    name = 'order-detail'