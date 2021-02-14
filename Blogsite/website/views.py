from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def index(request):
    return render(request, 'index.html', {})