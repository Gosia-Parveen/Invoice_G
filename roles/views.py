from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


# -------------------------- LOGIN ----------------------------------------

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Find user using email
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

def admin_dash(request):
    return render(request, "admin_dash.html")


# -------------------------- ACCOUNT MANAGER DASHBOARD ---------------------

def acc_man(request):
    return render(request, "acc_man.html")
