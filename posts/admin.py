from django.contrib import admin

from .models import PostModel, PostCommentsModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(PostCommentsModel)

