from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Business, Item
from django.utils import timezone
from django.forms import modelform_factory
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import os
import uuid

load_dotenv()


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
        exclude=("user", "pub_date", "likes", "id", "image", "items"),
    )
    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.pub_date = timezone.now()
            business.likes = 0
            # Azure Blob Storage upload
            blob_service_client = BlobServiceClient.from_connection_string(
                os.getenv("AZURE_CONNECTION_STRING"),
            )

            # Generate a unique filename by appending a UUID
            unique_filename = str(uuid.uuid4()) + "_" + request.FILES["image"].name

            blob_client = blob_service_client.get_blob_client("dj2", unique_filename)

            blob_client.upload_blob(request.FILES["image"].read())
            business.image = blob_client.url

            business.save()
            return redirect("business_list")
    else:
        form = BusinessForm()
    return render(request, "form.html", {"form": form})


def business_list(request):
    businesses = Business.objects.all()
    return render(request, "business_list.html", {"businesses": businesses})


@login_required
def business_page(request):
    businesses = Business.objects.filter(user=request.user)
    return render(request, "my_business.html", {"businesses": businesses})


@login_required
def my_business(request, business_id):
    business = Business.objects.get(id=business_id, user=request.user)
    return render(request, "your_business.html", {"business": business})


@login_required
def create_menu_item(request, business_id):
    ItemForm = modelform_factory(
        Item,
        fields=(
            "name",
            "price",
        ),
        exclude=("rating", "id", "image"),
    )
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.rating = 0

            # Azure Blob Storage upload
            blob_service_client = BlobServiceClient.from_connection_string(
                os.getenv("AZURE_CONNECTION_STRING"),
            )

            # Generate a unique filename by appending a UUID
            unique_filename = str(uuid.uuid4()) + "_" + request.FILES["image"].name

            blob_client = blob_service_client.get_blob_client("dj2", unique_filename)

            blob_client.upload_blob(request.FILES["image"].read())
            item.image = blob_client.url

            item.save()

            # Fetch the Business and add the Item to it
            business = Business.objects.get(id=business_id)
            business.items.add(item)

            return redirect("your_business", business_id=business_id)
        else:
            print(form.errors)  # print form errors
    else:
        form = ItemForm()
    return render(request, "menu_add.html", {"form": form})


@login_required
def view_menu(request, business_id):
    business = Business.objects.get(id=business_id, user=request.user)
    items = business.items.all()
    return render(request, "view_menu.html", {"items": items})
