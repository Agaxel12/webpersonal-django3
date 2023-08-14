from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def home(request):
    productos = Product.objects.all()
    return render(request, "core/home.html", {'productos' : productos})

def contact(request):
    return render(request, "core/contact.html")

def all_products(request):
    productos = Product.objects.all()
    return render(request, "core/all_products.html", {'productos': productos})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'core/product_detail.html', {'product': product})
def confirmacion_compra(request):
    return render(request, 'core/confirmacion_compra.html')
def home(request):
    productos = Product.objects.all().order_by('-created')[:3]  # Get the three latest products
    return render(request, "core/home.html", {'productos': productos})
