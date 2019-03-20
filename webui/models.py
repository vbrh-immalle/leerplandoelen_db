class Leerplanonderdeel:
    def init(self):
        self.nummer = ""
        self.omschrijving = ""


class Competentie(Leerplanonderdeel):
    pass


class Deelcompetentie(Leerplanonderdeel):
    def init(self):
        self.competentie = ""


class Leerplandoel(Leerplanonderdeel):
    def init(self):
        self.competentie = ""
        self.deelcompetentie = ""
