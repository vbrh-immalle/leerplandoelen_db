from datetime import datetime

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


class User:
    def init(self):
        self.id = 0
        self.achternaam = ""
        self.voornaam = ""


class Antwoord:
    def init(self):
        self.leerplandoel = Leerplandoel()
        self.inhoud = ""
        self.tijdstip = datetime(1, 1, 1, 0, 0)


class MyObject:
    pass
