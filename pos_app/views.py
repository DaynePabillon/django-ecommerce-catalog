from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'pos_app/product_list.html', {'products': products})

def home(request):
    return render(request, 'pos_app/home.html')
