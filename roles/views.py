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


# -------------------------------Subs---------------------------------------
@login_required
def subs_tab(request):
    subscriptions = Subscription.objects.filter(is_archived=False)

    return render(request, "subs.html", {
        "subscriptions": subscriptions
    })



# -------------------------------Subs_FORM--------------------------------------------
@login_required
def add_subscription(request):

    account_managers = User.objects.filter(
        groups__name="Account Manager"
    )

    if request.method == "POST":
        Subscription.objects.create(
            customer_name=request.POST.get("customer_name"),
            billing_email=request.POST.get("billing_email"),
            plan=request.POST.get("plan"),
            billing_cycle=request.POST.get("billing_cycle"),
            price=request.POST.get("price"),
            start_date=request.POST.get("start_date"),
            owner_id=request.POST.get("owner")
        )

        return redirect("subs_tab")

    return render(request, "new_sub.html", {
        "account_managers": account_managers
    })



# -------------------------------Subs_FORM_EDIT----------------------------------------------------
@login_required
def edit_subscription(request, id):

    subscription = Subscription.objects.get(id=id)

    account_managers = User.objects.filter(
        groups__name="Account Manager"
    )

    if request.method == "POST":
        subscription.customer_name = request.POST.get("customer_name")
        subscription.billing_email = request.POST.get("billing_email")
        subscription.plan = request.POST.get("plan")
        subscription.billing_cycle = request.POST.get("billing_cycle")
        subscription.price = request.POST.get("price")
        subscription.start_date = request.POST.get("start_date")
        subscription.owner_id = request.POST.get("owner")

        subscription.save()

        return redirect("subs_tab")

    return render(request, "new_sub.html", {
        "subscription": subscription,
        "account_managers": account_managers
    })
