/* JS functions file */

function validateFormOnSubmit() {
    
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    gradyear = document.getElementById("gradyear").value
    city = document.getElementById("city").value
    country = document.getElementById("country").value
    start_date = document.getElementById("start_date").value
    end_date = document.getElementById("end_date").value
    
    d1 = new Date(start_date)
    d2 = new Date(end_date)
    
    resultat = "";
    if (d1 < d2) {
        resultat += "Prénom : " + fname + "\n";
        resultat += "Nom : " + lname + "\n";
        resultat += "Promotion : " + gradyear + "\n";
        resultat += "Ville : " + city + "\n";
        resultat += "Pays : " + country + "\n";
        resultat += "Début : " + start_date + "\n";
        resultat += "Fin : " + end_date;
    }
    else {
        resultat += "Erreur comparaison dates";
    }
    
    alert(resultat);
}


