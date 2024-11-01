from django.forms import ModelForm
from .models import PostModel, PostCommentsModel


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update(placeholder="What's on ya mind?")
        self.fields["picture"].required = False

    class Meta:
        model = PostModel
        fields = ["content", "picture"]


class PostCommentsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comment"].widget.attrs.update(placeholder="Type a comment here...")
        self.fields["comment"].required = False
        self.fields["picture"].required = False
    
    class Meta:
        model = PostCommentsModel
        fields = ["comment", "picture"]

