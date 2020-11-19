/* JS functions file */

function indexQuery() {
    
    name = document.getElementById("name").value
    gradyear = document.getElementById("gradyear").value
    
    resultat = "Vous avez lancé une requête avec les paramètres suivants :\n";
    resultat += "[nom : '" + name + "' | promo : '" + gradyear + "']";
    
    alert(resultat);
}


function studentQuery() {
    
    fname = document.getElementById("s_fname").value
    lname = document.getElementById("s_lname").value
    gradyear = document.getElementById("s_gradyear").value
    
    resultat = "Vous avez créé un étudiant dans la base :\n";
    resultat += fname + " " + lname + " -- promo(" + gradyear + ")";
    
    alert(resultat);
}


function cityQuery() {
    
    city = document.getElementById("c_city").value
    country = document.getElementById("c_country").value
    lon = document.getElementById("c_lon").value
    lat = document.getElementById("c_lat").value
    
    resultat = "Vous avez créé une ville dans la base :\n";
    resultat += city + ", " + country + " -- coord(" + lon + " , " + lat + ")";
    
    alert(resultat);
}


function internshipQuery() {
    
    fname = document.getElementById("i_fname").value
    lname = document.getElementById("i_lname").value
    gradyear = document.getElementById("i_gradyear").value
    city = document.getElementById("i_city").value
    country = document.getElementById("i_country").value
    start = document.getElementById("i_start_date").value
    end = document.getElementById("i_end_date").value
    
    resultat = "Vous avez créé un stage dans la base :\n";
    resultat += "DE " + fname + " " + lname + " -- promo(" + gradyear + ")\n"
    resultat += "A " + city + ", " + country + "\n"
    resultat += "ENTRE " + start + " ET " + end;
    
    alert(resultat);
}



