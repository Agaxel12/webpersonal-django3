from django.shortcuts import render
from .models import proyect

# Create your views here.
def noticias(request):
    proyects = proyect.objects.all()
    return render(request, "portfolio/noticias.html", {'proyects' : proyects})