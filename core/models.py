from uuid import uuid4

from django.db import models


class Postagem(models.Model):
    postagem_id = models.UUIDField(primary_key=True, default=uuid4,
                                   editable=False)
    titulo = models.CharField(max_length=255)
    texto = models.CharField(max_length=500)
    imagem = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    data_criacao = models.DateField(auto_now_add=True)
    curtidas = models.BooleanField()

    class Meta:
        db_table = "postagens"
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.titulo
