from django.urls import path

from supplier import views

urlpatterns = [
    path('', views.index, name='home'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
    path('suppliers/delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
    path('<int:pk>/', views.single, name='single'),
    path('<int:pk>/payment/', views.payment, name='payment'),
    path('invoice/<int:pk>/', views.invoice, name='invoice'),
    path('<int:pk>/delete/invoice/<int:tid>/', views.delete_invoice, name='delete_invoice'),
    path('<int:pk>/delete/payment/<int:tid>/', views.delete_payment, name='delete_payment'),
]