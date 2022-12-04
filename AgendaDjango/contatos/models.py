from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=True)
    Data_de_Criação = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%D')

    def __str__(self):
        return self.nome



