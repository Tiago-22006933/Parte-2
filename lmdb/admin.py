from django.contrib import admin
from .models import Contacto, Comentario, Streaming

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Comentario)
admin.site.register(Streaming)