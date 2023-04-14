window.onload = function() {
    if(window.innerHeight > window.innerWidth){
        document.getElementById("centre").style.fontSize = "clamp(3vw, 4vw, 5vw)";
        document.getElementById("titre").style.height = "clamp(15vw, 17.5vw, 20vw)";
        document.getElementById("titre").style.fontSize = "clamp(15vw, 17.5vw, 20vw)";
        document.getElementById("home_button").style.width = "48px";
        document.getElementById("home_button").style.height = "48px";
        document.getElementById("logo").style.width = "48px";
    }
}