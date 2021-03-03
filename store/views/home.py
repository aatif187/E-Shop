from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


class Index(View):
    def post(self,request):
        product= request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity= cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product]= quantity-1
                else:
                    cart[product]= quantity+1
            else :
                cart[product]=1
        
        else:
            cart={}
            cart[product]=1
        
        request.session['cart']=cart
        print('cart'  , cart)
        return redirect('homepage')
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        prds = None
        categs = Category.get_All_Category()

        categoryId = request.GET.get('category')
        if categoryId:
            prds = Product.get_Products_by_categoryId(categoryId)
        else:
            prds = Product.get_All_Products()
        data = {}
        data['products'] = prds
        data['categories'] = categs
        return render(request, 'index.html', data)




    