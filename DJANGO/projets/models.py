from django.db import models

# Create your models here.
class Projet(models.Model):
    titre = models.CharField(max_length= 50)
    description = models.TextField()
    image_url = models.CharField(max_length=2000)
    
    
class Plat(models.Model):
    nom = models.CharField(max_length= 100)
    description = models.TextField()
    url = models.CharField(max_length=2000)
    image= models.CharField(max_length=2000)
    
class Menu(models.Model):
    nom = models.CharField(max_length= 100)
    description = models.TextField()
    url = models.CharField(max_length=2000)
    image = models.CharField(max_length=2000)
    
class Restaurant(models.Model):
    nom = models.CharField(max_length= 100)
    description = models.TextField()
    url = models.CharField(max_length=2000)
    image= models.CharField(max_length=2000)