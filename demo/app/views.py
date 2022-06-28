from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from . models import Category, Product
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products':products,'categories':categories})


def category_detail(request, id):   
    category = Category.objects.get(id=id)  
    return render(request, 'pages/category-details.html', {'category':category})



def product_detail(request, id):   
    product = Product.objects.get(id=id)    
    return render(request, 'pages/product-detail.html', {'product':product})