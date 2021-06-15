from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

# Create your models here.
class Contacto(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=60, default='')
    telefone = models.IntegerField(validators=[MinValueValidator(910000000),MaxValueValidator(969999999)], default='910000000')
    data_nascimento = models.DateField(default=timezone.now)

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
    comentário = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return 'Comentário'

class Streaming(models.Model):
    nome = models.CharField(max_length=30)
    link = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, default='Generalista')
    imagem = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome

class Actor(models.Model):
    nome = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.nome

class Realizador(models.Model):
    nome = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length=30)
    data_lancamento = models.DateField(default=timezone.now)
    codigo = models.CharField(max_length=30, default='tt0000000')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='filmes')
    realizador = models.ForeignKey(Realizador, on_delete=models.CASCADE, related_name='filmes')
    actores = models.ManyToManyField(Actor)
    capa = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome
