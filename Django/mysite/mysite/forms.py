from django.core.validators import RegexValidator
from django import forms

letters = RegexValidator(r'^[a-zA-Z ]*$', 'Saisissez un nom valide')
digits = RegexValidator(r'^\-?(\d+\.)?\d+$', 'Saisissez une coordonnée valide')
year = RegexValidator(r'^\d{4}$', 'Saisissez une année valide (AAAA)')


class AnnuaireForm(forms.Form):
    # global search form
    nom = forms.CharField(label = 'Nom / Prénom', required = False, max_length = 100, validators = [letters])
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
    # redefine constructor
    def __init__(self, student_list, city_list, *args, **kwargs):
        # call parent
        super().__init__(*args, **kwargs)
        
        # internship insertion form
        self.fields['etudiant'] = forms.CharField(label = 'Etudiant', widget = forms.Select(choices = student_list))
        self.fields['ville'] = forms.CharField(label = 'Ville', widget = forms.Select(choices = city_list))
        self.fields['debut'] = forms.DateField(label = 'Date de début')
        self.fields['fin'] = forms.DateField(label = 'Date de fin')


### END OF FILE ###
