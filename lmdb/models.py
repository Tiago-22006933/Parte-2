from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Contacto(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Comentario(models.Model):
    clareza = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    rigor = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    precisão = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    profundidade = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    amplitude = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    lógica = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    significância = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    originalidade = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    globalidade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    comentário = models.CharField(max_length=500, default="Sem comentário")

    def __str__(self):
        return 'Comentário'

class Streaming(models.Model):
    nome = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, default='Generalista')
    imagem = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome

class Filme(models.Model):
    pass

class Actor(models.Model):
    pass

class Realizador(models.Model):
    pass