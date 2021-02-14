from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('blog/', views.home, name='webhome'),
]
