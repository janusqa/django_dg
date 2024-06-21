from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())  # form.save() returns user
            return redirect("posts:list")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())  # form.get_user returns user
            return redirect(
                request.POST.get("next") if "next" in request.POST else "posts:list"
            )
    else:
        form = AuthenticationForm()

    return render(request, "users/signin.html", {"form": form})


def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")
