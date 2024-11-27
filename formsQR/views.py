from django.shortcuts import render

def encuestas(request):
    return render(request, 'encuestas/encuesta.html')

def codigoQR(request):
    return render(request, 'codigoQR/codigoQR.html')
