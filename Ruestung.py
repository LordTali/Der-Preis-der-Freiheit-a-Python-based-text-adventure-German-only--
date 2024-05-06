class Ruestung:
    def __init__(self, name, klasse, panzerung_kopf, panzerung_torso, panzerung_arm_links, panzerung_arm_rechts, panzerung_bein_links, panzerung_bein_rechts, max_panzerung, gewicht, belastung, schadensreduzierung):
        self.name = name
        self.klasse = klasse
        self.panzerung_kopf = panzerung_kopf
        self.panzerung_torso = panzerung_torso
        self.panzerung_arm_links = panzerung_arm_links
        self.panzerung_arm_rechts = panzerung_arm_rechts
        self.panzerung_bein_links = panzerung_bein_links
        self.panzerung_bein_rechts = panzerung_bein_rechts
        self.max_panzerung = max_panzerung
        self.gewicht = gewicht
        self.belastung = belastung
        self.schadensreduzierung = schadensreduzierung

keine_ruestung = Ruestung ("Ungerüstet", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


ruestung_textil = Ruestung ("Textilrüstung",
                             "leicht",
                             0,
                             20,
                             20,
                             20,
                             0,
                             0,
                             20,
                             3.5,
                             0, 0)


