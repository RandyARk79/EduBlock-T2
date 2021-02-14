from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'home.html', context)


def index(request):
    return render(request, 'index.html', {})
