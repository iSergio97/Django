from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index),
    path('index.html/', views.index),
    path('buscar_fechas.html/', views.buscarEventosPorFecha),
    path('buscar_idiomas.html/', views.buscarEventosPorIdioma),
    path('eventos_municipio.html/', views.mostrar_eventos_codigo)
    ]
