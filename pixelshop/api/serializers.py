"""Serializers file."""

from rest_framework import serializers
from pixelshop.models import User, Order, PixelArt
from pytz import UTC
import datetime as dt
from profanity_check import predict as profanity_predict


class UserSerializer(serializers.ModelSerializer):
    """User serializer class."""

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
        fields = '__all__'


class PixelArtSerializer(serializers.ModelSerializer):
    """PixelArt serializer class."""

    class Meta:
        model = PixelArt
        fields = '__all__'

    def validate_title(self, value):
        if profanity_predict([value])[0] > 0:
            raise serializers.ValidationError(
                "Your tittle contains offensive words."
            ) 
        return value

    def validate_desc(self, value):
        if sum(profanity_predict(list.split(' '))) > 0:
            raise serializers.ValidationError(
                "Your description contains offensive words."
            ) 
        return value


class OrderSerializer(serializers.ModelSerializer):
    """Order serializer class."""
        
    class Meta:
        model = Order
        fields = '__all__'
    
    def validate_date_purchased(self, value):
        if value.replace(tzinfo=UTC) > dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Date purchased can't be from future.",
            )
        return value