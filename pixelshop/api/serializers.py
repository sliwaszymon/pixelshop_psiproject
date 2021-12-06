"""Serializers file."""

from rest_framework import serializers
from pixelshop.models import User, Order, PixelArt


class UserSerializer(serializers.ModelSerializer):
    """User serializer class."""

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "First name must contain only letters."
            ) 
        elif value != value.capitalize():
            raise serializers.ValidationError(
                "First name must start with "
            )
    class Meta:
        model = User
        fields = '__all__'


class PixelArtSerializer(serializers.ModelSerializer):
    """PixelArt serializer class."""

    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=200)
    date_purchased = serializers.DateTimeField()

    class Meta:
        model = PixelArt
        fields = '__all__'

    def validate_title(self, value):
        pass

class OrderSerializer(serializers.ModelSerializer):
    """Order serializer class."""

    date_purchased = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = '__all__'