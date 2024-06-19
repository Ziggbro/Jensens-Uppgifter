"""""
måste innehålla
-Variabler
-Input-kommando
-En eller flera print-satser
-for- eller while-slingor
-If-satser
-Functions (Alernativ)
"""
#importerar random bibloteket
import random
#variabler som är bra att ha
options = ("sten", "sax", "påse")
running = True
#main while loopen
while running:
    #variabler som sparar spelarens val
    player = None
    computer = random.choice(options)
    #kollar att du valt ett av dom tillgengliga valen. så du inte fuskar.
    while player not in options:
        player = input("Välj sten sax eller påse:): ")

    print(f"Spelare: {player}")
    print(f"Datorn: {computer}")
    #vinst räkningen
    if player == computer:
        print("Det blev oavgjort!")
    elif player == "sten" and computer == "sax":
        print("Du winner!")
    elif player == "papper" and computer == "sten":
        print("Du winner!")
    elif player == "sax" and computer == "påse":
        print("Du winner!")
    else:
        print("Du förlorade!")
    #stannar loopen så den inte körs för evigt
    if not input("Vill du spela igen? (j/n): ").lower() == "j":
        running = False
#goodbye medelande
print("Thanks for playing!")

