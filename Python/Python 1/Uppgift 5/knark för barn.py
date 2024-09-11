
print("Här får du reda på hur stark dos Patienten behöver.")
while True:
    pick = input("Är patienten ett barn?").lower()
    if pick == "ja" or pick == "j":
        print("Patienten behöver bara 500mg per dag.")
        break
    elif pick == "n" or pick == "nej":
        print("Patienten behöver 700mg per dag.")
        break
    else:
        print("Vi måste veta om du ska få rätt mängd medicine")
        

 