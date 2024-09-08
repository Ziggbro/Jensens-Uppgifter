

""" def hälsa (namn):
    
    medelande = "hej, " + namn + "! Välkommen!"
    return medelande


resultat = hälsa("anna")

print(resultat)
 """


def List(lista):
    nyLista = []
    for element in lista:
        nyttElement = pow(element,2)
        nyLista.append(nyttElement)
    return nyLista
    
print(List([2,4,5,6,7,10]))



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





