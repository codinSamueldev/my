from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegistrationForm

# Create your views here.
def registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "users/registration.html", {"form": form})

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
            return render(request, "users/registration.html", {"form": form})
        
