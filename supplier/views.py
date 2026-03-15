from datetime import date

from django.shortcuts import render, redirect

from supplier.models import Supplier, Invoice, Payment
from itertools import chain

# Create your views here.

def index(request):
    query = request.GET.get('searchbar', '')
    suppliers = Supplier.objects.filter(name__icontains=query) if query else Supplier.objects.all()
    return render(request, 'supplier/index.html', {'suppliers': suppliers})

def add_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('supplierName')
        Supplier.objects.create(name=name)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_supplier(request, supplier_id):
    if request.method == 'POST':
        Supplier.objects.filter(id=supplier_id).delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def single(request, pk):
    supplier = Supplier.objects.get(id=pk)

    if request.method == 'POST':
        supplier.name = request.POST.get('supplierName')
        supplier.email = request.POST.get('supplierEmail')
        supplier.phone = request.POST.get('supplierPhone')
        supplier.url = request.POST.get('supplierWebsite')
        supplier.country = request.POST.get('supplierCountry')
        supplier.save()

    invoices = supplier.invoices.all()
    payments = supplier.payments.all()

    # Combine both querysets
    transactions = sorted(
        chain(invoices, payments),
        key=lambda obj: obj.date
    )

    context = {
        'supplier': supplier,
        'transactions': transactions
    }

    return render(request, 'supplier/single.html', context)

def payment(request, pk):
    supplier = Supplier.objects.get(id=pk)

    if request.method == 'POST':
        Payment.objects.create(
            supplier=supplier,
            date=request.POST.get('paymentDate') or date.today(),
            amount=request.POST.get('paymentAmount'),
            bank=request.POST.get('paymentBank'),
        )
        return redirect('single', pk=pk)

    context = {
        'supplier': supplier,
    }
    return render(request, 'supplier/payment.html', context)

def invoice(request, pk):
    supplier = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        Invoice.objects.create(
            supplier=supplier,
            date=request.POST.get('invoiceDate') or date.today(),
            amount=request.POST.get('invoiceAmount'),
            invoice_id=request.POST.get('invoiceId'),
        )
        return redirect('single', pk=pk)
    context = {
        'supplier': supplier,
    }
    return render(request, 'supplier/charge.html', context)

def delete_invoice(request, pk, tid):
    if request.method == 'POST':
        Invoice.objects.filter(id=tid, supplier_id=pk).delete()
    return redirect('single', pk=pk)

def delete_payment(request, pk, tid):
    if request.method == 'POST':
        Payment.objects.filter(id=tid, supplier_id=pk).delete()
    return redirect('single', pk=pk)