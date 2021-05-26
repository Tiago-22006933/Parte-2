from django import forms
from django.forms import ModelForm, EmailField

from .models import Contacto, Comentario

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