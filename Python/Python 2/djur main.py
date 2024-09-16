
#importerar alla classer från 
from djur_classer import *

def main():
    djur = Djur("Djuret", 5)
    djur.äta() #object method
    djur.sova()
    djur.göra_ljud()



    hund = Hund("Fido", 3, "Labrador")
    hund.äta()
    hund.sova()
    hund.göra_ljud()
    hund.visa_ras()




main()