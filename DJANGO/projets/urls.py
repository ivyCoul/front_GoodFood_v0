from . import views 
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('accueil', views.index),
    path('restaurants', views.restaurants),
    path('menus', views.menus),
    path('connexion', views.connexion),
    path('inscription', views.inscription)
] 