
from django import forms


class Tag_Form(forms.Form):
    tag = forms.CharField(label="Nom du tag", max_length=100)

class Unit_Form(forms.Form):
    name = forms.CharField(label="Nom de l'unité", max_length=100)