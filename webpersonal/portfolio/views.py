from django.shortcuts import render
from .models import proyect

# Create your views here.
def portafolio(request):
    proyects = proyect.objects.all()
    return render(request, "portfolio/portafolio.html", {'proyects' : proyects})