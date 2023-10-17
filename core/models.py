from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta():
        ordering = ['concluida']
