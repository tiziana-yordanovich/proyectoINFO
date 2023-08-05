from django import forms
from .models import Noticia, Comentario


class NoticiaForm(forms.ModelForm):
   
    class Meta:
        model = Noticia
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_noticia']