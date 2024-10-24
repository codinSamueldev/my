from django.contrib.auth.forms import BaseUserCreationForm

from .models import UserModel

class RegistrationForm(BaseUserCreationForm):
    class Meta:
        model = UserModel
        fields = [
            "email", 
            "username",  
            "profile_picture", 
            "bio"
        ]

