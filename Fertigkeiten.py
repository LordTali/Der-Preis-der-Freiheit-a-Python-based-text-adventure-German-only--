class Fertigkeiten():
    def __init__ (self, name, attribut, schwierigkeit_sehr_leicht, schwierigkeit_leicht, schwierigkeit_mittel, schwierigkeit_schwer, schwierigkeit_sehr_schwer):
        self.name = name
        self.attribut = attribut
        self.schwierigkeit_sehr_leicht = schwierigkeit_sehr_leicht
        self.schwierigkeit_leicht = schwierigkeit_leicht
        self.schwierigkeit_mittel = schwierigkeit_mittel
        self.schwierigkeit_schwer = schwierigkeit_schwer
        self.schwierigkeit_sehr_schwer = schwierigkeit_sehr_schwer


    def Fertigkeiten_hinzufuegen(self, charakter):
        attribut_kraft = ["Drohen"]
        attribut_geschick = ["Schwimmen", "Sportlichkeit", "Reiten", "Tarnung"]
        attribut_empathie = ["Magistik", "Menschenkenntnis", "Religion", "Täuschen", "Überreden", "Verführen", "Zauber"]
        attribut_grips = ["Botanik", "Kulturkunde", "Sprachen", "Erkennen", "Linguistik", "Mechanik", "Orientierung","Weltwissen", "Elektrik"]
        liste = attribut_kraft, attribut_geschick, attribut_empathie, attribut_grips
        for fertigkeit in liste:
            if fertigkeit in liste:
                charakter[fertigkeit] = Charakter(name=fertigkeit, amount=1)


attribut_kraft = ["Drohen"]
attribut_geschick = ["Schwimmen", "Sportlichkeit", "Reiten", "Tarnung"]
attribut_empathie = ["Magistik", "Menschenkenntnis", "Religion", "Täuschen", "Überreden", "Verführen", "Zauber"]
attribut_grips = ["Botanik", "Kulturkunde", "Sprachen", "Erkennen", "Linguistik", "Mechanik", "Orientierung","Weltwissen", "Elektrik"]