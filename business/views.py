from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Business
from django.utils import timezone
from django import forms
from django.forms import modelform_factory


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
def create_business(request):
    BusinessForm = modelform_factory(
        Business,
        fields=(
            "name",
            "address",
            "type",
            "opening_time",
            "closing_time",
            "contact_info",
        ),
        exclude=("user", "pub_date", "likes", "id"),
    )
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.pub_date = timezone.now()
            business.likes = 0
            business.save()
            return redirect("business_list")
    else:
        form = BusinessForm()
    return render(request, "form.html", {"form": form})


def business_list(request):
    businesses = Business.objects.all()
    return render(request, "business_list.html", {"businesses": businesses})
