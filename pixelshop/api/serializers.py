"""Serializers file."""

from rest_framework import serializers
from pixelshop.models import User, Order, PixelArt


class UserSerializer(serializers.ModelSerializer):
    """User serializer class."""

    class Meta:
        model = User
        fields = ['username','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # def validate_password(self, value):
    #     """Check that password is compatible with standards."""

    #     if len(value) < 8:
    #         raise serializers.ValidationError(
    #             "Hasło jest zbyt krótkie. Musi składać się z conajmnuiej 8 znaków."
    #         )
    #     special_characters = "!@#$%^&*()"
    #     upper_letter = False
    #     special_character = False
    #     for x in list(value): 
    #         if x in list(value.upper()):
    #             upper_letter = True
    #         if x in list(special_characters):
    #             special_character = True
    #     if not upper_letter:
    #         raise serializers.ValidationError(
    #             "Hasło musi posiadać conajmniej jedną wielką literę."
    #         )
    #     elif not special_character:
    #         raise serializers.ValidationError(
    #             "Hasło musi zawierać conajmniej jeden znak specjalny."
    #         )
    #     return value



class PixelArtSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=200)
    date_purchased = serializers.DateTimeField()

    def validate_title(self, value):
        pass