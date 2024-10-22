from django.shortcuts import render
from django.views.generic.edit import FormView

from posts.forms import PostForm
from posts.models import PostModel

class PostFormView(FormView):
    template_name = "index.html"
    form_class = PostForm
    success_url = "/"


    def get(self, request):
        posts = PostModel.objects.all()

        form = PostForm()
        return render(request, self.template_name, {"posts": posts, "form": form})


    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

