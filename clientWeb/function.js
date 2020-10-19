/* JS functions file */

function validateFormOnSubmit() {
    
    var resultat = "DK likes bananas!\n";
    
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    gradyear = document.getElementById("gradyear").value
    city = document.getElementById("city").value
    country = document.getElementById("country").value
    start_date = document.getElementById("start_date").value
    end_date = document.getElementById("end_date").value
    
    resultat += "Prénom : " + fname + "\n";
    resultat += "Nom : " + lname + "\n";
    resultat += "Promotion : " + gradyear + "\n";
    resultat += "Ville : " + city + "\n";
    resultat += "Pays : " + country + "\n";
    resultat += "Début : " + start_date + "\n";
    resultat += "Fin : " + end_date;
    
    alert(resultat);
}


