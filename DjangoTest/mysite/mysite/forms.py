from django.core.validators import RegexValidator
from django import forms

letters = RegexValidator(r'^[a-zA-Z ]*$', 'Saisissez un nom valide.')
digits = RegexValidator(r'^\-?(\d+\.)?\d+$', 'Saisissez une coordonnée valide.')
year = RegexValidator(r'^\d{4}$', 'Saisissez une année valide.')


class AnnuaireForm(forms.Form):
    # global search form
    nom = forms.CharField(label = 'Nom / Prénom', max_length = 100, validators = [letters])
    annee = forms.CharField(label = 'Promo', required = False, max_length = 4, validators = [year])


class EtudiantForm(forms.Form):
    # student insertion form
    prenom = forms.CharField(label = 'Prénom', max_length = 100, validators = [letters])
    nom = forms.CharField(label = 'Nom', max_length = 100, validators = [letters])
    email = forms.EmailField(label = 'Email', max_length = 100, required = True)
    annee = forms.CharField(label = 'Promo', max_length = 4, validators = [year])


class VilleForm(forms.Form):
    # city insertion form
    ville = forms.CharField(label = 'Ville', max_length = 100, validators = [letters])
    pays = forms.CharField(label = 'Pays', max_length = 100, validators = [letters])
    long = forms.CharField(label = 'Longitude', max_length = 20, validators = [digits])
    lat = forms.CharField(label = 'Latitude', max_length = 20, validators = [digits])


class StageForm(forms.Form):
    # internship insertion form
    prenom = forms.CharField(label = 'Prénom', max_length = 100, validators = [letters])
    nom = forms.CharField(label = 'Nom', max_length = 100, validators = [letters])
    email = forms.EmailField(label = 'Email', max_length = 100, required = True)
    ville = forms.CharField(label = 'Ville', max_length = 100, validators = [letters])
    pays = forms.CharField(label = 'Pays', max_length = 100, validators = [letters])
    debut = forms.DateField(label = 'Date de début')
    fin = forms.DateField(label = 'Date de fin')


### END OF FILE ###
