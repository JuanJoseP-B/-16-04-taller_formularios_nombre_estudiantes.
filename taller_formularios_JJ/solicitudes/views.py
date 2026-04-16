from django.shortcuts import render, redirect
from .forms import SolicitudForm

def registrar_solicitud(request):
    if request.method == 'POST':
        # request.FILES es OBLIGATORIO para preprocesar el FileField
        form = SolicitudForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('solicitud_exito') # Hacer redirect a una url de exito (debemos crearla en urls.py)
    else:
        form = SolicitudForm()
    
    return render(request, 'solicitudes/formulario.html', {'form': form})

def solicitud_exito(request):
    return render(request, 'solicitudes/exito.html')
