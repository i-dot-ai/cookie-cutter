from django.contrib import admin
from django.urls import include, path

from {{cookiecutter.package_name}}.{{cookiecutter.appname}} import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("home/", views.homepage_view, name="homepage"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
