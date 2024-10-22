from django.forms import ModelForm
from .models import PostModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ["content", "picture"]

