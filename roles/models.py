
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


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

    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.customer_name
