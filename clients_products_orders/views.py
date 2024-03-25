from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from .models import Client, Product, Order, OrderItem
from .forms import ClientForm, ProductForm, OrderForm, OrderItemForm


def index(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        product_form = ProductForm(request.POST)
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)

        if client_form.is_valid():
            client_form.save()
        elif product_form.is_valid():
            product_form.save()
        elif order_form.is_valid():
            order_form.save()
        elif order_item_form.is_valid():
            order_item_form.save()

        return redirect('clients_products_orders:index')

    else:
        client_form = ClientForm()
        product_form = ProductForm()
        order_form = OrderForm()
        order_item_form = OrderItemForm()

    create_test_data()

    context = {
        'client_form': client_form,
        'product_form': product_form,
        'order_form': order_form,
        'order_item_form': order_item_form,
    }
    return render(request, 'clients_products_orders/index.html', context)


def create_test_data():
    Client.objects.all().delete()
    Product.objects.all().delete()
    Order.objects.all().delete()
    OrderItem.objects.all().delete()

    for i in range(1, 6):
        Client.objects.create(
            name=f'Client {i}',
            email=f'client{i}@example.com',
            phone_number=f'+799912345{i}',
            address=f'Address {i}',
        )

    for i in range(1, 21):
        Product.objects.create(
            name=f'Product {i}',
            description=f'Description {i}',
            price=i * 10,
            quantity=100,
            creation_date=timezone.make_aware(datetime(2023, 1, 1)),
        )

    for i in range(1, 6):
        order = Order.objects.create(
            client=Client.objects.get(pk=i),
            total_amount=500,
            order_date='2023-01-01',
        )

        for j in range(1, 6):
            OrderItem.objects.create(
                order=order,
                product=Product.objects.get(pk=j),
                quantity=1,
            )
