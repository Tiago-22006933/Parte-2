from django.contrib import admin
from .models import Contacto, Comentario, Streaming, Genero, Realizador, Actor, Filme

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Comentario)
admin.site.register(Streaming)
admin.site.register(Genero)
admin.site.register(Realizador)
admin.site.register(Actor)
admin.site.register(Filme)