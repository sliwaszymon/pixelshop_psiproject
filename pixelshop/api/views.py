from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from pixelshop.models import User

# main api view
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'User -> List': '/api-user/user-list/',
        'User -> DetailView': '/api-user/user-detail/<str:pk>/',
        'User -> Create': '/api-user/user-create/',
        'User -> Update': '/api-user/user-update/<str:pk>/',
        'User -> Delete': '/api-user/user-delete/<str:pk>/',
        'PixelArt -> List': '/api-pixelart/pixelart-list/',
        'PixelArt -> DetailView': '/api-pixelart/pixelart-detail/<str:pk>/',
        'PixelArt -> Create': '/api-pixelart/pixelart-create/',
        'PixelArt -> Update': '/api-pixelart/pixelart-update/<str:pk>/',
        'PixelArt -> Delete': '/api-pixelart/pixelart-delete/<str:pk>/',
        'Order -> List': '/api-order/order-list/',
        'Order -> DetailView': '/api-order/order-detail/<str:pk>/',
        'Order -> Create': '/api-order/order-create/',
        'Order -> Update': '/api-order/order-update/<str:pk>/',
        'Order -> Delete': '/api-order/order-delete/<str:pk>/'
    }
    return Response(api_urls)

# user list api view
@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)