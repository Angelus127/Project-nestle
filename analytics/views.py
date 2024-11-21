from django.shortcuts import render

def index(request):
    return render(request, 'inicio/index.html')

def product_view(request):
    return render(request, 'productos/products.html')
