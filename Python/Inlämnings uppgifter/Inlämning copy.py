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
happiness = true
val = ("sten","sax","påse")
#spelare = None
#dator = random.choice(val)

#print welcome messege
print("Let's play a game")
#print("Please pick wich one.")
#wichgame = int(print("1:   sten saxs påse \n 2: Tärning \n 3: Something else"))
#hopefully invokes first choice to start another function
def gameStart():
    if input("1"):
        print("du har valt sten sax påse")
        tresome()
    else:
        print("game machine broken, pick another")
        
#sten sax påse spel typ
def tresome():
    while happiness:
        spelare = None
        dator = random.choice(val)

        while spelare not in val:
            spelare = input("välj sten sax eller påse")
        else :
            print("välj ett riktigt val")

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
    
    if not input("Play again? (y/n): ").lower() == "y":
        happiness = False