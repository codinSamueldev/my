from django.contrib.auth.forms import BaseUserCreationForm

from .models import UserModel

class RegistrationForm(BaseUserCreationForm):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password", "profile_picture", "bio"]

