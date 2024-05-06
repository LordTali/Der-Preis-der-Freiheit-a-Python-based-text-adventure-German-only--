from main import random
class Waffe:
    def __init__(self, name, typ, gattung, gewicht, reichweite, angriffsbonus, toedlichkeit, schaden, schadensart, besonderheit, haltung, belastung, verteidigungsmalus, angriffsmalus):
        self.name = name
        self.typ = typ
        self.gattung = gattung
        self.gewicht = gewicht
        self.gattung = gattung
        self.reichweite = reichweite
        self.angriffsbonus = angriffsbonus
        self.schaden = schaden
        self.schadensart = schadensart
        self.besonderheit = besonderheit
        self.haltung = haltung
        self.belastung = belastung
        self.verteidigungsmalus = verteidigungsmalus
        self.toedlichkeit = toedlichkeit
        self.angriffsmalus = angriffsmalus



class Schwerter (Waffe):
    def __init__(self, name, typ, gattung, gewicht, reichweite, angriffsbonus, toedlichkeit, schaden, schadensart, besonderheit, haltung, belastung, verteidigungsmalus, angriffsmalus):
        self.name = name
        self.typ = typ
        self.gattung = "Schwerter"
        self.gewicht = gewicht
        self.haltung = 1 or 2
        self.schaden = schaden
        self.belastung = belastung
        self.besonderheit = None
        self.verteidigungsmalus = verteidigungsmalus
        self.toedlichkeit = toedlichkeit
        self.angriffsmalus = angriffsmalus

class Aexte (Waffe):
    def __init__(self, name, typ, gattung, gewicht, reichweite, angriffsbonus, toedlichkeit, schaden, schadensart, besonderheit, haltung,
                 belastung, verteidigungsmalus, angriffsmalus):
        self.gattung = "Äxte"
        self.typ = typ
        self.gewicht = gewicht
        self.haltung = 1 or 2
        self.schaden = schaden
        self.belastung = belastung
        self.besonderheit = "Sperrig"
        self.verteidigungsmalus = verteidigungsmalus
        self.toedlichkeit = toedlichkeit
        self.angriffsmalus = angriffsmalus



kurzschwert = Schwerter("Kurzschwert", "Nahkampf",
                        "Schwerter",
                        str(1) + "kg",
                        1,
                        0, "1W8",
                        random.randint(1,8),
                        "H/S",
                        "kombinierbar",
                        1 or 2,
                        0, 0, 0)

faust = Waffe("Faust", "Nahkampf",
             "unbewaffnet",
             0 ,
             1,
             0, "1W4",
             random.randint(1,4),
             "W",
             "Kombinierbar",
             None,
             0, 0,0)

dolch = Waffe ("Dolch", "Nahkampf",
                "leichte und Wurfwaffen",
                0.6,
                1,
                0, "1W6",
                random.randint(1,6),
                "S",
                "fernkampftauglich",
                1,
                0, 0,0)

zweihaendige_axt = Aexte ("Zweihändige Axt", "Nahkampf",
                           "Äxte",
                           3,
                           1,
                           0, "2W12",
                           int(random.randint(1,12)+random.randint(1,12)),
                           "H",
                           "sperrig",
                           2,
                           2,
                          2,2)
