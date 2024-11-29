from django.shortcuts import render
from .models import Encuesta
from .forms import EncuestaForm



def codigoQR(request):
    return render(request, 'codigoQR/codigoQR.html')

def encuesta_view(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Encuesta')
    else:
        form = EncuestaForm()
    
    encuestas = Encuesta.objects.all()
    return render(request, 'encuestas/encuesta.html', {'form': form, 'encuestas': encuestas})

