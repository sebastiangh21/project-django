from django.shortcuts import render
from Servicios.models import Servicio

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})