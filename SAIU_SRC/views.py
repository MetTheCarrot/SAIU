from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from SAIU_DATOS.models import Agosto, Septiembre, Octubre, Noviembre
import time


@login_required
def base(request):
    a = []
    b = []
    c = []
    d = []
    for i in (Agosto.objects.all()):
        a.append(i.primeraSemana)
        a.append(i.segundaSemana)
        a.append(i.terceraSemana)
        a.append(i.cuartaSemana)
    for i in (Septiembre.objects.all()):
        b.append(i.primeraSemana)
        b.append(i.segundaSemana)
        b.append(i.terceraSemana)
        b.append(i.cuartaSemana)
    for i in (Octubre.objects.all()):
        c.append(i.primeraSemana)
        c.append(i.segundaSemana)
        c.append(i.terceraSemana)
        c.append(i.cuartaSemana)
    for i in (Noviembre.objects.all()):
        d.append(i.primeraSemana)
        d.append(i.segundaSemana)
        d.append(i.terceraSemana)
        d.append(i.cuartaSemana)
    #date today
    today = time.strftime("%d/%m/%y")
    return render(request, "informacion.html", {"a": a, "b": b, "c": c, "d": d, "today": today})