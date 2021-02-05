from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnnuaireForm, EtudiantForm, VilleForm, StageForm
from .models import Gradyear, Student, Country, City, Internship

# WHERE ... OR ... condition requests
from django.db.models import Q


def index(request):
    # TODO: faire une requete sur les stages pour
    # plotter les villes de stage sur la worldmap
    return render(request, 'index.html')


def annuaire(request):
    if request.method == 'GET':
        # create a form instance and populate it
        form = AnnuaireForm(request.GET)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            nom = form.cleaned_data['nom']
            annee = form.cleaned_data['annee']
            
            # make query to get students
            try:
                if annee != "":
                    try:
                        yearId = Gradyear.objects.get(label = annee)
                    
                    except:
                        return HttpResponse(f'<p>Query failed: no matching gradyear ID</p>')
                    
                    students = Student.objects.filter(Q(fname__contains = nom, gradyear_id = yearId) | Q(lname__contains = nom, gradyear_id = yearId))
                
                else:
                    students = Student.objects.filter(Q(fname__contains = nom) | Q(lname__contains = nom))
            
            except Student.DoesNotExist:
                return HttpResponse(f'<p>Query OK: 0 students found in database</p>')
            
            # create HttpResponse
            content = '<p>Query OK: ' + str(len(students)) + ' students found in database.</p><ul>'
            
            for i in range(len(students)):
                # get student data
                student_id, fname, lname = students[i].student_id, students[i].fname, students[i].lname
                
                # add <li> element
                content += '<li>' + lname.upper() + ' ' + fname.lower() + ' (' + str(student_id) + ')</li>'
            
            content += '</ul>'
            
            # return HttpResponse
            return HttpResponse(content)

    else:
        form = AnnuaireForm()

    return render(request, 'annuaire.html', {'form': form})


def etudiant(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = EtudiantForm(request.POST)

        if form.is_valid():
            # get the data from cleaned_data as required
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
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
                return HttpResponse(f'<p>Query OK: {prenom.lower()} {nom.upper()} added to database.</p>')
            
            return HttpResponse(f'<p>Query failed: mail unicity constraint.</p>')
    
    else:
        form = EtudiantForm()
    
    return render(request, 'etudiant.html', {'form': form})


def ville(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = VilleForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            ville = form.cleaned_data['ville']
            pays = form.cleaned_data['pays']
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
                return HttpResponse(f'<p>Query OK: {ville}, {pays} added to database.</p>')
            
            return HttpResponse(f'<p>Query failed: unicity constraint.</p>')

    else:
        form = VilleForm()

    return render(request, 'ville.html', {'form': form})


def stage(request):
    if request.method == 'POST':
        # create a form instance and populate it
        form = StageForm(request.POST)

        if form.is_valid():
            # useless - just for good look
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            
            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']
            ville = form.cleaned_data['ville']
            pays = form.cleaned_data['pays']
            debut = form.cleaned_data['debut']
            fin = form.cleaned_data['fin']
            
            # date boolean condition check
            if debut < fin:
                
                # get student id
                try:
                    student = Student.objects.get(email = email)
                
                except Student.DoesNotExist:
                    return HttpResponse(f'<p>Query failed: no matching student in database.</p>')
                
                # get country id
                try:
                    country = Country.objects.get(country_name = pays)
                
                except Country.DoesNotExist:
                    return HttpResponse(f'<p>Query failed: no matching country in database.</p>')
                
                # get city id
                try:
                    city = City.objects.get(city_name = ville, country_id = country)
                
                except City.DoesNotExist:
                    return HttpResponse(f'<p>Query failed: no matching city in database.</p>')
                
                # create internship
                try:
                    newInternship = Internship.objects.get(student_id = student, city_id = city, date_start = debut, date_end = fin)
                
                except Internship.DoesNotExist:
                    newInternship = Internship(student_id = student, city_id = city, date_start = debut, date_end = fin)
                    newInternship.save()
                    return HttpResponse(f'<p>Query OK: internship added to database.</p>')
                
                return HttpResponse(f'<p>Query failed: unicity constraint.</p>')
            
            else:
                return HttpResponse(f'<p>Query failed: did you invert your start and end dates?.</p>')
    
    else:
        form = StageForm()

    return render(request, 'stage.html', {'form': form})


### END OF FILE ###
