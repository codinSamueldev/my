from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import RegistrationForm
from .models import UserModel
from posts.models import PostModel


# Create your views here.
def registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "users/registration/registration.html", {"form": form})

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password', None)

            if password:
                user.password = make_password(password)

            user.save()
            # messages.success(request, "Great, successful registration :D")
            return HttpResponseRedirect("/")
        else:
            return render(request, "users/registration/registration.html", {"form": form})


def login_view(request):
    
    if request.method == 'GET':
        return render(request, "users/login/login.html", {})
    
    
    if request.method == 'POST':
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            
            return HttpResponseRedirect("/")
        else:
            err_msg = "We could not log you in, make sure email and password are typed correctly"
            
            return render(request, "users/login/login.html", {"err_msg": err_msg})


def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/")


def my_profile(request):

    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("login"))

    profile = UserModel.objects.get(username=request.user)

    posts = PostModel.objects.all().filter(posted_by=profile.id)

    return render(request, "users/profiles/my_profile.html", {'profile': profile, 'posts': posts})


