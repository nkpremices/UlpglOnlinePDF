from django import forms
from .models import Livre

from .models import Livre, Categorie

class Auth(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    #fichier = forms.FileField()

class Livre_upload_form(forms.ModelForm):
    class Meta:
        model = Livre
        fields = (
            'categorie',
            'titre',
            'auteur',
            'resume',
            'pdf',
            'cover'

        )