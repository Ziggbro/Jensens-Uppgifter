

""" def hälsa (namn):
    
    medelande = "hej, " + namn + "! Välkommen!"
    return medelande


resultat = hälsa("anna")

print(resultat)
 """

""" 
def List(lista):
    nyLista = []
    for element in lista:
        nyttElement = pow(element,2)
        nyLista.append(nyttElement)
    return nyLista
    
print(List([2,4,5,6,7,10]))

 """
""" 
def bokstavsByte(mening):
    v = ""
    for bokstav in mening:
        if bokstav == "Ö":
            v = v + "O"
        elif bokstav == "ö":
            v = v + "o"
        else:
            v = v + bokstav
    return v

print(bokstavsByte("Ön nära östermalm"))
 """


""" 
• Skriv ett program som definierar en funktion som tar en lista med löner som indata
och returnerar medellönen.
• Användaren anger antalet löner att mata in, och programmet beräknar sedan och
visar medel lönen.
"""



import random
from random import randrange










""" 
Extra övning

Definierar en funktion som kontrollerar om användarens gissning matchar det hemliga
numret. Programmet loopar tills användaren gissar rätt och ger feedback under varje
försök.
 """
import random
from random import randrange


numbers = randrange(10)
number = 1
print(numbers)

while True :
    print("Gissa mitt hemliga nummer och vin ett pris!")

    for g in range(1,6):
        gissning = input("vad gissar du på?")
        if gissning == number:
            print("correct!")
            break
            
        else:
            print("fel")
            print(numbers)
        
