import folium

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .forms import AnnuaireForm, EtudiantForm, VilleForm, StageForm
from .models import Gradyear, Student, Country, City, Internship


def index(request):
    
    worldMap = folium.Map(location = (30,0) , tiles = 'OpenStreetMap', zoom_start = 2, max_zoom = 2, min_zoom = 2)
    stages = Internship.objects.all()
    
    markers = {}
    for i in range(len(stages)):
        # get internship data
        longitude = stages[i].city_id.longitude
        latitude = stages[i].city_id.latitude
        cityName = stages[i].city_id.city_name
        
        # update 'markers' dictionary
        if cityName not in list(markers.keys()):
            markers[cityName] = [ latitude, longitude, 1 ] # 1 internship in this city
        
        else:
            markers[cityName][2] += 1 # + 1 internship in this city
    
    for name in list(markers.keys()):
        # get data on marker
        data = markers[name]
        
        # draw circle object on map
        folium.CircleMarker(
            location = ( data[0] , data[1] ),
            popup = '<b>' + name + '</b> (' + str(data[2]) + ')',
            radius = 5,
            fill = True,
            color = 'green',
            fillColor = 'green'
        ).add_to(worldMap)
    
    worldMap.save(outfile = 'static/map.html')
    
    return render(request, 'index.html')


def annuaire(request):
    if request.method == 'GET':
        # create a form instance and populate it
        form = AnnuaireForm(request.GET)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            nom = form.cleaned_data['nom'].upper()
            annee = form.cleaned_data['annee']
            
            # empty fields
            if nom == "" and annee == "":
                return render(request, 'annuaire.html', {'form': AnnuaireForm()})
            
            # 'nom' is empty
            elif nom == "":
                try:
                    yearId = Gradyear.objects.get(label = annee)
                
                except:
                    return render(request, 'annuaire.html', {'form': form, 'css': "bad-query", 'response': 'No matching gradyear in database.'})
                
                students = Student.objects.filter(gradyear_id = yearId)
            
            # 'annee' is empty
            elif annee == "":
                students = Student.objects.filter( Q(fname__contains = nom) | Q(lname__contains = nom) )
            
            # both are non-empty
            else:
                try:
                    yearId = Gradyear.objects.get(label = annee)
                
                except:
                    return render(request, 'annuaire.html', {'form': form, 'css': "bad-query", 'response': 'No matching gradyear in database.'})
                
                students = Student.objects.filter( ( Q(fname__contains = nom) | Q(lname__contains = nom) ) & Q(gradyear_id = yearId) )
            
            # create HttpResponse
            header = str(len(students)) + ' student(s) found in the database.'
            
            # return HttpResponse
            return render(request, 'annuaire.html', {'form': AnnuaireForm(), 'css': "good-query", 'response': header, 'elements': students})

    else:
        form = AnnuaireForm()

    return render(request, 'annuaire.html', {'form': form})


def details(request, idStudent):
    # personal data
    etudiant = Student.objects.get(student_id = idStudent)
    
    # internships
    stages = Internship.objects.filter(student_id = idStudent)
    
    return render(request, 'details.html', {'student': etudiant, 'internships': stages})


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
                
                # blank form
                form = EtudiantForm()
                
                return render(request, 'etudiant.html', {'form': form, 'css': "good-query", 'response': 'Student added to database.'})
            
            return render(request, 'etudiant.html', {'form': form, 'css': "bad-query", 'response': 'Matching student found in database.'})
    
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
                
                # blank form
                form = VilleForm()
                
                return render(request, 'ville.html', {'form': form, 'css': "good-query", 'response': 'City added to database.'})
            
            return render(request, 'ville.html', {'form': form, 'css': "bad-query", 'response': 'Matching city found in database.'})

    else:
        form = VilleForm()

    return render(request, 'ville.html', {'form': form})


def stage(request):
    """ requesting Student and City tables for the input lists """
    etudiants = Student.objects.all()
    villes = City.objects.all()
    
    student_list, city_list = [], []
    
    for e in etudiants:
        # get values
        studentId = e.student_id
        studentEmail = e.email
        
        # append to list of values
        student_list += [ ( studentId, studentEmail ) ]
    
    for v in villes:
        # get values
        cityId = v.city_id
        cityName = v.city_name + ' (' + v.country_id.country_name + ')'
        
        # append to list of values
        city_list += [ ( cityId, cityName ) ]
    
    """ manage internship form """
    if request.method == 'POST':
        # create a form instance and populate it
        form = StageForm(student_list, city_list, request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            etudiantId = form.cleaned_data['etudiant']
            villeId = form.cleaned_data['ville']
            debut = form.cleaned_data['debut']
            fin = form.cleaned_data['fin']
            
            # date boolean condition check
            if debut < fin:
                # get student by Id
                etudiant = Student.objects.get(student_id = etudiantId)
                
                # get city by Id
                ville = City.objects.get(city_id = villeId)
                
                # create new internship
                newInternship = Internship(student_id = etudiant, city_id = ville, date_start = debut, date_end = fin)
                newInternship.save()
                
                # blank form
                form = StageForm(student_list, city_list)
                
                return render(request, 'stage.html', {'form': form, 'css': "good-query", 'response': 'Internship added to database.'})
            
            else:
                return render(request, 'stage.html', {'form': form, 'css': "bad-query", 'response': 'Did you invert your start and end dates?'})
    
    else:
        form = StageForm(student_list, city_list)

    return render(request, 'stage.html', {'form': form})


### END OF FILE ###
