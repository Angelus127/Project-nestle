from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm


def index(request):
    return render(request, 'inicio/index.html')

def product_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.Post, request.FILES)
        if form.is_valid():
            return redirect('Producto')
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, 'productos/products.html', {'form': form, 'productos': productos})

def report_view(request):
    return render(request, 'inicio/report.html')