from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Customer
# Create your views here.

def sign_out(request):
     logout(request)
     return redirect('home')

def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')

            # Create user accounts
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
            # Create customer object
            customer = Customer.objects.create(
                user = user,
                address = address
            )

            success_message = "Account Created"
            messages.success(request, success_message)

            # return redirect('home')
        except Exception as e:
            error_message = "Duplicate user or Invalid inputs"
            messages.error(request, error_message)

    elif request.POST and 'login' in request.POST:
            context['register'] = False
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('home')

                # success_message = "Account fetched"
                # messages.success(request, success_message)
            else:
                error_message = "Invalid credentials"
                messages.error(request, error_message)

    return render(request, 'account.html', context)