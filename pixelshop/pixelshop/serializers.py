"""Serializers file."""

from rest_framework import serializers
from models import User

# zostawmy to bez komentarza, dobrze?
offensive_words = [
    'kurwa',
    'chuj',
    'huj',
    'dupa',
    'cipa',
    'jebac',
    'czarnuch',
    'nigger',
]

class UserSerializer(serializers.Serializer):
    """User serializer class."""

    class Meta:
        model = User
        fields = ['username', 'password']

    
    def validate_passwd(self, value):
        """Check that password is compatible with standards."""

        if len(value) < 8:
            raise serializers.ValidationError(
                "Hasło jest zbyt krótkie. Musi składać się z conajmnuiej 8 znaków."
            )
        special_characters = "!@#$%^&*()"
        upper_letter = False
        special_character = False
        for x in list(value): 
            if x in list(value.upper()):
                upper_letter = True
            if x in list(special_characters):
                special_character = True
        if not upper_letter:
            raise serializers.ValidationError(
                "Hasło musi posiadać conajmniej jedną wielką literę."
            )
        elif not special_character:
            raise serializers.ValidationError(
                "Hasło musi zawierać conajmniej jeden znak specjalny."
            )
        return value

    def create(self, validated_data):
        return User.objects.create(self, **validated_data)