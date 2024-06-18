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

options = ("sten", "sax", "påse")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Välj sten sax eller påse:): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

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

    if not input("Vill du spela igen? (j/n): ").lower() == "j":
        running = False

print("Thanks for playing!")

