"""Serializers file."""

from rest_framework import serializers
from pixelshop.models import User, Order, PixelArt
from pytz import UTC
from datetime import datetime as dt
from profanity_check import predict as profanity_predict


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer class."""
    url = serializers.HyperlinkedIdentityField(view_name = "user-detail")

    def validate_username(self, value):
        if profanity_predict([value])[0] > 0:
            raise serializers.ValidationError(
                "Your username contains offensive words."
            ) 
        return value

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "First name must contain only letters."
            ) 
        elif value != value.capitalize():
            raise serializers.ValidationError(
                "First name must start with big letter."
            )
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Last name must contain only letters."
            ) 
        elif value != value.capitalize():
            raise serializers.ValidationError(
                "Last name must start with big letter."
            )
        return value

    def validate_email(self, value):
        supported_hosts = [
            'hotmail.com',
            'outlook.com',
            'gmail.com'
        ]
        if value.split('@')[1] not in supported_hosts:
            raise serializers.ValidationError(
                "Your email host is not supported."
            ) 
        return value

    class Meta:
        model = User
        fields = [
            'url', 
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'is_staff', 
            'is_active', 
            'date_joined', 
            'password', 
            'last_login', 
            'is_active'
        ]


class PixelArtSerializer(serializers.HyperlinkedModelSerializer):
    """PixelArt serializer class."""

    def validate_title(self, value):
        if profanity_predict([value])[0] > 0:
            raise serializers.ValidationError(
                "Your tittle contains offensive words."
            ) 
        return value

    def validate_desc(self, value):
        if sum(profanity_predict(value.split(' '))) > 0:
            raise serializers.ValidationError(
                "Your description contains offensive words."
            ) 
        return value

    class Meta:
        model = PixelArt
        fields = ['url', 'id', 'title', 'desc', 'file', 'price', 'certificate_id']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """Order serializer class."""
    
    def validate_date_purchased(self, value):
        if value.replace(tzinfo=UTC) > dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Date purchased can't be from future.",
            )
        return value

    class Meta:
        model = Order
        fields = ['url', 'id', 'user', 'pixelart', 'date_purchased', 'status']
    
