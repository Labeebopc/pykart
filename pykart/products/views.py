from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Product page

def index(request):
    return render(request, 'index.html')

def product_list(request):

    # To calculate requested page
    page = 1
    if request.GET:
        page = request.GET.get("page", 1)

    # Fetch products
    fetchProducts = Product.objects.all()

    # Pagination
    product_paginator = Paginator(fetchProducts, 2)

    fetchProducts = product_paginator.get_page(page)

    # Create a dictionary
    context = {
        "products" : fetchProducts
    }
    return render(request, 'products.html', context)

def product_details(request):
    return render(request, 'product_details.html')

