from django.contrib import admin

from supplier.models import Supplier, Invoice, Payment

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Invoice)
admin.site.register(Payment)
