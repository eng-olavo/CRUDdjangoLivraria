from django.db import models

# Create your models here.

class Lib(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    resumo = models.TextField(max_length=255)
    autor = models.CharField(max_length=100)
    