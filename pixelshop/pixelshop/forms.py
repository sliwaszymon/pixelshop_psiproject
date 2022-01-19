"""Forms file."""

# Django
from django.contrib.auth.forms import UserCreationForm

# Local
from .models import User


class RegisterForm(UserCreationForm):
    """RegisterForm class."""

    class Meta:
        """Meta class."""

        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            ]
