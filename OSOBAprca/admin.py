from IT import IT
class Admin(IT):
    def __init__(self, _imie, _wiek, _umiejetnosci):
        super().__init__(_imie, _wiek, _umiejetnosci)
        

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Zajmuje sie {self.umiejetnosci}"
    
