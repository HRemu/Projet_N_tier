from django.core.validators import RegexValidator
from django import forms

letters = RegexValidator(r'^[a-zA-Z ]*$', 'Only name characters are allowed.')
digits = RegexValidator(r'^[0-9]{4}$', 'Only valid coordinates are allowed.')
year = RegexValidator(r'^[0-9]{4}$', 'Only a valid year is allowed.')


class AnnuaireForm(forms.Form):
    # global search form
    nom = forms.CharField(label = 'Nom', required = False, max_length = 100, validators = [letters])
    annee = forms.CharField(label = 'Promo', required = False, max_length = 4, validators = [year])


class EtudiantForm(forms.Form):
    # student insertion form
    prenom = forms.CharField(label = 'Prénom', max_length = 100, validators = [letters])
    nom = forms.CharField(label = 'Nom', max_length = 100, validators = [letters])
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
    annee = forms.CharField(label = 'Promo', max_length = 4, validators = [year])
    ville = forms.CharField(label = 'Ville', max_length = 100, validators = [letters])
    pays = forms.CharField(label = 'Pays', max_length = 100, validators = [letters])
    debut = forms.DateField(label = 'Date de début')
    fin = forms.DateField(label = 'Date de fin')


### END OF FILE ###
