from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponse

from posts.forms import PostForm, PostCommentsForm
from posts.models import PostModel, PostCommentsModel

class PostFormView(FormView):
    template_name = "index.html"
    form_class = PostForm
    success_url = "/"


    def get(self, request):
        posts = PostModel.objects.all()
        comments = PostCommentsModel.objects.all()

        comment_form = PostCommentsForm()
        post_form = PostForm()

        return render(request, self.template_name, {'posts': posts, 'form': post_form, 'comments': comments, 'comment_form': comment_form})
    

    def post(self, request, *args, **kwargs):
        comment_form = PostCommentsForm(request.POST, request.FILES)
        post_form = PostForm(request.POST, request.FILES)

        if 'post' in request.POST:
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.posted_by = self.request.user # Associate the post with the current user.
                post.save()
                return redirect("home")

        if 'submit_comment' in request.POST:
            post_id = request.POST.get("post")
            
            print(f"\n  {post_id}  \n")

            if post_id:
                commented_post = PostModel.objects.get(id=post_id)
            else:
                return HttpResponse("Aqui no hay ningun post_id pelao")

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.commented_by = request.user
                comment.post = commented_post
                comment.save()
                return redirect("home")
        
        
        posts = PostModel.objects.all()
        comments = PostCommentsModel.objects.all()

        return render(request, self.template_name, {'posts': posts, 'form': post_form, 'comments': comments, 'comment_form': comment_form})


