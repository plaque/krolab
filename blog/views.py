from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def category(request, id=None):
    if(id):
        return render(request, 'category.html', {})
    else:
        return render(request, 'category.html', {})
