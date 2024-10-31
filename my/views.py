from django.shortcuts import render
from django.views.generic.edit import FormView

from posts.forms import PostForm, PostCommentsForm
from posts.models import PostModel, PostCommentsModel

class PostFormView(FormView):
    template_name = "index.html"
    form_class = PostForm
    success_url = "/"


    def get(self, request):
        posts = PostModel.objects.all()

        form = PostForm()
        return render(request, self.template_name, {"posts": posts, "form": form})


    def form_valid(self, form):
        post = form.save(commit=False)
        post.posted_by = self.request.user # Associate the post with the current user.
        post.save()

        return super().form_valid(form)

"""
class PostCommentsView(FormView):
    template_name = "index.html"
    form_class = PostCommentsForm
    success_url = "/" 
"""

