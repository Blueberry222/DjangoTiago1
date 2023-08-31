from django.db import models
from django.utils import timezone # Usar timezone


# Create your models here.
class Celular(models.Model):

    # campo de texto com tamanho maximo
    modelo = models.CharField(max_length=300)
    marca = models.CharField(max_length=300)
    data = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.modelo
    
    class Meta:
        ordering = ['-data']
        verbose_name = "Celular"
        verbose_name_plural = "Celulares"