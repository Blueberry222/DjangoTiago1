from django.db import models
from django.utils import timezone # Usar timezone
from django.contrib.auth.models import User # Utilizar o sistema de usuários do Django

class Post(models.Model):
    # Atributos (campos)
    # campo de texto com tamanho maximo
    titulo = models.CharField(max_length=300)
    # autor como uma chave estrangeira.
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # campo de texto maiores
    conteudo = models.TextField()
    # data de criação do post
    data = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        ordering = ['-data']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

# Create your models here.
