"""Serializers file."""

from rest_framework import serializers
from pixelshop.models import User, Order, PixelArt


class UserSerializer(serializers.ModelSerializer):
    """User serializer class."""

    class Meta:
        model = User
        fields = '__all__'


class PixelArtSerializer(serializers.Serializer):
    """PixelArt serializer class."""

    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=200)
    date_purchased = serializers.DateTimeField()

    def validate_title(self, value):
        pass

class OrderSerializer(serializers.Serializer):
    """Order serializer class."""

    pass