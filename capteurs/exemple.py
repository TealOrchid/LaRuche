"""
Pour calibrer ma balance, j'ai d'abord utilisé "1" comme paramètre à hx.set_reference_unit() (ligne 23 du script), puis j'ai placé une masse connue sur le plateau de la balance. J'ai ensuite divisé la mesure affichée par la masse, ce qui m'a donné 382,6, qui est devenu le nouveau paramètre de hx.set_reference_unit().

Par exemple: 

    J'exécute le script avec hx.set_reference_unit(1).
    Lorsque la balance est prête, je place une masse de 200 grammes sur le plateau.
    Le programme affiche 76520.
    Je calcule 76520/200, ce qui donne 382,6.
    J'exécute à nouveau le script, mais avec hx.set_reference_unit(382.6).
    La masse s'affiche correctement en grammes.



"""



import time
import RPi.GPIO as GPIO
from hx711 import HX711

brocheDT = 11   # DT du HX711 branché à GPIO5
brocheSCK = 12  # SCK du HX711 branché à GPIO6

hx = HX711(brocheDT, brocheSCK) 

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(382.6) #calibration: le nombre dépend de votre balance
hx.reset()
hx.tare()
print("La balance est prete a etre utilisee")

while True:

    val = hx.get_weight(5)
    print(round(val,2))
    time.sleep(0.5)
