class Osoba:
    def __init__(self,_imie,_wiek):
        self.imie = _imie
        self.wiek = _wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie}, mam {self.wiek} lat"
    

