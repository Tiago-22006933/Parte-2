from django import forms
from django.forms import ModelForm, EmailField

from .models import Contacto, Comentario, Realizador, Actor, Filme

class NovoContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class NovoComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        widgets = {'clareza': forms.HiddenInput(),
                   'rigor': forms.HiddenInput(),
                   'precisão': forms.HiddenInput(),
                   'profundidade': forms.HiddenInput(),
                   'amplitude': forms.HiddenInput(),
                   'lógica': forms.HiddenInput(),
                   'significância': forms.HiddenInput(),
                   'originalidade': forms.HiddenInput(),
                   'globalidade': forms.HiddenInput(),
                   'comentário': forms.HiddenInput()}

class NovoRealizadorForm(ModelForm):
    class Meta:
        model = Realizador
        fields = '__all__'

class NovoActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

class NovoFilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {'nome': forms.HiddenInput(),
                   'data_lancamento': forms.HiddenInput(),
                   'genero': forms.HiddenInput(),
                   'realizador': forms.HiddenInput(),
                   'actores': forms.HiddenInput(),
                   'capa': forms.HiddenInput(),
                   }