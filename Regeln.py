from Waffen import *
from Ruestung import *
from Magie import blitz, feuerball
from main import time, random



def Textpause():
    time.sleep(1)


class Charakter:
    def __init__(self, name, rasse, geschlecht, kraft, geschick, koerperbau, grips, empathie, magie, stufe, klasse,
                 max_ausdauer, ausdauer, max_zauberkraft, zauberkraft, verteidigung, willen, reflexe_bonus, reflexe,
                 widerstand, max_lebenskraft, lebenskraft,initiative_bonus, aktionen_nummer, angriffsbonus,
                 schadensbonus, max_schutz, schutz, panzerung, kontrollwuerfel, initiative, angriffsmalus, malus_erschoepfung,
                 verfuegbare_zauber, fertigkeiten, waffenfertigkeiten, wundenmalus,  max_lebenskraft_kopf, lebenskraft_kopf,
                 max_lebenskraft_hals, lebenskraft_hals, max_lebenskraft_arme, lebenskraft_arm_links, lebenskraft_arm_rechts,
                 max_lebenskraft_haende, lebenskraft_hand_links, lebenskraft_hand_rechts, max_lebenskraft_torso, lebenskraft_torso,
                 treffer_genitalien, max_lebenskraft_beine, lebenskraft_bein_links, lebenskraft_bein_rechts, max_lebenskraft_knie,
                 lebenskraft_knie_links, lebenskraft_knie_rechts, zustand):

        # Wichtige Attribute
        self.name = name
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.kraft = kraft
        self.geschick = geschick
        self.koerperbau = koerperbau
        self.grips = grips
        self.empathie = empathie
        self.magie = magie
        self.stufe = stufe
        self.klasse = klasse
        self.max_ausdauer = self.kraft + self.koerperbau + self.stufe
        self.ausdauer = max_ausdauer
        self.max_zauberkraft = self.empathie + self.magie + self.stufe
        self.zauberkraft = max_zauberkraft
        self.willen = self.empathie + self.stufe
        self.reflexe_bonus = reflexe_bonus
        self.reflexe = self.geschick + self.stufe + self.reflexe_bonus
        self.bewaffnung = kurzschwert
        self.wundenmalus = wundenmalus
        self.verteidigung = 10 + self.stufe + self.reflexe - self.bewaffnung.verteidigungsmalus - self.wundenmalus
        self.widerstand = self.willen + self.koerperbau
        self.zustand = zustand
        if self.geschlecht == "weiblich":
            self.geschick += 2
            self.empathie += 2
        elif self.geschlecht == "männlich":
            self.kraft += 2
            self.koerperbau += 2


        # Die Trefferzonen
        self.max_lebenskraft = self.koerperbau + self.stufe
        self.lebenskraft = self.max_lebenskraft
        self.max_lebenskraft_kopf = 15
        self.lebenskraft_kopf = self.max_lebenskraft
        self.max_lebenskraft_hals = 10
        self.lebenskraft_hals = self.max_lebenskraft_hals
        self.max_lebenskraft_arme = 10
        self.lebenskraft_arm_links = self.max_lebenskraft_arme
        self.max_lebenskraft_arm_rechts = 10
        self.lebenskraft_arm_rechts = self.max_lebenskraft_arme
        self.max_lebenskraft_haende = 10
        self.lebenskraft_hand_links = self.max_lebenskraft_haende
        self.lebenskraft_hand_links = self.max_lebenskraft_haende
        self.max_lebenskraft_torso = 15
        self.lebenskraft_torso = self.max_lebenskraft_torso
        self.max_lebenskraft_beine = 10
        self.lebenskraft_bein_links = self.max_lebenskraft_beine
        self.lebenskraft_bein_rechts = self.max_lebenskraft_beine
        self.max_lebenskraft_knie = 10
        self.lebenskraft_knie_links = self.max_lebenskraft_knie
        self.lebenskraft_knie_rechts = self.max_lebenskraft_knie
        self.teffer_genitalien = treffer_genitalien

        # Die Kampfwerte
        self.initiative_bonus = initiative_bonus
        self.aktionen_nummer = aktionen_nummer
        self.angriffsbonus = angriffsbonus
        self.schadensbonus = schadensbonus
        self.wuerfel_w12 = random.randint(1, 12)
        self.max_schutz = max_schutz
        self.schutz = max_schutz
        self.panzerung = panzerung
        self.initiative = initiative
        self.kontrollwuerfel = int(self.magie / 2)
        self.angriffsmalus = angriffsmalus
        self.malus_erschoepfung = malus_erschoepfung
        self.verfuegbare_zauber = []

        # Die Fertigkeiten
        self.fertigkeiten = fertigkeiten
        self.waffenfertigkeiten = waffenfertigkeiten


    def Wurf_w6(self):
        wurf = random.randint(1, 6)
        print(f"[Würfel: {(wurf)}]\n")
        return wurf

    def Wurf_w8(self):
            wurf = random.randint(1, 8)
            print(f"[Würfel: {(wurf)}]\n")
            return wurf

    def Wurf_w12(self):
        if self.zustand == "handlos" or self.zustand == "handlos" or self.zustand == "liegend":
            wurf = self.Erschwerter_wurf()
        else:
            wurf = random.randint(1, 12)
        print(f"[Würfel: {(wurf)}]\n")
        Textpause()
        return wurf

    def Reflexwrf(self):
            wuerfel = (self.Wurf_w12())
            wurf_auf_reflexe = wuerfel + self.reflexe
            print(f"[Dein Wurf (Reflexe): {(wurf_auf_reflexe)}]\n")
            return wurf_auf_reflexe

    def Willenswurf (self):
            wuerfel = (self.Wurf_w12())
            wurf_auf_willen = wuerfel + self.willen
            print(f"[Dein Wurf (Willen): {(wurf_auf_willen)}]\n")
            return wurf_auf_willen

    def Ausruesten(self, Waffen):
        self.bewaffnung = Waffen
        print(f"{self.name} kämpft nun mit: {self.bewaffnung.name}")

    def Beguenstigter_wurf (self):
        print("[Begünstigter WUrf]\n")
        Textpause()
        wurf1 = random.randint(1, 12)
        print(f"[Würfel 1: {(wurf1)}]\n")
        Textpause()
        wurf2 = random.randint(1, 12)
        print(f"[Würfel 2: {(wurf2)}]\n")
        Textpause()
        if wurf1 >= wurf2:
            return wurf1
        else:
            return wurf2

    def Erschwerter_wurf (self):
        wurf1 = random.randint(1, 12)
        print(f"[Würfel 1: {(wurf1)}]\n")
        Textpause()
        wurf2 = random.randint(1, 12)
        print(f"[Würfel 2: {(wurf2)}]\n")
        Textpause()
        if wurf1 < wurf2:
            return wurf1
        else:
            return wurf2
    def Handeln(self, target):
        if self.aktionen_nummer<=0:
            print("[Du kannst in diesem Zug keine Aktionen mehr ausführen.] \n")
            return None
        else:
            print("[Du bist dran.]\n")
            Textpause()
            print (f"[Verbleibende Aktionen: {self.aktionen_nummer}]\n")
            Textpause()
            befehl = input ("Was willst du tun? (Optionen: angreifen, zaubern, ausweichen, volle Verteidigung, Zug beenden) \n > ").lower()
            if "greif" in befehl:
                Textpause()
                target = self.Ziel_waehlen()
                self.Handeln_angriff(target)
            elif "voll" in befehl:
                Textpause()
                if self.klasse != "Krieger":
                    Textpause()
                    print("\n[Diese Option steht nur Kampfklassen zur Verfügung. Bitte wähle eine andere Aktion.]\n")
                    Textpause()
                    self.Handeln(target)
                else:
                    self.aktionen_nummer -= 1
                    self.verteidigung += 4
                    self.angriffsbonus -= 4
                    self.ausdauer -= 2
                    Textpause()
                    print(f"[Ausdauer: {self.ausdauer}/{self.max_ausdauer}]\n")
                    Textpause()
                    if self.aktionen_nummer >= 1:
                        self.Handeln(target)
                    else:
                        print("[Du kannst in diesem Zug keine Aktionen mehr ausführen.]\n")
                        Textpause()
                        return None
            elif "zauber" in befehl:
                Textpause()
                target = self.Ziel_waehlen()
                zauberangriff = self.Zaubern(target)
                self.Handeln(target)
                pass
            elif "weich" in befehl:
                if self.aktionen_nummer >= 2:
                    self.aktionen_nummer = 0
                    self.verteidigung += 2
                    self.ausdauer -= 1
                    Textpause()
                    print("[Du versuchst, dem Angriff des Gegners auszuweichen.]\n")
                    Textpause()
                    print ("[Bonus (Verteidigung): 2]\n")
                    Textpause()
                    print (f"[Ausdauer: {self.ausdauer}/{self.max_ausdauer}]\n")
                    Textpause()
                    return None
                else:
                    Textpause()
                    print("[Du hast in dieser Runde bereits gehandelt, daher kannst du nicht mehr ausweichen. Bitte wähle eine andere Aktion.]\n")
                    Textpause()
                    self.Handeln(target)
            elif "zug" in befehl:
                Textpause()
                print ("[Du beendest deinen Zug.]\n")
                Textpause()
                if self.aktionen_nummer == 2:
                    if self.ausdauer < self.max_ausdauer:
                        self.ausdauer +=1
                print (f"[Ausdauer: {self.ausdauer}/{self.max_ausdauer}]\n")
                Textpause()
                self.aktionen_nummer = 0
                return None
            else:
                Textpause()
                print("[Hoppla! An diesem Befehl stimmt etwas nicht. Versuch's bitte noch mal!]\n")
                Textpause()
                self.Handeln(target)

    def Ziel_waehlen(self):
        deine_gegner = []
        for kaempfer in Begegnung.gegner:
            deine_gegner.append(kaempfer.name)
            umwandeln = [str(gegner) for gegner in deine_gegner]
            trennzeichen = ", "
            gegner_liste = trennzeichen.join(umwandeln)
        print(f"[Du kämpfst gegen: {gegner_liste}]\n")  # Bis hierhin geht es nur um die Anzeige.
        Textpause()
        target = self.Ziel_ermitteln()
        return target

    def Ziel_ermitteln(self):
        while True:
            if len(Begegnung.gegner) == 1:
                for kaempfer in Begegnung.gegner:
                    print(f"[{kaempfer.name} ist als einziger Gegner übrig.]\n")
                    Textpause()
                    return kaempfer
            else:
                aktuelles_ziel = input("[Gib den Namen des Gegners ein, auf den du dich konzentrieren willst.]\n > ")
                for kaempfer in Begegnung.gegner:
                    if aktuelles_ziel.lower() in kaempfer.name.lower():
                        Textpause()
                        print(f"[Du konzentrierst dich auf {kaempfer.name}]\n")
                        return kaempfer




    def Handeln_angriff (self, target):
        if self.angriffsbonus != 0:
            print("[Du hast bereits einen anderen modifizierten Kampfstil für diese Runde verwendet. Dieser bleibt bis zur nächsten Runde erhalten.]\n")
            Textpause()
            self.Angreifen(target)
        else:
            befehl = input("[Wie willst du angreifen? (Optionen: ruhig, aggressiv, vorsichtig, schnell)] \n > ").lower()
            if "ruh" in befehl:
                self.Angreifen(target)
            elif "aggr" in befehl:
                self.Angreifen_aggressiv(target)
            elif "vor" in befehl:
                self.Angreifen_vorsichtig(target)
            elif "schnell" in befehl:
                self.Angreifen_schnell(target)
            else:
                print("[Hoppla! An diesem Befehl stimmt etwas nicht. Versuch's bitte noch mal!]\n")
                Textpause()
                self.Handeln_angriff(target)

    def Angreifen_vorsichtig (self, target):
        self.angriffsbonus -= 2
        self.verteidigung += 2
        Textpause()
        self.Angreifen(target)

    def Angreifen_aggressiv (self, target):
        self.angriffsbonus += 2
        self.schadensbonus += 2
        self.verteidigung -=4
        Textpause()
        self.Angreifen(target)

    def Angreifen_schnell(self, target):
        Textpause()
        self.angriffsbonus -= 4
        self.verteidigung -= 4
        Textpause()
        self.Angreifen (target)

    def Angreifen (self, target):
        if self.aktionen_nummer < 2:
            self.angriffsmalus = 5
        else:
            self.angriffsmalus = 0
        if self.ausdauer <= 0:
            Textpause()
            print("[Du bist erschöpft, kannst aber aus letzter Kraft noch weiterkämpfen.]\n")
            Textpause()
        else:
            befehl1 = input ("[Willst du deinen Angriff mit mehr Krafteinsatz verstärken? (Optionen: Ja, Nein)]\n > ").lower()
            if "ja" in befehl1:
                Textpause()
                befehl2 = input (f"[Wie viel Ausdauer willst du einsetzen ({self.ausdauer} verfügbar)? Bitte nur ganze Zahlen eingeben.]\n > ").lower()
                try:
                    befehl2 = int(befehl2)
                    if int(befehl2) < 0:
                        Textpause()
                        print ("[Netter Versuch! Aber so kriegst du deine Ausdauer nicht zurück! Versuch's bitte noch einmal.]\n")
                        Textpause()
                        self.Angreifen(target)
                    elif int(befehl2) > self.ausdauer:
                        Textpause()
                        print ("[So viel Ausdauer hast du derzeit leider nicht zur Verfügung. Versuch's bitte noch einmal.]\n")
                        Textpause()
                        self.Angreifen (target)
                    else:
                        Textpause()
                        self.schadensbonus += int(befehl2)
                        self.ausdauer -= int(befehl2)
                        print(f"[Schadensbonus (Ausdauer): {befehl2}]\n")
                        Textpause()
                        print(f"[Schadensbonus (gesamt): {self.schadensbonus}]\n")
                        Textpause()
                except:
                    print ("[Das ist keine Zahl. Versuch's bitte noch einmal.]\n")
                    Textpause()
                    self.Angreifen(target)
            elif "nein" in befehl1:
                pass
                Textpause()
            else:
                print ("[Hoppla! Da ist etwas schiefgelaufen. Versuch's bitte noch einmal!]\n")
                Textpause()
                self.Angreifen(target)
        angriff_zielen = self.Gezielt_angreifen(target)
        zielen = Begegnung.gezielter_angriff[1]
        self.aktionen_nummer -= 1
        if "taumelnd" in target.zustand:
            wuerfelwurf = self.Beguenstigter_wurf()
        else:
            wuerfelwurf = self.Wurf_w12()
        angriffswurf = (wuerfelwurf + self.geschick + self.angriffsbonus + self.stufe) - self.angriffsmalus - self.bewaffnung.angriffsmalus - self.malus_erschoepfung - zielen
        angriffswurf = target.verteidigung
        angriffsmalus_gesamt = self.angriffsmalus + self.bewaffnung.angriffsmalus + self.malus_erschoepfung + zielen
        verteidigung_ziel = target.verteidigung - target.malus_erschoepfung
        self.ausdauer -= 1 + self.panzerung.belastung + self.bewaffnung.belastung
        print (f"[Ausdauer: {self.ausdauer}/{self.max_ausdauer}]\n")
        Textpause()
        print(f"[Angriffsbonus: {self.geschick + self.angriffsbonus + self.stufe}] \n")
        Textpause()
        if zielen != "nichts":
            print(f"[Angriffsmalus (gezielter Angriff): -{zielen}]\n")
            Textpause()
        if self.angriffsmalus > 0:
            print (f"[Angriffsmalus (Folgeaktion): -{self.angriffsmalus}]\n")
            Textpause()
            if self.ausdauer <= 0:
                self.malus_erschoepfung = 4
                print(f"[Angriffsmalus (Erschöpfung): -{self.malus_erschoepfung}]\n")
                Textpause()
            else:
                self.malus_erschoepfung = 0
        if self.bewaffnung.besonderheit == "sperrig":
            print (f"[Angriffsmalus ({self.bewaffnung.name}): -{self.bewaffnung.angriffsmalus}]\n")
            Textpause()
            print (f"[Angriffsmalus (gesamt): {angriffsmalus_gesamt}]\n")
            Textpause()
        print(f"[Angriffswurf: {angriffswurf}] \n")
        Textpause()
        if target.ausdauer <= 0:
            target.malus_erschoepfung = 4
        print(f"[Verteidigung ({target.name}): {verteidigung_ziel}] \n")
        Textpause()
        if angriffswurf > verteidigung_ziel or wuerfelwurf == 12:                          # Ab hier die Erfolgsberechnung
            self.Schaden(target)
        elif wuerfelwurf == 1:
            print("[KRITISCHER MISSERFOLG.]\n")
            Textpause()
            print("[Dein Angriff geht kolossal daneben.]\n")
            Textpause()
            self.ausdauer -= 1
            print(f"[Deine Ausdauer: {self.ausdauer}/{self.max_ausdauer}]\n")
            Textpause()
        elif angriffswurf == verteidigung_ziel:
            if self.bewaffnung.typ == "Nahkampf":
                print("[Der Angriff wurde in letzter Sekunde pariert. Mach dich auf einen Gegenangriff gefasst.]\n")
                Textpause()
                target.Angreifen_gegenangriff(self)
            else:
                self.Schaden(target)
        elif angriffswurf < verteidigung_ziel -3:
            print("[MISSERFOLG] \n")
            Textpause()
            print(f"[Dein Angriff verfehlt {target.name}.]\n")
            Textpause()
            self.Handeln(target)
        else:
            target.ausdauer -= 1
            print("[MISSERFOLG] \n")
            Textpause()
            print(f"[Dein Angriff verfehlt {target.name} nur knapp.]\n")
            Textpause()
            self.Handeln(target)

    def Schaden (self, target):
        print("[ERFOLG] \n")
        Textpause()
        print(f"[Tödlichkeit der Waffe ({self.bewaffnung.name}): {self.bewaffnung.toedlichkeit}]\n")
        Textpause()
        print(f"[Schaden: {self.bewaffnung.schaden}]\n")
        Textpause()
        gesamtschaden = self.bewaffnung.schaden + self.schadensbonus
        print(f"[Schaden (gesamt): {gesamtschaden}]\n")
        Textpause()
        if Begegnung.gezielter_angriff[0] != "nichts":
            self.Schaden_effekt(target)
        else:
            if target.panzerung.klasse != "ungerüstet":
                target.schutz -= self.bewaffnung.schaden
                if target.schutz > 0:
                    print(f"[Rüstung ({target.name}): {target.schutz}/{target.max_schutz}]\n")
                    Textpause()
                elif target.panzerung == 0:
                    target.lebenskraft -= self.bewaffnung.schaden
                    print("[Die Rüstung bietet keinen Schutz mehr] \n ")
                    Textpause()
                    print(f"[Lebenskraft {target.name}): {target.lebenskraft}/{target.max_lebenskraft}] \n")
                    Textpause()
                else:
                    target.lebenskraft = (target.lebenskraft + (target.schutz + self.bewaffnung.schaden)) - self.bewaffnung.schaden
                    print("[Die Rüstung wurde durchbrochen.] \n")
                    Textpause()
                    print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}] \n")
                    target.schutz = 0
                    Textpause()
                    if target.lebenskraft <= 0:
                        Begegnung.gegner.remove(target)
                        Begegnung.teilnehmer.remove(target)
                        print(f"[{target.name} wurde besiegt.]\n")
                        Textpause()
                        self.Handeln(target)
                    else:
                        target.lebenskraft -= self.bewaffnung.schaden
                        print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}] \n")
                        Textpause()
                        self.Handeln(target)

    def Angreifen_gegenangriff(self, target):
        if self.aktionen_nummer < 2:
            self.angriffsmalus = 5
        else:
            self.angriffsmalus = 0
        print("[Du konntest den Angriff in letzter Sekunde parieren.]\n")
        Textpause()
        print(f"[Deine Ausdauer: {self.ausdauer}/{self.max_ausdauer}]\n")
        Textpause()
        befehl = input("[Willst du einen Gegenangriff wagen? (Optionen: Ja, Nein)]\n > ").lower()
        Textpause()
        if "ja" in befehl:
            self.aktionen_nummer +=1
            self.Handeln_angriff(target)
        elif "nein" in befehl:
            print("[Du verzichtest auf einen Gegenangriff, löst die Waffenbindung und gehst einen Schritt zurück.]\n")
            Textpause()
            target.Handeln(self)
        else:
            print("[Hoppla! Da ist wohl etwas schiefgelaufen! Wir gehen mal davon aus, dass es Nein heißt.]\n")
            Textpause()
            self.Handeln(target)


    def Gezielt_angreifen(self, target):
        befehl = input("[Willst du bei deinem Angriff auf etwas Bestimmtes zielen?]\n > ").lower()
        if "ja" in befehl:
            zielen = self.Angriff_zielen(target)
            Textpause()
            return zielen
        elif "nein" in befehl:
            Textpause()
            return "nichts"
        else:
            print("[Hoppla! Da ist etwas schiefgelaufen. Versuch's bitte noch einmal!]\n")
            Textpause()
            self.Gezielt_angreifen(target)
        
        
    def Angriff_zielen(self, target):
        Textpause()
        print("[Welches Körperteil willst du angreifen?]\n")
        Textpause()
        befehl1 = input(f"[(Optionen: Kopf, Hals, Torso, Hand, Genitalien, Bein)]\n > ").lower()
        if "kopf" in befehl1:
            Textpause()
            Begegnung.gezielter_angriff = ["Kopf", 5]
            return ["Kopf", 5]
        elif "Hals" in befehl1:
            Begegnung.gezielter_angriff = ["Hals", 5]
        elif "Tor" in befehl1:
            Begegnung.gezielter_angriff = ["Torso", 2]
            return ["Torso", 2]
        elif "Hand" in befehl1:
            Begegnung.gezielter_angriff = ["Hand", 3]
            return ["Hand", 5]
        elif "Gen" in befehl1:
            if target.geschlecht == "männlich":
                return ["Genitalien", 7]
            else:
                print ("[Dein Gegner ist nicht männlichen Geschlechts, die Wirkung wäre im Falle des Treffers also weniger dramatisch.]")
                Textpause()
                befehl2 = input(f"[Willst du {target.name} trotzdem im Genitalienbereich angreifen?)\n > ").lower()
                if "ja" in befehl2:
                    Begegnung.gezielter_angriff = ["Genitalien", 7]
                    return ["Genitalien", 7]
                elif "nein" in befehl2:
                    Textpause()
                    self.Angriff_zielen(target)
                else:
                    print("[Hoppla! Da ist etwas schiefgelaufen. Versuch's bitte noch einmal!]\n")
                    Textpause()
                    self.Angriff_zielen(target)
                    Textpause()
        elif "Bein" in befehl1:
            Begegnung.gezielter_angriff = ["Bein", 3]
            return ["Bein", 3]
        else:
            print("[Hoppla! Da ist etwas schiefgelaufen. Versuch's bitte noch einmal!]\n")
            Textpause()
            self.Angriff_zielen(target)

    def Schaden_effekt(self, target):
        if Begegnung.gezielter_angriff[0] == "Kopf":
            print(f"[Deine Waffe trifft {target.name} direkt am Kopf und fügt dem Gegner eine starke verletzung zu.]\n")
            extraschaden = 5
            target.lebenskraft -= extraschaden
            target.lebenskraft_kopf -= extraschaden
            print (f"[Extra-Schaden (Kopf): {extraschaden}]\n")
            Textpause()
            print (f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
            Textpause()
            print (f"[Schaden am Kopf: {target.lebenskraft.kopf}/{target.max_lebenskraft_kopf}]\n")
            Textpause()
            if target.lebenskraft_kopf <= 0 or self.Wurf_w12() == 12:
                print(f"[Dein Angriff fügt {target.name} eine tödliche Wunde zu.]\n")
                Textpause()
                print(f"[{target.name} bricht zusammen und bleibt reglos am Boden liegen.]\n")
                Textpause()
                Begegnung.teilnehmer.remove(target)
                Begegnung.gegner.remove(target)
                self.Handeln(target)
            else:
                print (f"[{target.name} wurde auf den ungeschützten Kopf getroffen und muss einen Rettungswurf ablegen, um nichts Wanken zu geraten.]\n")
                Textpause()
                wurf_auf_willen = target.Willenswurf()
                Textpause()
                if wurf_auf_willen >= 18 or self.Wurf_w12() == 12:
                    print(f"[{target.name} konnte einen klaren Kopf bewahren.]\n")
                else:
                    print(f"[{target.name} ist nur für 1 Runde verwirrt")
                    target.zustand = "verwirrt"
                self.Handeln(target)
        if Begegnung.gezielter_angriff[0] == "Hals":
            print(f"[Deine Waffe trifft {target.name} direkt am Hals und fügt dem Gegner eine starke verletzung zu.]\n")
            extraschaden = 5
            target.lebenskraft -= extraschaden
            target.lebenskraft_hals -= extraschaden
            print(f"[Extra-Schaden (Kopf): {extraschaden}]\n")
            Textpause()
            print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
            Textpause()
            print(f"[Schaden am Hals: {target.lebenskraft.hals}/{target.max_lebenskraft_hals}]\n")
            Textpause()
            if target.lebenskraft_kopf <= 0 or self.Wurf_w12() == 12:
                print(f"[Dein Angriff fügt {target.name} eine tödliche Wunde zu.]\n")
                Textpause()
                print(f"[{target.name} bricht zusammen und bleibt reglos am Boden liegen.]\n")
                Textpause()
                Begegnung.teilnehmer.remove(target)
                Begegnung.gegner.remove(target)
                self.Handeln(target)
            else:
                self.Handeln(target)
        elif Begegnung.gezielter_angriff[0] == "Genitalien" and target.geschlecht == "männlich":
            print(f"[Deine Waffe trifft {target.name} direkt an der wichtigsten Stelle und fügt dem Gegner eine starke verletzung zu.]\n")
            Textpause()
            print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
            Textpause()
            print(f"[Schaden am Privatbereich: {target.lebenskraft.hals}/{target.max_lebenskraft_hals}]\n")
            Textpause()
            print(f"[Das weitere Schicksal des besten Stücks von {target.name} bleibt zumindest vorerst ungewiss, der Gegner geht jedoch zu Boden verkrümmt sich vor unvorstellbaren Schmerzen.]\n")
            Textpause()
            print("[In diesem Kampf stellt er für dich jedenfalls keine Gefahr mehr dar.]\n")
            Textpause()
            Begegnung.teilnehmer.remove(target)
            Begegnung.gegner.remove(target)
            self.Handeln(target)
        elif Begegnung.gezielter_angriff[0] == "Torso":
            print(f"[Deine Waffe trifft {target.name} am Torso und fügt dem Gegner eine starke verletzung zu.]\n")
            Textpause()
            print(f"[{target.name} taumelt und geht unsicher einen Schritt zurück.]\n")
            Textpause()
            target.zustand = "taumelnd"
            if target.lebenskraft_torso <= 0 or self.Wurf_w12() == 12:
                print(f"[Dein Angriff fügt {target.name} eine tödliche Wunde zu.]\n")
                Textpause()
                print(f"[{target.name} bricht zusammen und bleibt reglos am Boden liegen.]\n")
                Textpause()
                Begegnung.teilnehmer.remove(target)
                Begegnung.gegner.remove(target)
                self.Handeln(target)
            else:
                self.Handeln(target)
        elif Begegnung.gezielter_angriff[0] == "Hand":
            print(f"[Deine Waffe trifft {target.name} an der Hand und fügt dem Gegner eine starke verletzung zu.]\n")
            Textpause()
            print(f"[Dein Angriff fügt {target.name} eine kritische Wunde zu.]\n")
            Textpause()
            print(f"[{target.name} verliert seine Hand und kann nur bedingt weiterkämpfen.]\n")
            target.zustand = "handlos"
            Textpause()
            self.Handeln(target)
        elif Begegnung.gezielter_angriff[0] == "Bein":
            print(f"[Deine Waffe trifft {target.name} am Bein und fügt dem Gegner eine starke verletzung zu.]\n")
            Textpause()
            print(f"[{target.name} verliert ein Bein und fällt zu Boden.]\n")
            Textpause()
            target.zustand = "liegend"
            target.verteidigung = 10
            self.Handeln(target)



    def Zaubern(self, target):
        zauber = self.Zauber_waehlen()
        zauber_verstaerkung = self.Zauber_verstaerken()
        if zauber.aufhebung == "ja":                                                    # Hier die Berechnung des Aufhebungswerts
            zauber.aufhebungswert = self.willen + zauber.erfolgswert
            if zauber.erfolgswert == 5:
                for wuerfel in zauber.schadenswuerfel_anzahl:
                    zauber.aufhebungsbonus = 1
            elif zauber.erfolgswert == 6:
                for wuerfel in zauber.schadenswuerfel_anzahl:
                    zauber.aufhebungsbonus = 2
            else:
                zauber.aufhebungsbonus = 0
        print(f"[Zauberkraft-Aufwand ({zauber.name}): {zauber.aufwand_zauberkraft}]\n")
        Textpause()
        self.zauberkraft -= zauber.aufwand_zauberkraft
        print(f"[Deine Zauberkraft: {self.zauberkraft}/{self.max_zauberkraft}]\n")
        Textpause()
        if zauber_verstaerkung > 0:
            zauber.aufhebungsbonus += zauber_verstaerkung
            self.zauberkraft -= zauber_verstaerkung
            print(f"[Aufwand (Zauberverstärkung): {zauber_verstaerkung}]\n")
            Textpause()
            print(f"[Deine Zauberkraft: {self.zauberkraft}/{self.max_zauberkraft}]\n")
            Textpause()                                                                             # Ende der Verstärkung
        print(f"[Aktionsaufwand ({zauber.name}): {zauber.aufwand_aktion}]\n")
        Textpause()
        kontrollwurf = []
        erfolge = []
        print(f"[Erfolgswert ({zauber.name}): {zauber.erfolgswert}]\n")
        Textpause()
        for kontrollwuerfel in range(self.kontrollwuerfel):
            kontrollversuch = self.Wurf_w6()
            Textpause()
            kontrollwurf.append(kontrollversuch)
        kontroll_anzeige = []
        for wurf in kontrollwurf:                                                     # Hier die Formel für die Kontrollwurfanzeige
            kontroll_anzeige = kontrollwurf
            umwandeln = [str(wurf) for wurf in kontroll_anzeige]
            trennzeichen = ", "
            kontroll_anzeige = trennzeichen.join(umwandeln)
        print(f"[Ergebnis (Kontrollwurf): {kontroll_anzeige}]\n")                     # Ende der Kontrollwurfanzeige
        Textpause()
        for wuerfel in kontrollwurf:
            if wuerfel >= 4:
                erfolge.append(wuerfel)
        print(f"[Erfolge (Kontrollwurf): {len(erfolge)}]\n")
        Textpause()
        print(f"[Kontrollwert ({zauber.name}): {zauber.kontrollwert}]\n")
        if len(erfolge) >= zauber.kontrollwert:                                      # Hier die Erfolgsrechnung
            print("[Du konntest die erforderliche magische Kraft fokussieren.]\n")
            Textpause()
            target = self.Ziel_waehlen()                                             # Hier die Zielauswahl
            angriffswurf = self.Zauber_zielen(target)
            self.aktionen_nummer -= zauber.aufwand_aktion
            if zauber.angriffswurf == False:                                       # Wenn der Zauber nicht erst treffen muss.
                if zauber.rettungswurf_reflexe == True:                            # Zum Halbieren des Schadens
                    print(f"[Tödlichkeit des Zaubers: {zauber.toedlichkeit}]\n")  # Formel für die Tödlichkeit und den Schaden
                    Textpause()
                    gesamtschaden = self.Zauber_schaden(zauber)
                    print(f"[Gesamtschaden ({zauber.name}): {gesamtschaden}]\n")
                    Textpause()
                    wurf = target.Zauber_reflexwurf()
                    print(f"[Reflexe ({target.name}): {target.reflexe}]\n")
                    Textpause()
                    rettungswurf = wurf + target.reflexe
                    if wurf == 12:
                        print(f"[Mit einem unglaublichen Zusammenspiel von Glück und Reflexen schafft es {target.name}, deinem Zauber im allerletzten Moment auszuweichen.]\n")
                        Textpause()
                        target.ausdauer -= 1
                    else:
                        if rettungswurf >= angriffswurf:
                            print(f"[{target.name} kann das Schlimmste gerade noch so verhindern und nimmt nur den halben Schaden.]\n")
                            Textpause()
                            halber_schaden = int(gesamtschaden / 2)
                            print(f"[Dein Zauber ({zauber.name}) trifft {target.name} und richtet {halber_schaden}/{gesamtschaden} Punkte {zauber.schadensart} an.]\n")
                            target.lebenskraft -= halber_schaden
                            Textpause()
                            print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
                            Textpause()
                        else:
                            print(f"[{target.name} versucht, deinem Zauber ({zauber.name}) auszuweichen, ist aber zu langsam und nimmt vollen Schaden.]\n")
                            Textpause()
                            print(f"[Dein Zauber ({zauber.name}) trifft {target.name} und richtet {gesamtschaden} Punkte {zauber.schadensart} an.]\n")
                            target.lebenskraft -= gesamtschaden
                            Textpause()
                            print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
                            Textpause()
                        if target.lebenskraft <= 0:
                            Begegnung.gegner.remove(target)
                            Begegnung.teilnehmer.remove(target)
                            print(f"[{target.name} wurde besiegt.]\n")
                            Textpause()
                        else:
                            print (f"[Dein Zauber ({zauber.name}) hat eine den Geist beeinflussende Wirkung ({zauber.effekt}.]\n")
                            Textpause()
                            wurf = target.Zauber_willenswurf()
                            rettungswurf = wurf + target.willen
                            if rettungswurf >= self.willen + zauber_verstaerkung:
                                print(f"[{target.name} konnte der Wirkung widerstehen.]\n")
                                Textpause()
                            else:
                                target.zustand.append(zauber.effekt)
                                effekt = target.Zaubereffekt_berechnen()
                                print (f"[{target.name} ist nun {zauber.effekt}.]\n")
                                Textpause()
                            pass
                        self.Handeln(target)
                elif zauber.rettungswurf_willen == True:
                    print(f"[Dein Zauber ({zauber.name}) hat eine den Geist beeinflussende Wirkung ({zauber.effekt}.]\n")
                    Textpause()
                    wurf = target.Zauber_willenswurf()
                    rettungswurf = wurf + target.willen
                    if rettungswurf >= self.willen + zauber_verstaerkung:
                        print(f"[{target.name} konnte der Wirkung widerstehen.]\n")
                        Textpause()
                    else:
                        target.zustand.append(zauber.effekt)
                        effekt = target.Zaubereffekt_berechnen()
                        print(f"[{target.name} ist nun {zauber.effekt}.]\n")
                        Textpause()
                else:
                    self.Handeln(target)
            else:
                if angriffswurf >= target.verteidigung:
                    gesamtschaden = self.Zauber_schaden(zauber)
                    print(f"[Tödlichkeit des Zaubers: {zauber.toedlichkeit}]\n")          # Formel für die Tödlichkeit und den Schaden
                    Textpause()
                    print(f"[Dein Zauber ({zauber.name}) trifft {target.name} und richtet {gesamtschaden} Punkte {zauber.schadensart} an.]\n")
                    target.lebenskraft -= gesamtschaden
                    Textpause()
                    print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
                    Textpause()
                    if target.lebenskraft <= 0:
                        Begegnung.gegner.remove(target)
                        Begegnung.teilnehmer.remove(target)
                        print(f"[{target.name} wurde besiegt.]\n")
                        Textpause()
                    self.Handeln(target)
                else:
                    print(f"[{target.name} schafft es, dem Angriff auszuweichen.]\n")
                    Textpause()
                    self.Handeln(target)
        else:
            self.aktionen_nummer -= zauber.aufwand_aktion
            wurf_nat1 = kontrollwurf.count(1)
            wurf_nat6 = kontrollwurf.count(6)
            wurf_nat1 -= wurf_nat6
            if wurf_nat1 > len(erfolge):
                print("[Du versuchst, deine Kraft zu fokussieren, verlierst aber die Kontrolle über die magischen Ströme.]\n")
                Textpause()
                Textpause()
                print("[Es kommt zu einer Zauberdetonation.]\n")
                Textpause()
                schaden = self.Wurf_zauberdetonation()
                if target.lebenskraft <= 0:
                    Begegnung.gegner.remove(target)
                    Begegnung.teilnehmer.remove(target)
                    print(f"[{target.name} wurde besiegt.]\n")
                    Textpause()
                self.Handeln(target)
            else:
                print("[Etwas scheint nicht so zu klappen, wie du willst. Du kannst die notwendige magische Energie nicht gut genug fokussieren.]\n")
                Textpause()
                self.Handeln(target)
                return None

    def Zaubereffekt_berechnen(self):
        if self.zustand == "taumelnd":
            self.aktionen_nummer -= 1
        elif self.zustand == "verwirrt":
            self.aktionen_nummer = 0
            pass

    def Zauber_reflexwurf(self):
        Textpause()
        print(f"[{self.name} versucht, deinem Zauber im letzten Moment auszuweichen.]\n")
        Textpause()
        wurf = self.Wurf_w12()
        rettungswurf = wurf + self.reflexe
        return rettungswurf

    def Zauber_willenswurf(self):
        Textpause()
        print (f"[{self.name} versucht, den geistigen Effekten deines Zaubers zu widerstehen.]\n")
        Textpause()
        wurf = self.Wurf_w12()
        rettungswurf = wurf + self.willen
        return rettungswurf



    def Zauber_schaden(self, zauber):
        zauberschaden = []
        for wurf in range(zauber.schadenswuerfel_anzahl):
            if zauber.schadenswuerfel_groesse == 6:
                wurf = zauber.Wurf_w6()
                Textpause()
            elif zauber.schadenswuerfel_groesse == 8:
                wurf = zauber.Wurf_w8()
                Textpause()
            elif zauber.schadenswuerfel_groesse == 10:
                wurf = zauber.Wurf_w10()
                Textpause()
            elif zauber.schadenswuerf_groesse == 12:
                wurf = zauber.Wurf_w12()
                Textpause()
            elif zauber.schadenswuerfel_groesse == 20:
                wurf = zauber.Wurf_w20()
                Textpause()
            else:
                zauber.Wurf_w4()
            zauberschaden.append(wurf)
        gesamtschaden = sum(zauberschaden)
        print(gesamtschaden)
        return gesamtschaden


    def Zauber_waehlen(self):
        befehl = input("[Wähle den Zauber, den wirken willst.]\n > ")
        Textpause()
        for zauber in self.verfuegbare_zauber:
            if befehl.lower() in zauber.name.lower():
                Textpause()
                print(f"[Du versuchst, {zauber.name} zu wirken.]\n")
                Textpause()
                return zauber


    def Wurf_zauberdetonation(self):
        print("[Die magischen Ströme wirbeln wild umher und explodieren schließlich in einer 9n großen Sphäre aus weiß-blauer Energie, bevor jemand im Wirkungsbereich reagieren kann.]\n")
        Textpause()
        print("[Tödlichkeit (Zauberdetonation): 2W6]\n")
        Textpause()
        wurf1 = self.Wurf_w6()
        Textpause()
        wurf2 = self.Wurf_w6()
        Textpause()
        schaden = wurf1 + wurf2
        print(f"[Schaden: {schaden}]\n")
        Textpause()
        if len(Begegnung.teilnehmer) == 0: # Zauberdetonation außerhalb von Kämpfen
            self.lebenskraft -= schaden
            print (f"[Deine Lebenskraft: {self.lebenskraft}/{self.max_lebenskraft}]\n")
            Textpause()
            return schaden
        else:
            for kaempfer in Begegnung.teilnehmer: # Zauberdetonation im Kampf
                if kaempfer.entfernung <= 9:
                    kaempfer.lebenskraft -= schaden
                    print(f"[Lebenskraft ({kaempfer.name}): {kaempfer.lebenskraft}/{kaempfer.max_lebenskraft}]\n")
                    Textpause()
            return None


    def Zauber_zielen(self, target):
        wurf = self.Wurf_w12()
        angriffswurf = wurf + self.willen + self.waffenfertigkeiten.get("Zauber")
        print(f"[Dein Angriffswurf (Zauber): {angriffswurf}]\n")
        Textpause()
        if self.aktionen_nummer < 2:
            self.angriffsmalus = 5
            print(f"[Angriffsmalus (Folgeaktion): -{self.angriffsmalus}]\n")
            Textpause()
            print(f"[Angriffswurf (gesamt): {angriffswurf}]\n")
            Textpause()
        print(f"[Verteidigung ({target.name}): {target.verteidigung}]\n")
        Textpause()
        return angriffswurf


    def Gegenzauber(self, target):
        Textpause()
        befehl = input("[Du kannst versuchen, diesen Zauber zu unterbinden. Willst du einen Versuch wagen?]\n > ")
        if "ja" in befehl:
            print("[Du versucht, einen Gegenzauber zu wirken.]\n")
            Textpause()
            print(f"[Dein Willen: {self.willen}]\n")
            Textpause()
            gegenzauber = self.Zauber_aufhebungswurf()
            return gegenzauber
        elif "nein" in befehl:
            return 0
        else:
            print("[Hoppla! An diesem Befehl stimmt etwas nicht. Versuch's bitte noch mal!]\n")
            Textpause()
            self.Gegenzauber(target)


    def Zauber_aufhebungswurf(self):
        zauber_verstaerkung = self.Zauber_verstaerken()
        Textpause()
        wurf = self.Wurf_w12()
        Textpause()
        konzentration = self.willen + wurf
        if zauber_verstaerkung >= 0:
            konzentration += zauber_verstaerkung
            self.zauberkraft -= zauber_verstaerkung
            print(f"[Aufwand (Zauberverstärkung): {zauber_verstaerkung}]\n")
            Textpause()
            print(f"[Deine Zauberkraft: {self.zauberkraft}/{self.max_zauberkraft}]\n")
            Textpause()
        print(f"[Dein Aufhebungswurf: {konzentration}]\n")
        Textpause()
        return konzentration

    def Zauber_verstaerken(self):
        befehl1 = input("[Willst du den Zauber mit zusätzlicher Zauberkraft verstärken?]\n > ").lower()
        if "ja" in befehl1:
            befehl2 = input(f"[Wie viel Zauberkraft willst du einsetzen ({self.zauberkraft} verfügbar)? Bitte nur ganze Zahlen eingeben.]\n > ")
            try:
                befehl2 = int(befehl2)
                if int(befehl2) < 0:
                    Textpause()
                    print("[Netter Versuch! Aber so kriegst du deine Zauberkraft nicht zurück! Versuch's bitte noch einmal.]\n")
                    Textpause()
                    self.Zauber_verstaerken()
                elif int(befehl2) > self.zauberkraft:
                    Textpause()
                    print("[So viel Zauberkraft hast du derzeit leider nicht zur Verfügung. Versuch's bitte noch einmal.]\n")
                    Textpause()
                    self.Zauber_verstaerken()
                else:
                    Textpause()
                    return int(befehl2)
            except:
                print("[Das ist keine Zahl. Versuch's bitte noch einmal.]\n")
                Textpause()
                self.Zauber_verstaerken()
        elif "nein" in befehl1:
            return 0
        else:
            print("[Hoppla! An diesem Befehl stimmt etwas nicht. Versuch's bitte noch mal!]\n")
            Textpause()
            self.Zauber_verstaerken()


    def Fertigkeitswurf_ablegen(self, fertigkeit):
        global benutzte_fertigkeit
        benutzte_fertigkeit = self.Fertigkeit_waehlen(fertigkeit)
        Textpause()
        wurfel = self.Wurf_w12()
        print(f"[Bonus (Fertigkeit {fertigkeit}): {benutzte_fertigkeit}]\n")
        Textpause()
        bonus = self.Bonus_bestimmen(fertigkeit)
        wurfergebnis = wurfel + bonus + benutzte_fertigkeit
        print (f"[Wurfergebnis: {wurfergebnis}]\n")
        Textpause()
        global wurfergebnis_fertigkeit
        wurfergebnis_fertigkeit = wurfergebnis
        return wurfergebnis
        pass


    def Fertigkeit_waehlen(self, fertigkeit):
        print(f"[Du legst einen Wurf auf {fertigkeit} ab.]\n")
        if fertigkeit in self.fertigkeiten.keys():
            punktzahl = self.fertigkeiten.get(fertigkeit)
            return punktzahl
        else:
            return 0
        pass

    def Bonus_bestimmen(self, fertigkeit):
        fertigkeitswahl = benutzte_fertigkeit
        attribut_kraft = ["Drohen"]
        attribut_geschick = ["Schwimmen", "Sportlichkeit", "Reiten", "Tarnung", "Äxte", "Armbrüste", "Bögen","Handfeuerwaffen", "Kampfstäbe", "Leichte und Wurfwaffen", "Schwerter", "Sprengstoff","Spulenwaffen", "Stangenwaffen", "Starkfeuerwaffen", "Unbewaffnet", "Ungewöhnliche Waffen","Wuchtwaffen"]
        attribut_empathie = ["Magistik", "Menschenkenntnis", "Religion", "Täuschen", "Überreden", "Verführen", "Zauber"]
        attribut_grips = ["Botanik", "Kulturkunde", "Sprachen", "Erkennen", "Linguistik", "Mechanik", "Orientierung","Weltwissen", "Elektrik"]
        if fertigkeit in attribut_kraft:
            relevantes_attribut = "Kraft"
            relevanter_wert = self.kraft
        elif fertigkeit in attribut_geschick:
            relevantes_attribut = "Geschick"
            relevanter_wert = self.geschick
        elif fertigkeit in attribut_grips:
            relevantes_attribut = "Grips"
            relevanter_wert = self.grips
        else:
            relevantes_attribut = "Empathie"
            relevanter_wert = self.empathie
        bonus_attribut = int(relevanter_wert / 2)
        print(f"[Bonus ({relevantes_attribut}): {bonus_attribut}]\n ")
        Textpause()
        gesamtbonus = benutzte_fertigkeit + bonus_attribut
        if fertigkeitswahl == 0:
            gesamtbonus -= 3
            print("[Malus (ungeübt): -3]\n")
            Textpause()
        print(f"[Bonus (gesamt): {gesamtbonus}]\n ")
        Textpause()
        return gesamtbonus

    def Kontrollwurf_fertigkeit(self, zauber):                              # Zauberwurf außerhalb von Kämpfen.
        print(f"[Du versuchst, {zauber.name} zu wirken.]\n")
        Textpause()
        self.zauberkraft -= zauber.aufwand_zauberkraft
        print(f"[Deine Zauberkraft: {self.zauberkraft}/{self.max_zauberkraft}]\n")
        Textpause()
        kontrollwurf = []
        erfolge = []
        wurf_nat1 = kontrollwurf.count(1)
        wurf_nat6 = kontrollwurf.count(6)
        wurf_nat1 -= wurf_nat6
        print(f"[Erfolgswert ({zauber.name}): {zauber.erfolgswert}]\n")
        Textpause()
        for kontrollwuerfel in range(self.kontrollwuerfel):
            kontrollversuch = self.Wurf_w6()
            Textpause()
            kontrollwurf.append(kontrollversuch)
        kontroll_anzeige = []
        for wurf in kontrollwurf:                                                     # Hier die Formel für die Kontrollwurfanzeige
            kontroll_anzeige = kontrollwurf
            umwandeln = [str(wurf) for wurf in kontroll_anzeige]
            trennzeichen = ", "
            kontroll_anzeige = trennzeichen.join(umwandeln)
        print(f"[Ergebnis (Kontrollwurf): {kontroll_anzeige}]\n")                     # Ende der Kontrollwurfanzeige
        Textpause()
        for wuerfel in kontrollwurf:
            if wuerfel >= 4:
                erfolge.append(wuerfel)
        print(f"[Erfolge (Kontrollwurf): {len(erfolge)}]\n")
        Textpause()
        print(f"[Kontrollwert ({zauber.name}): {zauber.kontrollwert}]\n")
        Textpause()
        if len(erfolge) >= zauber.kontrollwert and len(erfolge) > wurf_nat1:            # Hier die Erfolgsrechnung
            print(f"[Du kannst die erforderliche magische Kraft fokussieren.]\n")
            Textpause()
            return True
        elif wurf_nat1 > len(erfolge):
            print("[Du versuchst, deine Kraft zu fokussieren, verlierst aber die Kontrolle über die magischen Ströme.]\n")
            Textpause()
            print("[Es kommt zu einer Zauberdetonation.]\n")
            Textpause()
            schaden = self.Wurf_zauberdetonation()
            return False
        else:
            print("[Du versuchst, zu zaubern, schaffst es aber nicht, die notwendige magische Kraft zu fokussieren.]\n")
            return False



class Spieler (Charakter):
    def __init__(self, name, rasse, geschlecht, kraft, geschick, koerperbau, grips, empathie, magie, stufe, klasse,
                 max_ausdauer, ausdauer, max_zauberkraft, zauberkraft, verteidigung, willen, reflexe_bonus, reflexe,
                 widerstand, max_lebenskraft, lebenskraft, initiative_bonus, aktionen_nummer, angriffsbonus,
                 schadensbonus, max_schutz, schutz, panzerung, kontrollwuerfel, initiative, angriffsmalus, malus_erschoepfung,
                 verfuegbare_zauber, entfernung, fertigkeiten, waffenfertigkeiten, wundenmalus, max_lebenskraft_kopf, lebenskraft_kopf,
                 max_lebenskraft_hals, lebenskraft_hals, max_lebenskraft_arme, lebenskraft_arm_links, lebenskraft_arm_rechts,
                 max_lebenskraft_haende, lebenskraft_hand_links, lebenskraft_hand_rechts, max_lebenskraft_torso, lebenskraft_torso,
                 treffer_genitalien, max_lebenskraft_beine, lebenskraft_bein_links, lebenskraft_bein_rechts, max_lebenskraft_knie,
                 lebenskraft_knie_links, lebenskraft_knie_rechts, zustand, wut, trauer, hoffnung, angst):
        self.name = name
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.kraft = kraft
        self.geschick = geschick
        self.koerperbau = koerperbau
        self.grips = grips
        self.empathie = empathie
        self.magie = magie
        self.stufe = stufe
        self.klasse = klasse
        self.max_ausdauer = self.kraft + self.koerperbau + self.stufe
        self.ausdauer = max_ausdauer
        self.max_zauberkraft = self.empathie + self.magie + self.stufe
        self.zauberkraft = max_zauberkraft
        self.willen = self.empathie + self.stufe
        self.reflexe_bonus = reflexe_bonus
        self.reflexe = self.geschick + self.stufe + self.reflexe_bonus
        self.bewaffnung = kurzschwert
        self.verteidigung = 10 + self.stufe + self.reflexe - self.bewaffnung.verteidigungsmalus - wundenmalus
        self.widerstand = self.willen + self.koerperbau
        self.max_lebenskraft = self.koerperbau + self.stufe
        self.lebenskraft = self.max_lebenskraft
        self.max_lebenskraft_kopf = 15
        self.lebenskraft_kopf = self.max_lebenskraft
        self.max_lebenskraft_hals = 10
        self.lebenskraft_hals = self.max_lebenskraft_hals
        self.max_lebenskraft_arme = 10
        self.lebenskraft_arm_links = self.max_lebenskraft_arme
        self.max_lebenskraft_arm_rechts = 10
        self.lebenskraft_arm_rechts = self.max_lebenskraft_arme
        self.max_lebenskraft_haende = 10
        self.lebenskraft_hand_links = self.max_lebenskraft_haende
        self.lebenskraft_hand_links = self.max_lebenskraft_haende
        self.max_lebenskraft_torso = 15
        self.lebenskraft_torso = self.max_lebenskraft_torso
        self.max_lebenskraft_beine = 10
        self.lebenskraft_bein_links = self.max_lebenskraft_beine
        self.lebenskraft_bein_rechts = self.max_lebenskraft_beine
        self.max_lebenskraft_knie = 10
        self.lebenskraft_knie_links = self.max_lebenskraft_knie
        self.lebenskraft_knie_rechts = self.max_lebenskraft_knie
        self.teffer_genitalien = treffer_genitalien
        self.initiative_bonus = initiative_bonus
        self.aktionen_nummer = aktionen_nummer
        self.angriffsbonus = angriffsbonus
        self.schadensbonus = schadensbonus
        self.wuerfel_w12 = random.randint(1, 12)
        self.max_schutz = max_schutz
        self.schutz = max_schutz
        self.panzerung = panzerung
        self.initiative = initiative
        self.kontrollwuerfel = int(self.magie / 2)
        self.angriffsmalus = angriffsmalus
        self.malus_erschoepfung = malus_erschoepfung
        self.verfuegbare_zauber = verfuegbare_zauber
        self.entfernung = entfernung
        self.fertigkeiten = fertigkeiten
        self.waffenfertigkeiten = waffenfertigkeiten
        self.wundenmalus = wundenmalus
        self.zustand = zustand
        if self.geschlecht == "weiblich":
            self.geschick += 2
            self.empathie += 2
        elif self.geschlecht == "männlich":
            self.kraft += 2
            self.koerperbau += 2
        self.wut = wut
        self.trauer = trauer
        self.hoffnung = hoffnung
        self.angst = angst

class Gegner (Charakter):
    def __init__(self, name, rasse, geschlecht, kraft, geschick, koerperbau, grips, empathie, magie, stufe, klasse,
                 max_ausdauer, ausdauer, max_zauberkraft, zauberkraft, verteidigung, willen, reflexe_bonus, reflexe,
                 widerstand, max_lebenskraft, lebenskraft, initiative_bonus, angriffsbonus, aktionen_nummer,
                 schadensbonus, max_schutz, schutz, panzerung, kontrollwuerfel, initiative, angriffsmalus, malus_erschoepfung,
                 schneller_angriff, verfuegbare_zauber, entfernung, fertigkeiten, waffenfertigkeiten, wundenmalus,  max_lebenskraft_kopf, lebenskraft_kopf,
                 max_lebenskraft_hals, lebenskraft_hals, max_lebenskraft_arme, lebenskraft_arm_links, lebenskraft_arm_rechts,
                 max_lebenskraft_haende, lebenskraft_hand_links, lebenskraft_hand_rechts, max_lebenskraft_torso, lebenskraft_torso,
                 treffer_genitalien, max_lebenskraft_beine, lebenskraft_bein_links, lebenskraft_bein_rechts, max_lebenskraft_knie,
                 lebenskraft_knie_links, lebenskraft_knie_rechts, zustand):
        self.name = name
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.kraft = kraft
        self.geschick = geschick
        self.koerperbau = koerperbau
        self.grips = grips
        self.empathie = empathie
        self.magie = magie
        self.stufe = stufe
        self.klasse = klasse
        self.max_ausdauer = self.kraft + self.koerperbau + self.stufe
        self.ausdauer = max_ausdauer
        self.max_zauberkraft = self.empathie + self.magie + self.stufe
        self.zauberkraft = max_zauberkraft
        self.willen = self.empathie + self.stufe
        self.reflexe_bonus = reflexe_bonus
        self.reflexe = self.geschick + self.stufe + self.reflexe_bonus
        self.bewaffnung = kurzschwert
        self.wundenmalus = wundenmalus
        self.verteidigung = 10 + self.stufe + self.reflexe - self.bewaffnung.verteidigungsmalus - self.wundenmalus
        self.widerstand = self.willen + self.koerperbau
        self.max_lebenskraft = self.koerperbau + self.stufe
        self.lebenskraft = self.max_lebenskraft

        # Die Trefferzonen
        self.max_lebenskraft_kopf = 15
        self.lebenskraft_kopf = self.max_lebenskraft
        self.max_lebenskraft_hals = 10
        self.lebenskraft_hals = self.max_lebenskraft_hals
        self.max_lebenskraft_arme = 10
        self.lebenskraft_arm_links = self.max_lebenskraft_arme
        self.max_lebenskraft_arm_rechts = 10
        self.lebenskraft_arm_rechts = self.max_lebenskraft_arme
        self.max_lebenskraft_haende = 10
        self.lebenskraft_hand_links = self.max_lebenskraft_haende
        self.lebenskraft_hand_links = self.max_lebenskraft_haende
        self.max_lebenskraft_torso = 15
        self.lebenskraft_torso = self.max_lebenskraft_torso
        self.max_lebenskraft_beine = 10
        self.lebenskraft_bein_links = self.max_lebenskraft_beine
        self.lebenskraft_bein_rechts = self.max_lebenskraft_beine
        self.max_lebenskraft_knie = 10
        self.lebenskraft_knie_links = self.max_lebenskraft_knie
        self.lebenskraft_knie_rechts = self.max_lebenskraft_knie
        self.teffer_genitalien = treffer_genitalien
        self.initiative_bonus = initiative_bonus
        self.aktionen_nummer = 2
        self.angriffsbonus = angriffsbonus
        self.schadensbonus = schadensbonus
        self.wuerfel_w12 = random.randint(1, 12)
        self.max_schutz = max_schutz
        self.schutz = max_schutz
        self.panzerung = panzerung
        self.kontrollwuerfel = int(self.magie / 2)
        self.angriffsmalus = angriffsmalus
        self.initiative = initiative
        self.malus_erschoepfung = malus_erschoepfung
        self.schneller_angriff = schneller_angriff
        self.verfuegbare_zauber = verfuegbare_zauber
        self.entfernung = entfernung
        self.fertigkeiten = fertigkeiten
        self.waffenfertigkeiten = waffenfertigkeiten
        self.zustand = zustand
        if self.geschlecht == "weiblich":
            self.geschick += 2
            self.empathie += 2
        elif self.geschlecht == "männlich":
            self.kraft += 2
            self.koerperbau += 2

    def Reflexwrf(self):
        wuerfel = (self.Wurf_w12())
        wurf_auf_reflexe = wuerfel + self.reflexe
        print(f"[Reflexwurf ({self.name}): {(wurf_auf_reflexe)}]\n")
        return wurf_auf_reflexe

    def Willenswurf(self):
        wuerfel = (self.Wurf_w12())
        wurf_auf_willen = wuerfel + self.willen
        print(f"[Willenswurf ({self.name}): {(wurf_auf_willen)}]\n")
        return wurf_auf_willen

    def Handeln(self, target):
        self.schneller_angriff = 0
        if self.aktionen_nummer <= 0:
            print(f"[{self.name} beendet den Zug.] \n")
            Textpause()
            Begegnung.Kampfschleife()
        else:
            print(f"[{self.name} ist dran.]\n")
            Textpause()
            if self.ausdauer <= 0:
                print (f"[{self.name} wirkt ziemlich erschöpft.]\n")
                Textpause()
            befehl1 = random.randint(1,12) # Ab hier die Logik der Handlung
            if befehl1 in range (1, 3):
                Textpause()
                self.Handeln_angreifen(target)
            elif befehl1 == 4:
                if self.kontrollwuerfel > 0:
                    Textpause()
                    self.Zaubern(target)
                    Textpause()
                else:
                    if self.aktionen_nummer < 2:
                        self.Handeln_angreifen(target)
                    else:
                        self.Handeln_ausweichen(target)
            elif befehl1 in range(5, 8):
                Textpause()
                self.Handeln_angreifen(target)
            elif befehl1 in range (9,10):
                if self.aktionen_nummer < 2:
                    self.Handeln_angreifen(target)
                else:
                    self.Handeln_ausweichen(target)
                Textpause()
            elif befehl1 in range (11,12):
                if self.klasse == "Krieger":
                    Textpause()
                    print(f"[{self.name} ahnt etwas und geht vorsichtshalber in Volle Verteidigung].\n")
                    self.verteidigung +=4
                    self.angriffsbonus -=4
                    self.aktionen_nummer-=1
                    Textpause()
                    self.Angreifen_ruhig(target)
                else:
                    if self.aktionen_nummer < 2:
                        self.Handeln_angreifen(target)
                    else:
                        self.Handeln_ausweichen(target)
            else:
                befehl2 = random.randint(1,2)
                if befehl2 == 1:
                    self.Handeln_angreifen(target)
                if befehl2 == 2:
                    if self.rasse == "Ork":
                        self.Handeln_angreifen(target)
                    else:
                        if self.aktionen_nummer < 2:
                            self.Handeln_angreifen(target)
                        else:
                            self.Angreifen(target)

    def Handeln_ausweichen (self, target):
        Textpause()
        print(f"[{self.name} versucht, nicht getroffen zu werden.]\n")
        Textpause()
        print("[Bonus (Verteidigung): 2]\n")
        Textpause()
        while self.ausdauer <= 0:
            print (f"[Malus (Erschöpfung): -{self.malus_erschoepfung}]n")
            Textpause()
        self.aktionen_nummer = 0
        self.verteidigung += 2 - self.malus_erschoepfung
        Begegnung.Kampfschleife()


    def Handeln_angreifen (self, target):
            if self.aktionen_nummer < 2:
                self.angriffsmalus = 5
            else:
                self.angriffsmalus = 0
            befehl1 = random.randint(1,12)
            if isinstance(self.aktionen_nummer, float):
                self.Angreifen_schnell(target)
            else:
                befehl2 = random.randint(1,3)
                if befehl2 == 1:
                    self.Angreifen_ruhig(target)
                elif befehl2 == 2:
                    self.Angreifen_aggressiv(target)
                else:
                    if self.rasse == "Ork":
                        self.Angreifen_ruhig(target)
                    else:
                        self.Angreifen_vorsichtig(target)
            if self.rasse == "Ork":
                if self.lebenskraft < int(self.max_lebenskraft/2):
                    if self.ausdauer > 3:
                        befehl_verstaerkung = random.randint(1,self.ausdauer)
                        self.ausdauer-=befehl_verstaerkung
                        self.schadensbonus+=befehl_verstaerkung
                        Textpause()
                        print(f"[Der Gegner verstärkt seinen Angriff mit {befehl_verstaerkung} Punkten Ausdauer.]\n")
                        if befehl1 in range(1,8):
                            self.Angreifen_aggressiv(target)
                        else:
                            self.Angreifen_ruhig(target)
                    else:
                        if befehl1 in range(1,8):
                            self.Angreifen_aggressiv(target)
                        else:
                            self.Angreifen_ruhig(target)
            else:
                pass
            if befehl1 in range(1,3):
                self.Angreifen_ruhig(target)
            elif befehl1 in range (4,6):
                self.Angreifen_aggressiv(target)
            elif befehl1 in range (7,9):
                self.Angreifen_vorsichtig(target)
            else:
                self.Angreifen_schnell(target)

    def Angreifen_vorsichtig(self, target):
        self.angriffsbonus -= 2
        self.verteidigung += 2
        Textpause()
        print(f"[{self.name} ist vorsichtig.]\n")
        self.Angreifen_ruhig(target)

    def Angreifen_aggressiv(self, target):
        self.angriffsbonus += 2
        self.schadensbonus += 2
        self.verteidigung -= 4
        Textpause()
        print(f"[{self.name} geht aggressiv vor.]\n")
        self.Angreifen_ruhig(target)

    def Angreifen_schnell(self, target):
        Textpause()
        self.schneller_angriff += 1
        self.angriffsbonus -= 4
        self.verteidigung -= 4
        print(f"[{self.name} setzt auf Geschwindigkeit.]\n")
        Textpause()
        self.Angreifen_ruhig(target)

    def Angreifen_ruhig(self, target):
        if self.aktionen_nummer < 2:
            self.angriffsmalus = 5
        Textpause()
        print(f"[{self.name} greift an.]\n")
        self.aktionen_nummer -= 1
        wuerfelwurf = self.Wurf_w12()
        angriffswurf = (wuerfelwurf + self.geschick + self.angriffsbonus + self.stufe) - self.angriffsmalus - self.bewaffnung.angriffsmalus - self.malus_erschoepfung
        angriffsmalus_gesamt = self.angriffsmalus + self.bewaffnung.angriffsmalus + self.malus_erschoepfung
        ziel_verteidigung = target.verteidigung - target.malus_erschoepfung
        self.ausdauer -= 1 + self.panzerung.belastung + self.bewaffnung.belastung
        Textpause()
        print (f"[Ausdauer ({self.name}): {self.ausdauer}/{self.max_ausdauer}]\n")
        Textpause()
        print (f"[Angriff ({self.bewaffnung.name})]\n")
        Textpause()
        print(f"[Angriffsbonus ({self.name}): {self.geschick + self.angriffsbonus + self.stufe}] \n")
        Textpause()
        if self.angriffsmalus > 0:
            print (f"[Angriffsmalus (Folgeaktion): -{self.angriffsmalus}]\n")
            Textpause()
        if self.bewaffnung.besonderheit == "sperrig":
            print (f"[Angriffsmalus ({self.bewaffnung.name}): -{self.bewaffnung.angriffsmalus}]\n")
            Textpause()
            print (f"[Angriffsmalus (gesamt): {angriffsmalus_gesamt}]\n")
            Textpause()
        if self.ausdauer <= 0:
            self.malus_erschoepfung = 4
            print (f"Angriffsmalus (Erschöpfung): -{self.malus_erschoepfung}]\n")
            Textpause()
        else:
            self.malus_erschoepfung = 0
        print(f"[Angriffswurf ({self.name}): {angriffswurf}] \n")
        Textpause()
        if self.ausdauer <= 0:
            print (f"[Verteidigungsmalus (Erschöpfung): -{self.malus_erschoepfung}]\n")
            Textpause()
        print(f"[Verteidigung ({target.name}): {ziel_verteidigung}] \n")
        Textpause()
        if angriffswurf > target.verteidigung or wuerfelwurf == 12: # Hier die Erfolgsrechnung.
                self.Schaden(target)
        elif wuerfelwurf == 1:
            print(f"[{self.name} schwingt kolossal daneben.] \n")
            Textpause()
            print(f"[Deine Ausdauer: {target.ausdauer}/{target.max_ausdauer}]\n")
            Textpause()
            self.ausdauer -=1
            if self.schneller_angriff == 1:
                self.Angreifen_schnell(target)
            elif self.schneller_angriff == 2:
                self.schneller_angriff = 0
                self.Angreifen_ruhig(target)
            else:
                print(f"[{self.name} beendet den Zug.]\n")
                Textpause()
            Begegnung.Kampfschleife()
        elif angriffswurf == target.verteidigung:
            if self.bewaffnung.typ == "Nahkampf":
                Textpause()
                target.Angreifen_gegenangriff(self)
            else:
                self.Schaden(target)
        elif angriffswurf < target.verteidigung - 3:
            print("[Du konntest dem Angriff mühelos ausweichen.] \n")
            Textpause()
            print(f"[Deine Ausdauer: {target.ausdauer}/{target.max_ausdauer}]\n")
            Textpause()
            if self.schneller_angriff == 1:
                self.Angreifen_schnell(target)
            elif self.schneller_angriff == 2:
                self.schneller_angriff = 0
                self.Angreifen_ruhig(target)
            else:
                if self.aktionen_nummer <= 0:
                    print(f"[{self.name} beendet den Zug.]\n")
                    Textpause()
                    Begegnung.Kampfschleife()
                elif self.ausdauer > 5:
                    self.Angreifen_ruhig(target)
                else:
                    print(f"[{self.name} beendet den Zug.]\n")
                    Textpause()
                    Begegnung.Kampfschleife()
        else:
            target.ausdauer -= 1
            print("[Du konntest dem Angriff ausweichen.] \n")
            Textpause()
            print(f"[Deine Ausdauer: {target.ausdauer}/{target.max_ausdauer}]\n")
            Textpause()
            if self.schneller_angriff == 1:
                self.Angreifen_schnell(target)
            elif self.schneller_angriff == 2:
                self.schneller_angriff = 0
                self.Angreifen_ruhig(target)
            else:
                self.Handeln(target)

    def Schaden (self, target):
        print("[ERFOLG] \n")
        Textpause()
        print(f"[Tödlichkeit der Waffe ({self.bewaffnung.name}): {self.bewaffnung.toedlichkeit}]\n")
        Textpause()
        print(f"[Schaden: {self.bewaffnung.schaden}]\n")
        Textpause()
        print(f"[Schaden (gesamt): {self.bewaffnung.schaden + self.schadensbonus}]\n")
        Textpause()
        if target.panzerung.klasse != "ungerüstet":
            target.schutz -= self.bewaffnung.schaden
            if target.schutz > 0:
                print(f"[Rüstung ({target.name}): {target.schutz}/{target.max_schutz}]\n")
                Textpause()
            elif target.panzerung == 0:
                target.lebenskraft -= self.bewaffnung.schaden
                print("[Die Rüstung bietet keinen Schutz mehr] \n ")
                Textpause()
                print(f"[Lebenskraft {target.name}): {target.lebenskraft}/{target.max_lebenskraft}] \n")
                Textpause()
            else:
                target.lebenskraft = (target.lebenskraft + (target.schutz + self.bewaffnung.schaden)) - self.bewaffnung.schaden
                print("[Die Rüstung wurde durchbrochen.] \n")
                Textpause()
                print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}] \n")
                target.schutz = 0
                Textpause()
                if self.schneller_angriff == 1:
                    self.schneller_angriff = 0
                    self.Angreifen_schnell(target)
                else:
                    self.Handeln(target)
        else:
            target.lebenskraft -= self.bewaffnung.schaden
            print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}] \n")
            Textpause()
            if self.schneller_angriff == 1:
                self.schneller_angriff = 0
                self.Angreifen_schnell(target)
            else:
               self.Handeln(target)
            pass

    def Angreifen_gegenangriff(self, target):
        if self.aktionen_nummer < 2:
            self.angriffsmalus = 5
        else:
            self.angriffsmalus = 0
        gegenbefehl1 = random.randint(1, 2)
        if gegenbefehl1 == 1:
            if self.ausdauer <= 3:
                print(f"[{self.name} verzichtet auf einen Gegenangriff.]\n")
                Textpause()
                target.Handeln(self)
            else:
                self.aktionen_nummer += 1
                self.Handeln_angreifen(target)
        if gegenbefehl1 == 2:
            self.aktionen_nummer += 1
            self.Handeln_angreifen(target)

    def Zaubern(self, target):
        zauber = self.Zauber_waehlen()
        if self.zauberkraft - zauber.aufwand_zauberkraft > 0:
            zauber_verstaerkung = self.Zauber_verstaerken()
        else:
            zauber_verstaerkung = 0
        if zauber.aufhebung == "ja":                                                    # Hier die Berechnung des Aufhebungswerts
            zauber.aufhebungswert = self.willen + zauber.erfolgswert
            if zauber.erfolgswert == 5:
                for wuerfel in zauber.schadenswuerfel_anzahl:
                    zauber.aufhebungsbonus = 1
            elif zauber.erfolgswert == 6:
                for wuerfel in zauber.schadenswuerfel_anzahl:
                    zauber.aufhebungsbonus = 2
            else:
                zauber.aufhebungsbonus = 0
        Textpause()
        self.zauberkraft -= zauber.aufwand_zauberkraft
        if zauber_verstaerkung > 0:
            zauber.aufhebungsbonus += zauber_verstaerkung
            self.zauberkraft -= zauber_verstaerkung
            print(f"[{self.name} verstärkt den Zauber mit {zauber.aufhebungsbonus} Punkten Zauberkraft.]\n")
            Textpause()
        print(f"[Aktionsaufwand ({zauber.name}): {zauber.aufwand_aktion}]\n")
        Textpause()
        kontrollwurf = []
        erfolge = []
        print(f"[Erfolgswert ({zauber.name}): {zauber.erfolgswert}]\n")
        Textpause()
        for kontrollwuerfel in range(self.kontrollwuerfel):
            kontrollversuch = self.Wurf_w6()
            Textpause()
            kontrollwurf.append(kontrollversuch)
        kontroll_anzeige = []
        for wurf in kontrollwurf:                                                     # Hier die Formel für die Kontrollwurfanzeige
            kontroll_anzeige = kontrollwurf
            umwandeln = [str(wurf) for wurf in kontroll_anzeige]
            trennzeichen = ", "
            kontroll_anzeige = trennzeichen.join(umwandeln)
        print(f"[Ergebnis (Kontrollwurf): {kontroll_anzeige}]\n")                     # Ende der Kontrollwurfanzeige
        Textpause()
        for wuerfel in kontrollwurf:
            if wuerfel >= 4:
                erfolge.append(wuerfel)
        print(f"[Erfolge (Kontrollwurf): {len(erfolge)}]\n")
        Textpause()
        print(f"[Kontrollwert ({zauber.name}): {zauber.kontrollwert}]\n")
        if len(erfolge) >= zauber.kontrollwert:                                      # Hier die Erfolgsrechnung
            print(f"[{self.name} konnte die erforderliche magische Kraft fokussieren.]\n")
            Textpause()
            target = Maika#self.Ziel_waehlen()         # Hier die Zielauswahl. Momentan nur Maika als Ziel. Verbündete kommen noch.
            if target == Maika:
                print (f"[{self.name} versucht, den Zauber {zauber.name} gegen dich einzusetzen.]\n")
                Textpause()
                gegenzauber = target.Gegenzauber(self)
                Textpause()
                if zauber.aufhebungsbonus > 0:
                    print (f"[{self.name} verstärkt den Zauber mit {zauber.aufhebungsbonus} Punkten Zauberkraft.]\n")
                    Textpause()
                print(f"[Aufhebungswert des Zaubers: {self.willen + zauber.aufhebungswert + zauber.aufhebungsbonus}]\n")
                Textpause()
                if gegenzauber > (self.willen + zauber.aufhebungswert + zauber.aufhebungsbonus):
                    print(f"[Du konntest den Zauber ({zauber.name}) mit einem Gegenzauber unterbinden.]\n")
                    Textpause()
                    Begegnung.Kampfschleife()
                else:
                    if gegenzauber < (self.willen + zauber.aufhebungswert + zauber.aufhebungsbonus) and gegenzauber != 0:
                        print("[Der Zauber ist zu stark für dich und bricht deinen Gegenzauber.]\n")
                    Textpause()
                    angriffswurf = self.Zauber_zielen(target)
                    self.aktionen_nummer -= zauber.aufwand_aktion
                    if angriffswurf >= target.verteidigung:
                        print(f"[Tödlichkeit des Zaubers: {zauber.toedlichkeit}]\n")          # Formel für die Tödlichkeit und den Schaden
                        zauberschaden = []
                        for wuerfel in range(zauber.schadenswuerfel_anzahl):
                            if zauber.schadenswuerfel_groesse == 6:
                                wurf = zauber.Wurf_w6()
                                Textpause()
                            elif zauber.schadenswuerfel_groesse == 8:
                                wurf = zauber.Wurf_w8()
                                Textpause()
                            elif zauber.schadenswuerfel_groesse == 10:
                                wurf = zauber.Wurf_w10()
                                Textpause()
                            elif zauber.schadenswuerf_groesse == 12:
                                wurf = zauber.Wurf_w12()
                                Textpause()
                            elif zauber.schadenswuerfel_groesse == 20:
                                wurf = zauber.Wurf_w20()
                                Textpause()
                            else:
                                zauber.Wurf_w4()
                            zauberschaden.append(wurf)
                            gesamtschaden = sum(zauberschaden)
                            print(f"[Der Zauber ({zauber.name}) trifft {target.name} und richtet {gesamtschaden} Punkte {zauber.schadensart} an.]\n")
                            target.lebenskraft -= gesamtschaden
                            Textpause()
                            print(f"[Lebenskraft ({target.name}): {target.lebenskraft}/{target.max_lebenskraft}]\n")
                            Textpause()
                            if target.lebenskraft <= 0:
                                Begegnung.verbuendete.remove(target)
                                Begegnung.teilnehmer.remove(target)
                                print(f"[{target.name} wurde besiegt.]\n")
                                Textpause()
                            self.Handeln(target)
            else:
                print(f"[{target.name} schafft es, dem Angriff auszuweichen.]\n")
                Textpause()
                self.Handeln(target)
        else:
            self.aktionen_nummer -= zauber.aufwand_aktion
            wurf_nat1 = kontrollwurf.count(1)
            wurf_nat6 = kontrollwurf.count(6)
            wurf_nat1 -= wurf_nat6
            if wurf_nat1 > len(erfolge):
                print(f"[{self.name} versucht, die notwendige Konzentration aufzubringen, verliert aber die Kontrolle über die magischen Ströme.]\n")
                Textpause()
                Textpause()
                print("[Es kommt zu einer Zauberdetonation.]\n")
                Textpause()
                schaden = self.Wurf_zauberdetonation()
                if target.lebenskraft <= 0:
                    Begegnung.gegner.remove(target)
                    Begegnung.verbuendete.remove(target)
                    Begegnung.teilnehmer.remove(target)
                    print(f"[{target.name} wurde besiegt.]\n")
                    Textpause()
                self.Handeln(target)
            else:
                print(f"[{self.name} versucht, zu zaubern, schafft es aber nicht, die notwendige magische Kraft zu fokussieren.]\n")
                Textpause()
                return None

    def Zauber_waehlen(self):
        befehl = random.randint(1,2)
        Textpause()
        for zauber in self.verfuegbare_zauber:
            if befehl == 1:
                zauber = blitz
                Textpause()
                print(f"[{self.name} versucht, {zauber.name} zu wirken.]\n")
                Textpause()
                return blitz
            else:
                zauber = feuerball
                Textpause()
                print(f"[{self.name} versucht, {zauber.name} zu wirken.]\n")
                Textpause()
                return feuerball

    def Zauber_verstaerken(self):
        befehl1 = random.randint (1,12)
        if self.lebenskraft >= 5:
            if self.zauberkraft > 8:
                if befehl1 in range (1,5):
                    befehl2 = random.randint(0,self.zauberkraft)
                    return befehl2
                else:
                    return 0
            else:
                return 0
        else:
            if self.zauberkraft > 5:
                befehl3 = random.randint(5,self.zauberkraft)
                return befehl3
            else:
                return self.zauberkraft

    def Wurf_zauberdetonation(self):
        print("[Die magischen Ströme wirbeln wild umher und explodieren schließlich in einer 9n großen Sphäre aus weiß-blauer Energie, bevor jemand im Wirkungsbereich reagieren kann.]\n")
        Textpause()
        print("[Tödlichkeit (Zauberdetonation): 2W6]\n")
        Textpause()
        wurf1 = self.Wurf_w6()
        Textpause()
        wurf2 = self.Wurf_w6()
        Textpause()
        schaden = wurf1 + wurf2
        print(f"[Schaden: {schaden}]\n")
        Textpause()
        for kaempfer in Begegnung.teilnehmer: # Zauberdetonation im Kampf
            if kaempfer.entfernung <= 9:
                kaempfer.lebenskraft -= schaden
                print(f"[Lebenskraft ({kaempfer.name}): {kaempfer.lebenskraft}/{kaempfer.max_lebenskraft}]\n")
                Textpause()
        return None

    def Zauber_zielen(self, target):
        wurf = self.Wurf_w12()
        zauberverstaerkung = self.Zauber_verstaerken()
        if zauberverstaerkung > 0:
            print(f"[{self.name} verstärkt den Zauberangriff mit {zauberverstaerkung} Punkten Zauberkraft.]\n")
            Textpause()
        angriffswurf = wurf + self.willen + self.waffenfertigkeiten.get("Zauber") + zauberverstaerkung +10
        print(f"[Willen ({self.name}): {self.willen}]\n")
        Textpause()
        print(f"[Zauber-Angriffswurf ({self.name}): {angriffswurf}]\n")
        Textpause()
        if self.aktionen_nummer < 2:
            self.angriffsmalus = 5
            print(f"[Angriffsmalus (Folgeaktion): -{self.angriffsmalus}]\n")
            Textpause()
            print(f"[Angriffswurf (gesamt): {angriffswurf}]\n")
            Textpause()
        print(f"[Verteidigung ({target.name}): {target.verteidigung}]\n")
        Textpause()
        return angriffswurf

Maika = Spieler ("Maika",
                "Mensch",
                "weiblich",
                2,
                4,
                4,
                2,
                6,
                8,
                3,
                "Zauberer",
                9,
                9,
                17,
                17,
                16,
                9,
                0,
                7,
                13,
                7,
                7,
                0,2,0,0,0,0, keine_ruestung, 4, 7, 0,  0, [blitz, feuerball],0, {"Religion": 1, "Magistik": 3, "Linguistik": 3, "Botanik": 1, "Menschenkenntnis": 2}, {"Zauber": 3, "Schwerter": 2}, 0,
                 15, 15, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, False, 5, 5, 5, 5, 5, 5, [],
                 0,0,0, 0)

Murg = Gegner ("Murg",
              "Ork",
                "männlich",
                7,
                4,
                7,
                2,
                6,
                0,
                1,
                "Krieger",
                15,
                15,
                17,
                17,
                20,
                9,
                0,
                7,
                13,
                7,
                7,
              0,
              2,
              2,
              0,
              0,
              0, ruestung_textil, 0, 7, 0,  0, 0, [],1, {}, {}, 0,
               15, 15, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, True, 5, 5, 5, 5, 5, 5, [])

Dorg = Gegner ("Dorg",
              "Ork",
                "männlich",
                7,
                4,
                7,
                2,
                6,
                0,
                1,
                "Krieger",
                15,
                15,
                17,
                17,
                20,
                9,
                0,
                7,
                13,
                7,
                7,
              0,
              2,
              2,
              0,
              0,
              0, ruestung_textil, 0, 9, 0, 0, 0, [blitz, feuerball],1, {},{"Schwerter": 3}, 0,
               15, 15, 10, 10, 10, 5, 5, 5, 5, 5, 10, 10, False, 5, 5, 5, 5, 5, 5, [])


class Kampf:
    def __init__(self, teilnehmer, gegner, verbuendete, letzter_zug, runde, gezielter_angriff):
        self.teilnehmer = []
        self.gegner = []
        self.verbuendete = []
        self.runden_kaempfer = []
        self.letzter_zug = letzter_zug
        self.runde = 0
        self.gezielter_angriff = gezielter_angriff

    def Wurf_w12(self):
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
            wurf = self.Wurf_w12()
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
        self.Runden_zaehler(kaempfer)

    def Runden_zaehler(self, kaempfer):
        self.runde += 1
        for kaempfer in self.teilnehmer:
            kaempfer.verteidigung = 10 + kaempfer.stufe + kaempfer.reflexe - kaempfer.bewaffnung.verteidigungsmalus - kaempfer.wundenmalus
            kaempfer.angriffsbonus = 0
            kaempfer.schadensbonus = 0
            kaempfer.aktionen_nummer = 2
            for zauber in kaempfer.verfuegbare_zauber:
                zauber.aufhebungsbonus = 0
            if kaempfer.lebenskraft <= 0 and kaempfer in self.gegner:
                self.teilnehmer.remove(kaempfer)
                self.gegner.remove(kaempfer)
            if len(self.gegner) == 0:
                print ("[Du hast den Kampf gewonnen.]\n")
                return None
            Textpause()
        print(f"[Runde {self.runde}]\n")
        Textpause()
        self.Kampfschleife()

    def Kampfschleife(self):
        for kaempfer in self.teilnehmer:
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
            print (len(self.gegner))
            if len(self.gegner) > 1:
                aktuelles_ziel = input("[Gib den Namen des Gegners ein, auf den du dich konzentrieren willst.]\n > ")
                print(self.gegner)
                for kaempfer in self.gegner:
                    print(kaempfer.name)
                    if aktuelles_ziel in kaempfer.name:
                        dein_gegner = kaempfer
                        Textpause()
                        print(f"[Du konzentrierst dich auf {dein_gegner.name}]\n")
                        Maika.Handeln_angriff(dein_gegner)
                    else:
                        print("[An deiner Eingabe stimmt etwas nicht, oder der Charakter nimmt nicht am Kampf teil.]\n")
                        Textpause()
                        self.Spieler_zug()
            else:
                for kaempfer in self.gegner:
                    print (f"[{kaempfer.name} ist als einziger Gegner übrig.]\n")
                    Textpause()
                    dein_gegner = kaempfer
                    Maika.Handeln_angriff(dein_gegner)


    def Gegner_zug(self):
        kaempfer = self.letzter_zug
        if kaempfer.aktionen_nummer > 0:
            kaempfer.Handeln(Maika)
        else:
            return None


Begegnung = Kampf([], [], [],0, 0, ["nichts", 0])