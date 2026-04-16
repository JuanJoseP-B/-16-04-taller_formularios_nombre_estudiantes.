# Ejemplo para asistencia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_asistencia, name='registrar_asistencia'),
    path('exito/', views.asistencia_exito, name='asistencia_exito'),
]