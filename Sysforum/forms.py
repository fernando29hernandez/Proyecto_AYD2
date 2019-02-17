from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe

from django.forms import ModelForm, Textarea, TextInput, URLInput, PasswordInput, EmailInput
from Sysforum.models import *



class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = ['Titulo', 'Descripcion']
        widgets = {
            'titulo': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
            
        }
        labels={
            'titulo': 'Nombre',
            'descripcion': 'Descripcion',
        }