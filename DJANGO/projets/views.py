from http.client import HTTPResponse
from django.shortcuts import render
#from django.http import HttpResponse

from .models import *
# Create your views here.
def index(request):
    #return HttpResponse("Hello Django")
    projet = Projet.objects.all()
    return render(request, 'index.html' , {'projet':projet})

def accueil(request):
    #return HttpResponse("Hello Django")
    plat = Plat.objects.all()
    return render(request, 'index.html' , {'plat':plat})

def restaurants(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'restaurants.html', {'restaurant':restaurant})

def menus(request):
    menu = Menu.objects.all()
    return render(request, 'menus.html', {'menu':menu})

def connexion(request):
    return render(request, 'connexion.html')

def inscription(request):
    return render(request, 'inscription.html')
