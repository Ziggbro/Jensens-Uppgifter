



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, ålder):
        super().__init__(fname, lname)
        self.ålder = ålder

    def printname(self):
        print(f"Namn: {self.firstname} {self.lastname} \nÅlder: {self.ålder}")


x = Student("Mike", "Olsen", 35)

x.printname()