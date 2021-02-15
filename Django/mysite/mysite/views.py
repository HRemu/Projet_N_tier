from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .forms import AnnuaireForm, EtudiantForm, VilleForm, StageForm
from .models import Gradyear, Student, Country, City, Internship


def index(request):
    # TODO: faire une requete sur les stages pour plotter les villes de stage sur la worldmap
    return render(request, 'index.html')


def annuaire(request):
    if request.method == 'GET':
        # create a form instance and populate it
        form = AnnuaireForm(request.GET)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            nom = form.cleaned_data['nom'].upper()
            annee = form.cleaned_data['annee']
            
            # make query to get students
            try:
                if annee != "":
                    try:
                        yearId = Gradyear.objects.get(label = annee)
                    
                    except:
                        return render(request, 'annuaire.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: no matching gradyear in database.'})
                    
                    students = Student.objects.filter(Q(fname__contains = nom, gradyear_id = yearId) | Q(lname__contains = nom, gradyear_id = yearId))
                
                else:
                    students = Student.objects.filter(Q(fname__contains = nom) | Q(lname__contains = nom))
            
            except Student.DoesNotExist:
                students = []
            
            # create HttpResponse
            header = 'Query OK: ' + str(len(students)) + ' student(s) found in the database.'
            
            # return HttpResponse
            return render(request, 'annuaire.html', {'form': AnnuaireForm(), 'css': "good-query", 'response': header, 'elements': students})

    else:
        form = AnnuaireForm()

    return render(request, 'annuaire.html', {'form': form})


def etudiant(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = EtudiantForm(request.POST)

        if form.is_valid():
            # get the data from cleaned_data as required
            prenom = form.cleaned_data['prenom'].upper()
            nom = form.cleaned_data['nom'].upper()
            email = form.cleaned_data['email']
            annee = form.cleaned_data['annee']
            
            # create the gradyear if it does not exist
            try:
                newYear = Gradyear.objects.get(label = annee)
            
            except Gradyear.DoesNotExist:
                newYear = Gradyear(label = annee)
                newYear.save()
            
            # create the student if it does not exist
            try:
                newStudent = Student.objects.get(email = email)
            
            except Student.DoesNotExist:
                newStudent = Student(fname = prenom, lname = nom, email = email, gradyear_id = newYear)
                newStudent.save()
                return render(request, 'etudiant.html', {'form': EtudiantForm(), 'css': "good-query", 'response': 'Query OK: student added to database.'})
            
            return render(request, 'etudiant.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: matching student found in database.'})
    
    else:
        form = EtudiantForm()
    
    return render(request, 'etudiant.html', {'form': form})


def ville(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = VilleForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            ville = form.cleaned_data['ville'].upper()
            pays = form.cleaned_data['pays'].upper()
            longitude = form.cleaned_data['long']
            latitude = form.cleaned_data['lat']
            
            # create the country if it does not exist
            try:
                newCountry = Country.objects.get(country_name = pays)
            
            except Country.DoesNotExist:
                newCountry = Country(country_name = pays)
                newCountry.save()
            
            # create the city if it does not exist
            try:
                newCity = City.objects.get(city_name = ville, country_id = newCountry)
            
            except City.DoesNotExist:
                newCity = City(city_name = ville, longitude = longitude, latitude = latitude, country_id = newCountry)
                newCity.save()
                return render(request, 'ville.html', {'form': VilleForm(), 'css': "good-query", 'response': 'Query OK: city added to database.'})
            
            return render(request, 'ville.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: matching city found in database.'})

    else:
        form = VilleForm()

    return render(request, 'ville.html', {'form': form})


def stage(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = StageForm(request.POST)

        if form.is_valid():
            # useless - just for good look
            prenom = form.cleaned_data['prenom'].upper()
            nom = form.cleaned_data['nom'].upper()
            
            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']
            ville = form.cleaned_data['ville'].upper()
            pays = form.cleaned_data['pays'].upper()
            debut = form.cleaned_data['debut']
            fin = form.cleaned_data['fin']
            
            # date boolean condition check
            if debut < fin:
                
                # get student id
                try:
                    student = Student.objects.get(email = email)
                
                except Student.DoesNotExist:
                    return render(request, 'stage.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: no matching student in database.'})
                
                # get country id
                try:
                    country = Country.objects.get(country_name = pays)
                
                except Country.DoesNotExist:
                    return render(request, 'stage.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: no matching country in database.'})
                
                # get city id
                try:
                    city = City.objects.get(city_name = ville, country_id = country)
                
                except City.DoesNotExist:
                    return render(request, 'stage.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: no matching city in database.'})
                
                # create internship
                try:
                    newInternship = Internship.objects.get(student_id = student, city_id = city, date_start = debut, date_end = fin)
                
                except Internship.DoesNotExist:
                    newInternship = Internship(student_id = student, city_id = city, date_start = debut, date_end = fin)
                    newInternship.save()
                    return render(request, 'stage.html', {'form': form, 'css': "good-query", 'response': 'Query OK: internship added to database.'})
                
                return render(request, 'stage.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: unicity constraint.'})
            
            else:
                return render(request, 'stage.html', {'form': form, 'css': "bad-query", 'response': 'Query failed: did you invert your start and end dates?'})
    
    else:
        form = StageForm()

    return render(request, 'stage.html', {'form': form})


### END OF FILE ###
