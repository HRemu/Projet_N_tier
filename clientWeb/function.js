/* JS functions file */
/* WARNING: ces fonctions ne testent QUE la syntaxe, pas la cohérence */


function checkNom(nom) {
    return /(^[A-Za-z]+([- ]?[A-Za-z]+){1,2}$)/.test(nom);
}


function checkPromo(promo) {
    return /(^[0-9]{4}$)/.test(promo);
}


function checkCoord(coord) {
    return /(^[-]?[0-9]+([.][0-9]+)?$)/.test(coord);
}


function checkDate(date) {
    return /(^([0-9]{2}[/]){2}[0-9]{4}$)/.test(date);
}


function requete(domaine) {
    
    if (domaine == 'annuaire') {
        
        nom = document.getElementById("name").value
        promo = document.getElementById("gradyear").value
        
        nomOK = checkNom(nom) ? "OK" : "Not OK";
        promoOK = checkPromo(promo) ? "OK" : "Not OK";
        
        resultat  = "Check nom (" + nom + ") : " + nomOK + "\n";
        resultat += "Check promotion ("  + promo + ") : " + promoOK;
        
        alert(resultat);
    }
    
    else if (domaine == 'etudiant') {
        
        prenom = document.getElementById("fname").value
        nom = document.getElementById("lname").value
        promo = document.getElementById("gradyear").value
        
        prenomOK = checkNom(prenom) ? "OK" : "Not OK";
        nomOK = checkNom(nom) ? "OK" : "Not OK";
        promoOK = checkPromo(promo) ? "OK" : "Not OK";
        
        resultat  = "Check prénom (" + prenom + ") : " + prenomOK + "\n";
        resultat += "Check nom (" + nom + ") : " + nomOK + "\n";
        resultat += "Check promotion ("  + promo + ") : " + promoOK;
        
        alert(resultat);
    }
    
    else if (domaine == 'ville') {
        
        ville = document.getElementById("city").value
        pays = document.getElementById("country").value
        lon = document.getElementById("lon").value
        lat = document.getElementById("lat").value
        
        villeOK = checkNom(ville) ? "OK" : "Not OK";
        paysOK = checkNom(pays) ? "OK" : "Not OK";
        lonOK = checkCoord(lon) ? "OK" : "Not OK";
        latOK = checkCoord(lat) ? "OK" : "Not OK";
        
        resultat  = "Check ville (" + ville + ") : " + villeOK + "\n";
        resultat += "Check pays (" + pays + ") : " + paysOK + "\n";
        resultat += "Check longitude (" + lon + ") : " + lonOK + "\n";
        resultat += "Check latitude (" + lat + ") : " + latOK;
        
        alert(resultat);
    }
    
    else if (domaine == 'stage') {
        
        prenom = document.getElementById("fname").value
        nom = document.getElementById("lname").value
        promo = document.getElementById("gradyear").value
        ville = document.getElementById("city").value
        pays = document.getElementById("country").value
        debut = document.getElementById("start_date").value
        fin = document.getElementById("end_date").value
        
        prenomOK = checkNom(prenom) ? "OK" : "Not OK";
        nomOK = checkNom(nom) ? "OK" : "Not OK";
        promoOK = checkPromo(promo) ? "OK" : "Not OK";
        villeOK = checkNom(ville) ? "OK" : "Not OK";
        paysOK = checkNom(pays) ? "OK" : "Not OK";
        debutOK = checkDate(debut) ? "OK" : "Not OK";
        finOK = checkDate(fin) ? "OK" : "Not OK";
        
        resultat  = "Check prénom (" + prenom + ") : " + prenomOK + "\n";
        resultat += "Check nom (" + nom + ") : " + nomOK + "\n";
        resultat += "Check promotion ("  + promo + ") : " + promoOK + "\n";
        resultat += "Check ville (" + ville + ") : " + villeOK + "\n";
        resultat += "Check pays (" + pays + ") : " + paysOK + "\n";
        resultat += "Check date début (" + debut + ") : " + debutOK + "\n";
        resultat += "Check date fin (" + fin + ") : " + finOK;
        
        alert(resultat);
    }
}



