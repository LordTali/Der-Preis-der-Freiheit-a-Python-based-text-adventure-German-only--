import random
from Regeln import *
class Kampf:
    def __init__(self, teilnehmer, gegner, letzter_zug, runde):
        self.teilnehmer = []
        self.gegner = []
        self.runden_kaempfer = []
        self.letzter_zug = letzter_zug
        self.runde = 0

    def wurf_w12(self):
        wurf = random.randint(1, 12)
        print(f"[Würfel: {wurf}]\n")
        Textpause()
        return wurf

    def Teilnehmer_hinzufuegen(self, teilnehmer):
        self.teilnehmer.append(teilnehmer)

    def Gegner_hinzufuegen(self, gegner):
        self.gegner.append(gegner)

    def Initiative_wuerfeln(self):
        print("[Initiativwurf] \n")
        Textpause()
        for kaempfer in self.teilnehmer:
            print(f"[Wurf ({kaempfer.name})]\n")
            Textpause()
            wurf = self.wurf_w12()
            Textpause()
            print(f"[Reflexe ({kaempfer.name}): {kaempfer.reflexe}]\n")
            Textpause()
            print(f"[Initiative-Bonus ({kaempfer.name}): {kaempfer.initiative_bonus}]\n")
            Textpause()
            initiative_gesamt = kaempfer.reflexe + kaempfer.initiative_bonus + wurf
            kaempfer.initiative = initiative_gesamt
            print(f"[Gesamtinitiative ({kaempfer.name}): {initiative_gesamt}]\n")
            Textpause()
            print("---------------------------------------\n")
            Textpause()

    def Reihenfolge_bestimmen(self):
        initiative = self.Initiative_wuerfeln()
        self.teilnehmer.sort(key=lambda x: x.initiative, reverse=True)
        self.gegner.sort(key=lambda x: x.initiative, reverse=True)
        Textpause()
        self.Reihenfolge_anzeigen()
        pass

    def Reihenfolge_anzeigen(self):
        print("[Kampfreihenfolge]\n")
        Textpause()
        for index, teilnehmer in enumerate(self.teilnehmer, start=1):
            print(f"{index}. {teilnehmer.name} (Initiative: {teilnehmer.initiative})]\n")
        Textpause()
        self.Kampf_beginnen()
        pass

    def Kampf_beginnen(self):
        deine_gegner = []
        for kaempfer in self.gegner:
            deine_gegner.append(kaempfer.name)
        umwandeln = [str(gegner) for gegner in deine_gegner]
        trennzeichen = ", "
        gegner_liste = trennzeichen.join(umwandeln)
        print(f"[Du bist nun im Kampf gegen {gegner_liste}.]\n")
        Textpause()
        self.Runden_zaehler()

    def Runden_zaehler(self):
        self.runde += 1
        for kaempfer in self.teilnehmer:
            kaempfer.verteidigung = 10 + kaempfer.stufe + kaempfer.reflexe - kaempfer.bewaffnung.verteidigungsmalus
            kaempfer.angriffsbonus = 0
            kaempfer.schadensbonus = 0
            kaempfer.aktionen_nummer = 2
        print(f"[Runde {self.runde}]\n")
        Textpause()
        self.Kampfschleife()

    def Kampfschleife(self):
        for kaempfer in (self.teilnehmer):
            self.letzter_zug = kaempfer
            self.Kampfhandlungen()
        self.Runden_zaehler()


    def Kampfhandlungen (self):
        kaempfer = self.letzter_zug
        if kaempfer == Maika:
            if Maika.aktionen_nummer <= 0:
                return None
            else:
                Maika.Handeln(kaempfer)
        else:
            if kaempfer.aktionen_nummer <= 0:
                return None
            else:
                self.Gegner_zug()


    def Spieler_zug(self):
        if Maika.aktionen_nummer <= 0:
            #self.Kampfhandlungen()
            return None
        else:
            deine_gegner = []
            for kaempfer in self.gegner:
                deine_gegner.append(kaempfer.name)
            umwandeln = [str(gegner) for gegner in deine_gegner]
            trennzeichen = ", "
            gegner_liste = trennzeichen.join(umwandeln)
            print(f"[Du kämpfst gegen: {gegner_liste}]\n")  # Bis hierhin geht es nur um die Anzeige.
            Textpause()
            aktuelles_ziel = input(
                "[Gib den Namen des Gegners ein, auf den du dich konzentrieren willst.]\n > ")  # .lower() #macht die Funktion kaputt. Warum?
            for kaempfer in self.gegner:
                if aktuelles_ziel in kaempfer.name:
                    dein_gegner = kaempfer
                    Textpause()
                    print(f"[Du konzentrierst dich auf {dein_gegner.name}]\n")
                    Maika.Handeln_angriff(dein_gegner)
                else:
                    print("[An deiner Eingabe stimmt etwas nicht, oder der Charakter nimmt nicht am Kampf teil.]\n") # Warum ploppt as auf, wenn ich für Maikas zweite Aktion aussetze oder ausweiche?
                    Textpause()
                    self.Spieler_zug()

    def Gegner_zug(self):
        kaempfer = self.letzter_zug
        if kaempfer.aktionen_nummer > 0:
            kaempfer.Handeln(Maika)
        else:
            #self.Kampfschleife()
            #self.Kampfhandlungen()
            return None


Begegnung = Kampf([], [], 0, 0)
