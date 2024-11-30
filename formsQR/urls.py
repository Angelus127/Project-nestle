from django.urls import path
from . import views

urlpatterns = [
    path('encuestas/', views.encuestas, name='encuesta'),
    path('QR/', views.codigoQR, name='QR')
]