from administracja import Administracja
class Ksiegowosc(Administracja):
    def __init__(self, _imie, _wiek, _rola):
        super().__init__(_imie, _wiek, _rola)

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Zajmuje się {self.rola}"