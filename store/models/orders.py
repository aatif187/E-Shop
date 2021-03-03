from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price= models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status= models.BooleanField(default='False')
    
    

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customerID(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
