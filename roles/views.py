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

    if request.user.is_superuser:
        subscriptions = Subscription.objects.filter(
            is_archived=False
        )

    elif request.user.groups.filter(name="Account Manager").exists():
        subscriptions = Subscription.objects.filter(
            is_archived=False
        ).filter(
            Q(owner=request.user) |
            Q(collaborators=request.user)
        ).distinct()

    else:
        subscriptions = Subscription.objects.none()

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

        subscription = Subscription.objects.create(
            customer_name=request.POST.get("customer_name"),
            billing_email=request.POST.get("billing_email"),
            plan=request.POST.get("plan"),
            billing_cycle=request.POST.get("billing_cycle"),
            price=request.POST.get("price"),
            start_date=request.POST.get("start_date"),
            owner_id=request.POST.get("owner")
        )

        collaborator_ids = request.POST.getlist("collaborators")
        subscription.collaborators.set(collaborator_ids)

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



# -------------------------------LIST ALL INVOICES----------------------------------------------------
@login_required
def invoice_list(request):

    invoices = Invoice.objects.select_related(
        'subscription',
        'subscription__owner'
    ).prefetch_related(
        'credit_note'
    ).all()

# -----------------------------ROLE-BASED ACCESS------------------------------------------

    if request.user.groups.filter(name='Account Manager').exists():
        invoices = invoices.filter(     # Account Manager sees only invoices belonging to subscriptions they own
            subscription__owner=request.user
    )
    # ---------------- SEARCH ----------------

    search = request.GET.get('search', '').strip()

    if search:
        invoices = invoices.filter(
            Q(subscription__customer_name__icontains=search) |
            Q(subscription__billing_email__icontains=search)
        )

    # ---------------- STATUS FILTER ----------------

    status = request.GET.get('status', '')

    if status:
        invoices = invoices.filter(status=status)

    # ---------------- OVERDUE FILTER ----------------

    overdue = request.GET.get('overdue', '')

    if overdue == 'yes':
        invoices = invoices.filter(
            status='Issued',
            due_date__lt=timezone.now().date()
        )

    elif overdue == 'no':
        invoices = invoices.exclude(
            status='Issued',
            due_date__lt=timezone.now().date()
        )

    # ---------------- OWNER FILTER ----------------

    owner = request.GET.get('owner', '')

    if owner:
        invoices = invoices.filter(
            subscription__owner_id=owner
        )

    # ---------------- SORTING ----------------

    sort = request.GET.get('sort', '')

    if sort == 'due_date':
        invoices = invoices.order_by('due_date')

    elif sort == 'amount':
        invoices = invoices.order_by('amount')

    elif sort == 'status':
        invoices = invoices.order_by('status')

    else:
        invoices = invoices.order_by('-id')

    # ---------------- PAGINATION ----------------

    paginator = Paginator(invoices, 10)

    page_number = request.GET.get('page')

    invoices = paginator.get_page(page_number)

    account_managers = request.user.__class__.objects.filter(
        groups__name='Account Manager'
    ).distinct()

    #change according to manager
    is_account_manager = request.user.groups.filter(
        name='Account Manager'
    ).exists()
#
    return render(
        request,
        'invo.html',
        {
            'invoices': invoices,
            'account_managers': account_managers,
            'is_account_manager': is_account_manager,
        }
    )

# -------------------------------ADD INVOICES----------------------------------------------------
@login_required
def add_invoice(request):

    subscriptions = Subscription.objects.filter(
        is_archived=False
    ).select_related('owner')

    # Account Manager can only use their own subscriptions
    if request.user.groups.filter(name='Account Manager').exists():
        subscriptions = subscriptions.filter(
            owner=request.user
        )

    if request.method == 'POST':

        subscription_id = request.POST.get('subscription')
        billing_period_start = request.POST.get('billing_period_start')
        billing_period_end = request.POST.get('billing_period_end')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')

        subscription = get_object_or_404(
            Subscription,
            id=subscription_id,
            is_archived=False
        )

        # Account Manager can only create invoices for subscriptions they own
        if request.user.groups.filter(name='Account Manager').exists():
            if subscription.owner != request.user:
                messages.error(
                    request,
                    'You do not have permission to create an invoice for this subscription.'
                )
                return redirect('invoice_list')

        invoice = Invoice.objects.create(
            subscription=subscription,
            billing_period_start=billing_period_start,
            billing_period_end=billing_period_end,
            amount=amount,
            due_date=due_date,
            status='Draft'
        )

        invoice.invoice_number = f"INV-{invoice.id:04d}"
        invoice.save(update_fields=['invoice_number'])

        messages.success(
            request,
            'Invoice created successfully.'
        )

        return redirect('invoice_list')

    return render(
        request,
        'invo_form.html',
        {
            'subscriptions': subscriptions,
        }
    )


# -------------------------------EDIT INVOICES----------------------------------------------------
@login_required
def edit_invoice(request, invoice_id):

    invoice = get_object_or_404(
        Invoice,
        id=invoice_id
    )

    # Account Manager can only edit their own invoices
    if request.user.groups.filter(name='Account Manager').exists():
        if invoice.subscription.owner != request.user:
            messages.error(
                request,
                'You do not have permission to edit this invoice.'
            )
            return redirect('invoice_list')

    subscriptions = Subscription.objects.filter(
        is_archived=False
    ).select_related('owner')


    #change according to manager
    if request.user.groups.filter(name='Account Manager').exists():
        subscriptions = subscriptions.filter(
            owner=request.user
        )
#
    if invoice.status == 'Paid':
        messages.error(
            request,
            'A Paid invoice is immutable and cannot be edited.'
        )
        return redirect('invoice_list')

    if invoice.status == 'Void':
        messages.error(
            request,
            'A Void invoice cannot be edited.'
        )
        return redirect('invoice_list')

    if request.method == 'POST':

        # Draft → everything can be changed
        if invoice.status == 'Draft':

            subscription_id = request.POST.get('subscription')

            invoice.subscription = get_object_or_404(
                Subscription,
                id=subscription_id,
                is_archived=False
            )

            invoice.billing_period_start = request.POST.get(
                'billing_period_start'
            )

            invoice.billing_period_end = request.POST.get(
                'billing_period_end'
            )

            invoice.amount = request.POST.get('amount')

            invoice.due_date = request.POST.get(
                'due_date'
            )

            invoice.save()

            messages.success(
                request,
                'Draft invoice updated successfully.'
            )

        # Issued → only due date
        elif invoice.status == 'Issued':

            invoice.due_date = request.POST.get(
                'due_date'
            )

            invoice.save(
                update_fields=[
                    'due_date',
                    'updated_at'
                ]
            )

            messages.success(
                request,
                'Invoice due date updated successfully.'
            )

        return redirect('invoice_list')

    return render(
        request,
        'invo_form.html',
        {
            'invoice': invoice,
            'subscriptions': subscriptions,
        }
    )


# -------------------------------ISSUE INVOICES----------------------------------------------------
@login_required
def issue_invoice(request, invoice_id):

    invoice = get_object_or_404(
        Invoice,
        id=invoice_id
    )

    #change according to manager
    if request.user.groups.filter(name='Account Manager').exists():
        if invoice.subscription.owner != request.user:
            messages.error(
                request,
                'You do not have permission to issue this invoice.'
            )
            return redirect('invoice_list')
#
    if request.method != 'POST':
        return redirect('invoice_list')

    if invoice.status != 'Draft':

        messages.error(
            request,
            'Only a Draft invoice can be issued.'
        )

        return redirect('invoice_list')

    if invoice.billing_period_start > invoice.billing_period_end:

        messages.error(
            request,
            'Billing period start date cannot be after the end date.'
        )

        return redirect('invoice_list')

    invoice.status = 'Issued'

    invoice.save(
        update_fields=[
            'status',
            'updated_at'
        ]
    )

    messages.success(
        request,
        f'{invoice.invoice_number} has been issued.'
    )

    return redirect('invoice_list')


# -------------------------------MARK AS PAID INVOICES----------------------------------------------------
@login_required
def mark_invoice_paid(request, invoice_id):

    invoice = get_object_or_404(
        Invoice,
        id=invoice_id
    )
    #change according to manager
    if request.user.groups.filter(name='Account Manager').exists():
        if invoice.subscription.owner != request.user:
            messages.error(
                request,
                'You do not have permission to mark this invoice as paid.'
            )
            return redirect('invoice_list')
    #
    if request.method != 'POST':
        return redirect('invoice_list')

    if invoice.status != 'Issued':

        messages.error(
            request,
            'Only an Issued invoice can be marked as Paid.'
        )

        return redirect('invoice_list')

    invoice.status = 'Paid'

    invoice.save(
        update_fields=[
            'status',
            'updated_at'
        ]
    )

    messages.success(
        request,
        f'{invoice.invoice_number} has been marked as Paid.'
    )

    return redirect('invoice_list')


# -------------------------------VOID INVOICES----------------------------------------------------
@login_required
def void_invoice(request, invoice_id):

    invoice = get_object_or_404(
        Invoice,
        id=invoice_id
    )
    #change according to manager
    if request.user.groups.filter(name='Account Manager').exists():
        if invoice.subscription.owner != request.user:
            messages.error(
                request,
                'You do not have permission to void this invoice.'
            )
            return redirect('invoice_list')
    #

    if request.method != 'POST':
        return redirect('invoice_list')

    if invoice.status not in ['Draft', 'Issued']:

        messages.error(
            request,
            'Only Draft or Issued invoices can be voided.'
        )

        return redirect('invoice_list')

    reason = request.POST.get('void_reason', '').strip()

    if not reason:

        messages.error(
            request,
            'A reason is required to void an invoice.'
        )

        return redirect('invoice_list')

    invoice.status = 'Void'
    invoice.void_reason = reason

    invoice.save(
        update_fields=[
            'status',
            'void_reason',
            'updated_at'
        ]
    )

    messages.success(
        request,
        f'{invoice.invoice_number} has been voided.'
    )

    return redirect('invoice_list')

# -------------------------------CREDIT_NOTE INVOICES----------------------------------------------------
@login_required
def create_credit_note(request, invoice_id):

    invoice = get_object_or_404(
        Invoice,
        id=invoice_id
    )

    if request.method != 'POST':
        return redirect('invoice_list')

    if invoice.status != 'Paid':

        messages.error(
            request,
            'A credit note can only be created for a Paid invoice.'
        )

        return redirect('invoice_list')

    if hasattr(invoice, 'credit_note'):

        messages.error(
            request,
            'A credit note already exists for this invoice.'
        )

        return redirect('invoice_list')

    amount = request.POST.get('amount')
    reason = request.POST.get('reason', '').strip()

    if not amount or not reason:

        messages.error(
            request,
            'Credit note amount and reason are required.'
        )

        return redirect('invoice_list')

    CreditNote.objects.create(
        invoice=invoice,
        amount=amount,
        reason=reason,
        created_by=request.user
    )

    messages.success(
        request,
        'Credit note created successfully.'
    )

    return redirect('invoice_list')
