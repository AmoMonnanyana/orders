from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import products, Order
from .forms import OrderForm, UpdateStatusForm
from django.http import HttpResponseBadRequest


# Create your views here.
def product_list(request):
    the_products = products.objects.all()
    return render(request, 'product_list.html', {'products': the_products})

def order_list(request):
    order_lists = Order.objects.all()
    print(order_lists)
    return render(request, 'order_list.html', {'orders': order_lists})

def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('order_list')
    else:
        order_form = OrderForm()

    return render(request, 'create_order.html', {'form': order_form})

def update_order_status(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data['new_status']
            order.order_status = new_status
            order.save()
            return redirect('order_list')
    else:
        form = UpdateStatusForm()

    return render(request, 'update_status.html', {'form': form, 'order': order})
    