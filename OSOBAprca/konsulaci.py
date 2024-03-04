from osoba import Osoba
class Konsultanci(Osoba):
    def __init__(self, _imie, _wiek, _rady_zakres):
        super().__init__(_imie, _wiek)
        self.rady_zakres = _rady_zakres

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Daje rady w zakresie {self.rady_zakres}"