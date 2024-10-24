from django.shortcuts import render

from .forms import RegistrationForm

# Create your views here.
def registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "users/registration.html", {"form": form})
