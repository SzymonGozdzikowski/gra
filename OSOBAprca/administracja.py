from osoba import Osoba
class Administracja(Osoba):
    def __init__(self, _imie, _wiek, _rola):
        super().__init__(_imie, _wiek)
        self.rola = _rola

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Zajmuje się {self.rola}"