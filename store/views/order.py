
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


class OrderView(View):
    def get(self, request):
        customer= request.session.get('customer')
        orders= Order.get_orders_by_customerID(customer)
        print(orders)
        return render(request, 'order.html',{'orders':orders})
