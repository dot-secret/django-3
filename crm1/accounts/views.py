from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from . filters import OrderFilter
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

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count,
               'myFilter': myFilter}
    return render(request, 'accounts/customer.html',context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing Coba:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html',context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Printing Coba:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'accounts/order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)

