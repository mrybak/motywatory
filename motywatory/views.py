# Create your views here.
from django.shortcuts import render
from motywatory.models import Motivator


def index(request):
    motivators = Motivator.objects.all().order_by('created_on').reverse()
    return render(request, 'index.html', {'motivators': motivators})

def add(request):
    return render(request, 'add.html')