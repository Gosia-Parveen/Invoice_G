from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Subscription



# -------------------------- LOGIN ----------------------------------------

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Find the user using their email
        user_obj = User.objects.filter(email=email).first()

        if user_obj:
            # Authenticate using the actual username
            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )
        else:
            user = None

        if user is not None:
            auth_login(request, user)

            # Billing Admin
            if user.is_superuser:
                return redirect("admin_dash")

            # Account Manager
            if user.groups.filter(name="Account Manager").exists():
                return redirect("acc_man")

        return render(request, "login.html", {
            "error": "Invalid email or password."
        })

    return render(request, "login.html")


# -------------------------- ADMIN DASHBOARD -------------------------------

@login_required
def admin_dash(request):

    if not request.user.is_superuser:
        return redirect("login")

    return render(request, "admin_dash.html")


# -------------------------- ACCOUNT MANAGER DASHBOARD ----------------------

@login_required
def acc_man(request):

    if not request.user.groups.filter(name="Account Manager").exists():
        return redirect("login")

    return render(request, "acc_man.html")


# -------------------------- LOGOUT ----------------------------------------

def logout(request):
    auth_logout(request)
    return redirect("login")

