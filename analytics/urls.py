from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index , name='index'),
    path('productos/', views.product_view, name='producto'),
    path('index/report/', views.report_view, name='report'),
    path('productos/<int:producto_id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]