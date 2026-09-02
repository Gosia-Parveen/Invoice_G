
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


#------------------------------------------------------subscription----------------------------------------------------
class Subscription(models.Model):

    customer_name = models.CharField(max_length=100)
    billing_email = models.EmailField()
    plan = models.CharField(max_length=100)

    billing_cycle = models.CharField(
        max_length=20,
        choices=[
            ("Monthly", "Monthly"),
            ("Yearly", "Yearly"),
        ]
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    start_date = models.DateField()

    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    collaborators = models.ManyToManyField(
        User,
        related_name="collaborated_subscriptions",
        blank=True
    )

    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name


#------------------------------------------------------invoice----------------------------------------------------
class Invoice(models.Model):

    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Issued', 'Issued'),
        ('Paid', 'Paid'),
        ('Void', 'Void'),
    ]

    subscription = models.ForeignKey(
        'Subscription',
        on_delete=models.CASCADE,
        related_name='invoices'
    )

    invoice_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    billing_period_start = models.DateField()
    billing_period_end = models.DateField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    due_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Draft'
    )

    void_reason = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.invoice_number


class CreditNote(models.Model):

    invoice = models.OneToOneField(
        Invoice,
        on_delete=models.CASCADE,
        related_name='credit_note'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    reason = models.TextField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_credit_notes'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Credit Note - {self.invoice.invoice_number}"
