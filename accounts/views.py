from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

# 🔥 IMPORTANT (for custom user model)
User = get_user_model()


# LOGIN VIEW
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")   # redirect to home

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


# SIGNUP VIEW
def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # check if user already exists
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists"
            })

        # create user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # auto login after signup
        login(request, user)

        return redirect("/")   # go to home

    return render(request, "signup.html")


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect("/")