from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customer = customers.count()
    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'customers':customers, 'orders': orders,
               'total_customer': total_customer,'total_order':total_order,
               'delivered':delivered,'pending':pending}
    return render(request, 'accounts/dashboard.html',context)
def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count }
    return render(request, 'accounts/customer.html',context)

