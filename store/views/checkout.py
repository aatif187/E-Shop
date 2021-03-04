
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


class CheckOut(View):
    def post(self, request):
        address= request.POST.get('address')
        phone= request.POST.get('phone')
        cart= request.session.get('cart')
        products= Product.get_products_by_id(list(cart.keys()))
        customer= request.session.get('customer')
        
        for pp in products:
            order= Order(
                customer= Customer(id= customer),
                product= pp,
                price= pp.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(pp.id))
            )
            
            order.place_order()
        request.session['cart']={}
        print('+++++PASSED CHECKOUT=====+++++++++')
        return redirect('homepage')
