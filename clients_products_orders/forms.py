from django import forms
from .models import Client, Product, Order, OrderItem


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'creation_date']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'total_amount', 'order_date']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']

