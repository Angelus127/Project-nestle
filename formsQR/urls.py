from django.urls import path
from . import views

urlpatterns = [
    path('QR/', views.codigoQR, name='QR'),
    path('encuesta/', views.encuesta_view, name='encuesta')
]