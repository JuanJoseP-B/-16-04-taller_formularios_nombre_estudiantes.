from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_solicitud, name='registrar_solicitud'),
    path('exito/', views.solicitud_exito, name='solicitud_exito'),
]
