from django.shortcuts import render

# Product page

def index(request):
    return render(request, 'index.html')

def list_products(request):
    return render(request, 'products.html')

def detail_products(request):
    return render(request, 'product_details.html')
