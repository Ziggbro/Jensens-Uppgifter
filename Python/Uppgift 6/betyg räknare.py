
poäng = int(input("skriv dina poäng, mellan 0-100"))



poäng = int(input("Skriv dina poäng, mellan 0-100: "))
if 0 <= poäng < 50:
    print("Ej godkänd")
elif 50 <= poäng < 60:
    print("Ditt betyg blir: E")
elif 60 <= poäng < 70:
    print("Ditt betyg blir: D")
elif 70 <= poäng < 80:
    print("Ditt betyg blir: C")
elif 80 <= poäng < 90:
    print("Ditt betyg blir: B")
elif 90 <= poäng <= 100:
    print("Ditt betyg blir: A")
else:
    print("Ange ett tal mellan 0 och 100")