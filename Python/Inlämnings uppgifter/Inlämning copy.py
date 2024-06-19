"""""
måste innehålla
-Variabler
-Input-kommando
-En eller flera print-satser
-for- eller while-slingor
-If-satser
-Functions (Alernativ)
"""
#importerar bibliteket för slumpmässiga beräkninar.
import random


#variabler kanske
happiness = True
val = ("sten","sax","påse")
#spelare = None
#dator = random.choice(val)

#print welcome messege
print("Let's play a game")
#print("Please pick wich one.")
wichgame = input("1:    sten saxs påse \n 2:    Tärning \n 3:   Something elsen\n")
#hopefully invokes first choice to start another function


if wichgame("1"):
    print("du har valt sten sax påse")
    rock()
    
else:
    print("game machine broken, pick another")
  
#sten sax påse spel typ
#def tresome():
while happiness:
    spelare = None
    dator = random.choice(val)

    while spelare not in val:
        spelare = input("välj sten sax eller påse\n")
    else :
        print("välj ett riktigt val\n")

    print("spelare valde :", spelare)
    print("Datorn valde:", dator)
    if spelare == dator:
        print("Ovavgjort")
    elif spelare == "sax" and dator == "påse":
        print("du vinner")
    elif spelare == "påse" and dator == "sten":
        print("du vinner")
    elif spelare == "sten" and dator == "sax":
        print("du vinner")
    else:
        print("Du förlorade")
        
    if not input("Vill du spela igen? (j/n): ").lower() == "j":
        happiness = False
    
    print("Trevligt spelande")