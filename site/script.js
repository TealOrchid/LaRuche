let overlay, open, close;

window.onload = function() {
  overlay = document.querySelector("#menu");
  open = document.querySelector("#open");
  open.addEventListener("click", function() {overlay.style.transform = "translateY(0)";}, false);
  close = document.querySelector("#close");
  close.addEventListener("click", function() {overlay.style.transform = "translateY(-110%)";}, false);
}