"""""
måste innehålla
-Variabler
-Input-kommando
-En eller flera print-satser
-for- eller while-slingor
-If-satser
-Functions (Alernativ)
"""
import random



val = ("sten","sax","påse")
spelare = None
dator = random.choice(val)


print("Let's play a game")
#print("Please pick wich one.")
#wichgame = int(print("1:   sten saxs påse \n 2: Tärning \n 3: Something else"))
while spelare not in val:
    spelare = input("välj sten sax eller påse")
else :
    print("välj ett riktigt val")
    
print("spelare valde :", spelare)
print("Datorn valde:", dator)

if spelare == spelare:
    print("Ovavgjort")
elif spelare == "sax" and dator == "påse":
    print("du vinner")
elif spelare == "påse" and dator == "sten":
    print("du vinner")
elif spelare == "sten" and dator == "sax":
    print("du vinner")
else:
    print("Du förlorade")
    