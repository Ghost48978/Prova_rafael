from django.db import models

class Livro(models.Model):
    autor = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    paginas = models.PositiveSmallIntegerField()
    editora = models.CharField(max_length=255)
    imagem = models.CharField(max_length=255)

    def __str__(self):
        return self.autor


class Emprestimo(models.Model):
    autor = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor.autor


