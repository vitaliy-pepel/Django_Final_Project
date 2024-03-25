from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_ordered_products_last_days(self, days):
        start_date = timezone.now() - timezone.timedelta(days=days)
        ordered_products = set()

        for order in self.orders.filter(order_date__gte=start_date):
            for item in order.items.all():
                ordered_products.add(item.product)

        return ordered_products.order_by('-creation_date')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order {self.id} for {self.client.name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}x ({self.price})'


