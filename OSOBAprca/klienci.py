from osoba import Osoba
class Klienci(Osoba):
    def __init__(self, _imie, _wiek, _miejsce_zamieszkania):
        super().__init__(_imie, _wiek)
        self.miejsce_zamieszkania = _miejsce_zamieszkania

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Mieszkam {self.miejsce_zamieszkania}"