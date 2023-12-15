"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from business.views import index, LoginView, signup
from business.views import CustomLogoutView
from business.views import business_list
from business.views import create_business
from business.views import my_business
from business.views import business_page
from business.views import create_menu_item

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("form/", create_business, name="form"),
    path("business_list/", business_list, name="business_list"),
    path("my_business/", business_page, name="my_business"),
    path("my_business/<uuid:business_id>/", my_business, name="your_business"),
    path(
        "my_business/<uuid:business_id>/menu/",
        create_menu_item,
        name="create_menu_item",
    ),
]
