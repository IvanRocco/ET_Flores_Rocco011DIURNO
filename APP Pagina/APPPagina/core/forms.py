from django import forms
from django.forms import ModelForm
from .models import Beat

class BeatForm(forms.ModelForm):
    class Meta:
        model= Beat
        fields= ['idBeat','nombreBeat','descripcion','nombreColab','precioBeat','imgenBeat']
        labels={
            'idBeat' : 'idBeat',
            'nombreBeat' : 'nombreBeat',
            'descripcion' : 'descripcion',
            'nombreColab' : 'nombreColab',
            'precioBeat' : 'precioBeat',
            'imgenBeat': 'imgenBeat'
            
        }
        widgets={
            'idBeat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID',
                    'id': 'id'
                }
            ),
            'nombreBeat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Pista',
                    'id': 'nombre'
                }
            ),'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion',
                    'id': 'descripcion'
                }
            ),
            'nombreColab': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre colab',
                    'id': 'id'
                }
            ),'precioBeat': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Precio',
                    'id': 'precio'
                }
            ),'imgenBeat': forms.FileInput()
            ,
            
        }