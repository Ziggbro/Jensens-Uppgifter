
from bilar_classer import * 
import math

    


print("beskriv din bil")
färg = input("vilken färg har den?")
märke = input("vilket märke är det?")
form =  input("vilken form har den?")
år =  input("vilken års moddel är det?")
bränsle = input("vilken typ av bränsle går dem på ?")


bil = Bil(färg,märke,form,år,bränsle)

print(f"\nFordonsinformation:\n")
print(f"")

