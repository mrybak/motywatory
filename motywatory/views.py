# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')