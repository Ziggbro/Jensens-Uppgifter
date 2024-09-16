

class Djur():
    def __init__(self,name,ålder):
        self.name = name
        self.ålder = ålder
    
    def äta(self):
        print(f"{self.name} äter")

    def sova(self):
        print(f"{self.name} sover")

    def göra_ljud(self):
        print(f"{self.name} gör ljud")


class Hund(Djur):
    def __init__(self, name, ålder, ras):
        super().__init__(name, ålder)
        self.ras = ras 
    def skälla(self):
        print(f"{self.name} skäller")
    def göra_ljud(self):
        self.skälla()

    def visa_ras(self):
        print(f"{self.name}, är av rasen {self.ras}.")


