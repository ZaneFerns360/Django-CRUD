from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Business


def index(request):
    return render(request, "index.html")


class LoginView(LoginView):
    template_name = "login.html"


class CustomLogoutView(LogoutView):
    next_page = "/"


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


@login_required
def guarded_view(request):
    return render(request, "form.html")


def create_business(request):
    if request.method == "POST":
        business = Business(
            user=request.user,
            name=request.POST["business_name"],
            pub_date=request.POST["pub_date"],
            address=request.POST["address"],
            type=request.POST["type"],
            timings=request.POST["timings"],
            likes=request.POST["likes"],
            contact_info=request.POST["contact_info"],
        )
        business.save()
        return redirect("")
    else:
        return render(request, "form.html")
