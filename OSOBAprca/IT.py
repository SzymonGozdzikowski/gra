from osoba import Osoba
class IT(Osoba):
    def __init__(self, _imie, _wiek, _umiejetnosci):
        super().__init__(_imie, _wiek)
        self.umiejetnosci = _umiejetnosci

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Pracuje {self.umiejetnosci}"