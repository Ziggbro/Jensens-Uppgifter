





# fil = open("d:\python.txt", "a")
# fil.write("I like Python")
# fil.close()

# # Öppna och läs filen efter tillägget:
# fil = open("d:\python.txt", "r")
# print(fil.read())
# fil.close()
import os

# fil = open("Python\Python 2\python.txt", "a")
# fil.write(" I like webdev")
# fil.close()

# fil = open("python.txt ","r")
# print(fil.read())
# fil.close()

# fil = open("Python\Python 2\listname.txt","a")
# fil.write("namn1")
# fil.write("name2")
# fil.write("\n name3")
# fil.close()

# fil = open("Python\Python 2\listname.txt","r")
# print(fil.read())


# with open("Python\Python 2\listname.txt") as file:
#     for line in file:
#         line = line.strip()
#         print("hej, ", line, "trevlig helg")

# fil.close()

import os
import os.path
deltagare = ['Samer', 'Olivia', 'Ove','Sara']

os.path.isfile("Python\Python 2\my_friends\exaple.txt")

# if os.path.exists('Python\Python 2\my_friends'):
#     os.remove("Python\Python 2\my_friends\exaple.txt")
#     os.rmdir("Python\Pyton 2\my_friends")
#     print("filen har tagits ort")
# else:
#     print("gay")

if not os.path.exists('Python\Pyton 2\my_friends'):
    os.makedirs('Python\Python 2\my_friends')


with open('Python\Python 2\my_friends\exaple.txt', 'w',) as fil:
    for y in deltagare:
        fil.write('Hej '+ y + '!\n')
        fil.close()
    




