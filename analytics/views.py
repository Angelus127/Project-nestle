from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def index(request):

    productos = Producto.objects.all()
    return render(request, 'inicio/index.html', {'productos': productos})

def product_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    
    productos = Producto.objects.all()
    return render(request, 'productos/products.html', {'form': form, 'productos': productos})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()

    return redirect('producto')

def report_view(request):
    return render(request, 'inicio/report.html')