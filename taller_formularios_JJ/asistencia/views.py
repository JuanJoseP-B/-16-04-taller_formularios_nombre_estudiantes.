from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia_exito') # Evita usar render() tras un POST exitoso
    else:
        form = AsistenciaForm()
        
    return render(request, 'asistencia/formulario.html', {'form': form})

def asistencia_exito(request):
    return render(request, 'asistencia/exito.html')