import random
from main import Textpause




class Zauber():
    def __init__ (self, name, kontrollwert, erfolgswert, magieart, aufwand_aktion, aufwand_zauberkraft,
                  aufwand_geste, aufwand_stimme, aufwand_material, zauberzweck, toedlichkeit, schaden,
                  schadensart, schadenswuerfel_anzahl, schadenswuerfel_groesse, besonderheit, reichweite,
                  dauer, aufhebung, aufhebungswert, aufhebungsbonus, beschreibung, rettungswurf, rettungswurf_willen,
                  rettungswurf_reflexe, angriffswurf, effekt):
        self.name = name
        self.kontrollwert = kontrollwert
        self.erfolgswert = erfolgswert
        self.magieart = magieart
        self.aufwand_aktion = aufwand_aktion
        self.aufwand_zauberkraft = aufwand_zauberkraft
        self.aufwand_geste = aufwand_geste
        self.aufwand_stimme = aufwand_stimme
        self.aufwand_material = aufwand_material
        self.zauberzweck = zauberzweck
        self.toedlichkeit = toedlichkeit
        self.schadensart = schadensart
        self.schaden = schaden
        self.schadenswuerfel_anzahl = schadenswuerfel_anzahl
        self.schadenswuerfel_groesse = schadenswuerfel_groesse
        self.besonderheit = besonderheit
        self.reichweite = reichweite
        self.dauer = dauer
        self.aufhebung = aufhebung
        self.aufhebungswert = aufhebungswert
        self.aufhebungsbonus = aufhebungsbonus
        self.beschreibung = beschreibung
        self.rettungswurf = rettungswurf
        self.rettungswurf_reflexe = rettungswurf_reflexe
        self.rettungswurf_willen = rettungswurf_willen
        self.angriffswurf = angriffswurf
        self.effekt = effekt

    def Wurf_w4(self):
        wurf = random.randint(1, 4)
        print(f"[Würfel: {(wurf)}]\n")
        return wurf

    def Wurf_w6(self):
        wurf = random.randint(1, 6)
        print(f"[Würfel: {(wurf)}]\n")
        return wurf

    def Wurf_w8(self):
            wurf = random.randint(1, 8)
            print(f"[Würfel: {(wurf)}]\n")
            return wurf
    def Wurf_w10(self):
            wurf = random.randint(1, 10)
            print(f"[Würfel: {(wurf)}]\n")
            return wurf
    def Wurf_w12(self):
            wurf = random.randint(1, 12)
            print(f"[Würfel: {(wurf)}]\n")
            Textpause()
            return wurf

    def Wurf_w20(self):
            wurf = random.randint(1, 20)
            print(f"[Würfel: {(wurf)}]\n")
            Textpause()
            return wurf

    def Schaden_berechnen(self):
        zauberschaden = []
        for wuerfel in range(self.schadenswuerfel_anzahl):
            if self.schadenswuerfel_groesse == 6:
                wurf = self.Wurf_w6()
                Textpause()
            elif self.schadenswuerfel_groesse == 8:
                self.Wurf_w8()
                Textpause()
            elif self.schadenswuerfel_groesse == 10:
                self.Wurf_w10()
                Textpause()
            elif self.schadenswuerfel_groesse == 12:
                self.Wurf_w12()
                Textpause()
            elif self.schadenswuerfel_groesse == 20:
                self.Wurf_w20()
                Textpause()
            else:
                self.Wurf_w4()
                Textpause()
            zauberschaden.append(wurf)
            gesamtschaden = sum(zauberschaden)
            return gesamtschaden



blitz=Zauber("Blitz",
             1,
             4,
             "ätherisch",
             1,
             4,
             True,
             True,
             False,
             "Schaden",
             "3W6 Elektrizitätsschaden",
             0,
             "Elektrizitätsschaden",
             3,
             6,
             "Verwirrung",
             10,
             "einmalig",
             "ja",0, 0,
             "[Du lässt deine Hand nach vorne schnellen, während sich zwischen deinen Fingern elektrische Entladungen bilden. Als du deine Hand auf den Gegner richtest, wird die gesammelte elektrische Energie gebündelt und schießt seinem Ziel entgegen.]\n",
             True, True,True, False, "verwirrt")

feuerball=Zauber("Feuerball",
                 3,
                 4,
                 "ätherisch",
                 1,
                 5,
                 True,
                 True,
                 False,
                 "Schaden",
                 "3W8 Feuerschaden",
                 0,
                 "Feuerschaden",
                 3,
                 8,
                 "Brand",
                 20,
                 "einmalig",
                 "ja", 0, 0,
                 "[Du gewinnst ausreichend Abstand zwischen dir und deinen Gegnern. Deine Hände führen die einstudierte Geste aus, ohne dass du darüber nachdenken musst. Zwischen deinen Händen bildet sich eine Kugel aus reinem Feuer, und du wirfst sie deinem Ziel entgegen, ehe du dich selbst daran verbrennen kannst.]\n",
                 True, False, True, False, "brennend")

licht = Zauber("Licht",
               1,
               4,
               "ätherisch",
               1,
               1,
               True,
               True,
               False,
               "Beschwörung",
               "Nicht tödlich",
               "keine",
               0,
               0,
               0,
               "keine",
               20,
               "1 Minute je Stufe",  "ja",0,0,
               " ", False,False,False,True, "geblendet")


#blitz.Schaden_berechnen()