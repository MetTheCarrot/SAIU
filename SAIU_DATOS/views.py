from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from SAIU_DATOS.models import Noviembre
from SAIU_DATOS.forms import estadisticasNoviembre
from django.contrib.auth.decorators import login_required

# Create your views here.

class estadisticas(HttpRequest):
    def noviembre2022(request, id):
        stats = get_object_or_404(Noviembre, id=id)
        formulario = {
            'form': estadisticasNoviembre(instance=stats)
        }
        if request.method == 'POST':
            form = estadisticasNoviembre(data=request.POST, instance=stats)
            if form.is_valid():
                form.save()
                return redirect(to='http://127.0.0.1:8000/')
            formulario["form"] = form
        
        return render(request, "modificar.html", formulario)