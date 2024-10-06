from django.shortcuts import render

# Product page

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'products.html')

def product_details(request):
    return render(request, 'product_details.html')

