from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password
                            )

        error_message = self.validation_user(customer)
        # saving
        if not error_message:

            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validation_user(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Name Required."
        elif len(customer.first_name) < 4:
            error_message = "FirstName must greater than 4 character"
        elif not customer.last_name:
            error_message = "Name Required."
        elif len(customer.last_name) < 4:
            error_message = "LastName must greater than 4 character"
        elif not customer.phone:
            error_message = "Phone Required"
        elif len(customer.phone) < 10:
            error_message = "phone must equal to 10 characters"

        elif not customer.password:
            error_message = "Password Required."
        elif len(customer.password) < 4:
            error_message = "password must be grater than 4 characters"
        elif customer.isExists():
            error_message = "Email Already Exists."

        return error_message
