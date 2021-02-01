from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnnuaireForm, EtudiantForm, VilleForm, StageForm
from .models import Gradyear, Student, Country, City, Internship

def annuaire(request):
    if request.method == 'GET':
        # create a form instance and populate it
        form = AnnuaireForm(request.GET)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # return HttpResponse
            return render(request, 'annuaire.html', {'form': form})

    else:
        form = AnnuaireForm()

    return render(request, 'annuaire.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def etudiant(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = EtudiantForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            prenom = form.cleaned_data['nom']
            nom = form.cleaned_data['prenom']
            try :
                annee = Gradyear.objects.get(label = form.cleaned_data['annee'] )
            except Gradyear.DoesNotExist :
                annee = Gradyear(label = form.cleaned_data['annee'])
                annee.save()
            newStudent = Student(fname = prenom, lname=nom, gradyear_id = annee)
            newStudent.save()           
            return HttpResponse(f'<h1>new Student : {nom} </h1>')  
    else:
        form = EtudiantForm()

    return render(request, 'etudiant.html', {'form': form})


def ville(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = VilleForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # return HttpResponse
            return render(request, 'ville.html', {'form': form})

    else:
        form = VilleForm()

    return render(request, 'ville.html', {'form': form})


def stage(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = StageForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # return HttpResponse
            return render(request, 'stage.html', {'form': form})

    else:
        form = StageForm()

    return render(request, 'stage.html', {'form': form})


### END OF FILE ###
