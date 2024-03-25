from django.urls import path
from . import views

app_name = 'clients_products_orders'

urlpatterns = [
    path('', views.index, name='index'),
]