
class Leerplanonderdeel:
    def init(self):
        self.nummer = ""
        self.omschrijving = ""
    
    def getInsertCommand(self):
        if self.table:
            return f'INSERT INTO {self.table} VALUES("{self.nummer}", "{self.omschrijving}");'
        else:
            return None


class Competentie(Leerplanonderdeel):
    table = "Competenties"


class Deelcompetentie(Leerplanonderdeel):
    table = "Deelcompetenties"
    
    def init(self):
        self.competentie = ""

    def getInsertCommand(self):
        if self.table:
            return f'INSERT INTO {self.table} VALUES("{self.nummer}", "{self.omschrijving}", "{self.competentie}");'
        else:
            return None


class Leerplandoel(Leerplanonderdeel):
    table = "Leerplandoelen"
    
    def init(self):
        self.competentie = ""
        self.deelcompetentie = ""

    def getInsertCommand(self):
        if self.table:
            return f'INSERT INTO {self.table} VALUES("{self.nummer}", "{self.omschrijving}", "{self.competentie}", "{self.deelcompetentie}");'
        else:
            return None
