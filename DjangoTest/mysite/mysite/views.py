from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def annuaire(request):
    return render(request, 'annuaire.html')

def etudiant(request):
    return render(request, 'etudiant.html')

def ville(request):
    return render(request, 'ville.html')

def stage(request):
    return render(request, 'stage.html')
