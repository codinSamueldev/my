from django.shortcuts import render


def home(request):
    # posts = Posts.objects.all()
    posts = "Nothing yet .-."
    
    return render(request, 'index.html', {"posts": posts})

