from django.db import models
from django.db.models import Sum

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)  # CharField is safer than IntegerField for phones
    country = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    def total_invoiced(self):
        return self.invoices.aggregate(total=Sum('amount'))['total'] or 0

    def total_paid(self):
        return self.payments.aggregate(total=Sum('amount'))['total'] or 0

    def balance(self):
        return self.total_invoiced() - self.total_paid()


class Invoice(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='invoices')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_id = models.CharField(max_length=100, null=True, blank=True)  # nullable, as you said

    def __str__(self):
        return f"{self.supplier.name} - {self.date} - {self.amount}"


class Payment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank = models.CharField(max_length=100, null=True, blank=True)  # nullable

    def __str__(self):
        return f"{self.supplier.name} - {self.date} - {self.amount}"
