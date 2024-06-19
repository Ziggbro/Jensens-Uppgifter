
import math



while True:
    tal = int(input("skriv det tal du vill ha kvadratroten av\n"))
    if tal>20:
        print("Kvadratroten av ",tal, "är ",math.sqrt(tal))
    else:
        print("kvadraten är:", math.pow(tal,2))
