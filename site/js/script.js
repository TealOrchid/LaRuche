let overlap, open, close;

function initMap() {
    let ruche = {lat: latitude, lng: longitude};
    let carte = new google.maps.Map(document.getElementById("carte"), {zoom: 15, center: ruche});
    new google.maps.Marker({position: ruche, map: carte, title: "LaRuche"});
}

function date_heure() {
    const date = new Date();
    const tab_jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi","Vendredi", "Samedi"];
    const tab_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
    let heures = String(date.getHours());
    let minutes = String(date.getMinutes());
    document.querySelector("#date").innerHTML = `Aujourd'hui nous sommes le ${tab_jours[date.getDay()]} ${date.getDate()} ${tab_mois[date.getMonth()]} ${date.getFullYear()}.`
    document.querySelector("#heure").innerHTML = `Il est ${heures.length < 2 ? "0"+heures : heures} h ${minutes.length < 2 ? "0"+minutes : minutes}.`
}

window.onload = function() {
    overlap = document.querySelector("#menu");
    open = document.querySelector("#open");
    close = document.querySelector("#close");
    open.addEventListener("click", function() {overlap.style.transform = "translateY(0)";}, false);
    close.addEventListener("click", function() {overlap.style.transform = "translateY(-110%)";}, false);
}