
""" Skriv ett Python-program som använder 4 funktioner för att utföra de fyra grundläggande
aritmetiska operationerna: : addition, subtraktion, multiplikation och division. """
""" Miniräknare """

print("Miniräknar application")
print("")
#alla modifiers
def adda(x,y):
    return x + y
def minus(x,y):
    return x - y
def dela(x,y):
    if y == 0:
        return "kys"
    return x/y
def multi(x,y):
    return x * y

while True:
    print("Knappa in dina nummer så börjar vi!")
    mod = input("Vad ska vi räkna idag? \n 1: + \n 2: - \n 3: * \n 4: / \n")
    if mod in ("1","2","3","4"):
        num1 = int(input("Välj första nummret"))
        num2 = int(input("Välj andrfa nummret"))
    if mod == "1":
        print(num1, "+", num2,"=", adda(num1,num2))
    elif mod == "2":
        print(num1, "-", num2,"=", minus(num1,num2))
    elif mod == "3":
        print(num1, "*", num2,"=", dela(num1,num2))
    elif mod == "4":
        print(num1, "/", num2, "=", multi(num1,num2))

    fortjäta = input("Räkna mer? Y / N")
    if fortjäta.upper() == "N":
        break
