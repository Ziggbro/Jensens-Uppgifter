class Fordon:
    def __init__(self,färg,märke,form,år,bränsle):
        self.self = self
        self.färg = färg
        self.märke = märke
        self.form = form
        self.år = år
        self.bränsle = bränsle

        
class Bil(Fordon):
    def __init__(self, färg, märke, form, år, bränsle):
        super().__init__(färg, märke, form, år, bränsle)
        return bil.visa_info()