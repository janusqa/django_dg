from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
]
