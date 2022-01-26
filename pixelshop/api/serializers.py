"""Serializers file."""

# Standard Library
from datetime import datetime as dt

# Django
from django.contrib.auth.hashers import make_password

# 3rd-party
from profanity_check import predict as profanity_predict
from pytz import UTC
from rest_framework import serializers

# Project
from pixelshop.models import Order
from pixelshop.models import PixelArt
from pixelshop.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer class."""

    url = serializers.HyperlinkedIdentityField(
        view_name='api:user-detail',
        lookup_field='pk',
        )

    def validate_username(self, value):
        """Username validate function."""
        if profanity_predict([value])[0] > 0:
            raise serializers.ValidationError(
                'Your username contains offensive words.',
            )
        return value

    def validate_first_name(self, value):
        """First name validate function."""
        if not value.isalpha():
            raise serializers.ValidationError(
                'First name must contain only letters.',
            )
        elif value != value.capitalize():
            raise serializers.ValidationError(
                'First name must start with big letter.',
            )
        return value

    def validate_last_name(self, value):
        """Last name validate function."""
        if not value.isalpha():
            raise serializers.ValidationError(
                'Last name must contain only letters.',
            )
        elif value != value.capitalize():
            raise serializers.ValidationError(
                'Last name must start with big letter.',
            )
        return value

    def validate_email(self, value):
        """Email validate function."""
        supported_hosts = [
            'hotmail.com',
            'outlook.com',
            'gmail.com',
        ]
        if value.split('@')[1] not in supported_hosts:
            raise serializers.ValidationError(
                'Your email host is not supported.',
            )
        return value
    
    def validate_password(self, value):
        """Password validate function."""
        if len(value) < 8:
            raise serializers.ValidationError(
                'Password must must have at least 8 digits.',
            )
        return make_password(value)

    class Meta:
        """Meta class."""

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
            'is_active',
        ]


class PixelArtSerializer(serializers.HyperlinkedModelSerializer):
    """PixelArt serializer class."""

    url = serializers.HyperlinkedIdentityField(
        view_name='api:pixelart-detail',
        lookup_field='pk',
        )

    def validate_title(self, value):
        """Title validate function."""
        if profanity_predict([value])[0] > 0:
            raise serializers.ValidationError(
                'Your tittle contains offensive words.',
            )
        return value

    def validate_desc(self, value):
        """Desc validate function."""
        if sum(profanity_predict(value.split(' '))) > 0:
            raise serializers.ValidationError(
                'Your description contains offensive words.',
            )
        return value

    class Meta:
        """Meta class."""

        model = PixelArt
        fields = [
            'url',
            'id',
            'title',
            'desc',
            'file',
            'price',
            'certificate_id',
            ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """Order serializer class."""

    url = serializers.HyperlinkedIdentityField(
        view_name='api:order-detail',
        lookup_field='pk',
        )
    user = serializers.HyperlinkedRelatedField(
        lookup_field='pk',
        many=False, view_name='api:user-detail',
        read_only=True,
        )
    pixelart = serializers.HyperlinkedRelatedField(
        lookup_field='pk',
        many=False,
        view_name='api:pixelart-detail',
        read_only=True,
        )

    def validate_date_purchased(self, value):
        """Date purchased validate function."""
        if value.replace(tzinfo=UTC) > dt.now().replace(tzinfo=UTC):
            raise serializers.ValidationError(
                "Date purchased can't be from future.",
            )
        return value

    class Meta:
        """Meta class."""

        model = Order
        fields = ['url', 'id', 'user', 'pixelart', 'date_purchased', 'status']
