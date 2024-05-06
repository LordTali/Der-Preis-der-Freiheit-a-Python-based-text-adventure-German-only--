# Importe
from Regeln import Maika
from Waffen import *
import tkinter as tk
import random
from tkinter.scrolledtext import ScrolledText
import sys
from functools import partial
from Handlung import *
import pygame
import mixer

def dialog_auswahl(option):
    anzeige_text.insert(tk.END, option + "\n\n")

def fertigkeitswurf(fertigkeit):
    wurf = Maika.Fertigkeitswurf_ablegen(fertigkeit)
    anzeige_text.insert(tk.END, wurf)

def antworten(option):
    option()
    '''reagieren = dialog_optionen.get(option)
    if reagieren:
        reagieren()'''

# Das eigentliche Hauptfenster
root = tk.Tk()
root.title("Zeit der Zünfte: Der Preis der Freiheit")
root.geometry("1625x980")
root.resizable (width=None, height=None)
root.configure(background='#5d9443')



# Fenster 1 links für die Charaktereigenschaften
fenster_links = tk.Frame(root, bg="white", width=200, height=200)
fenster_links.place(x = 50, y = 200)

# Werte-Fenster 1
wertefenster = tk.Label(fenster_links, text="Maika Sommerfeld", bg="white", fg="black", font=("Helvetica", 16))
wertefenster.grid(row=0, column=0, columnspan=2, pady=10)

# Die eigentlichen Werte
werte = {"Rasse:": Maika.rasse,
"Geschlecht:": Maika.geschlecht,
"Klasse:": Maika.klasse,
"Stufe:": Maika.stufe,
"Kraft:": Maika.kraft,
"Geschick:": Maika.geschick,
"Körperbau:": Maika.koerperbau,
"Grips:": Maika.grips,
"Empathie:":Maika.empathie,
"Magie:": Maika.magie,
"Kontrollwürfel:": Maika.kontrollwuerfel,
"Reflexe:": Maika.reflexe,
"Willen:": Maika.willen,
"Widerstand:": Maika.widerstand,

}
spalte = 1
for wert, hoehe in werte.items():
    wertefenster_wert = tk.Label(fenster_links, text=f"{wert}", bg="white", fg="black", font=("Helvetica", 12), anchor="w")
    wertefenster_wert.grid(row=spalte, column=0)
    wertefenster_hoehe = tk.Label(fenster_links, text=f"{hoehe}", bg="white", fg="black", font=("Helvetica", 12), anchor="e")
    wertefenster_hoehe.grid(row=spalte, column=1, padx= 120)
    spalte +=1

# Fenster 2 links für die Charaktereigenschaften
fenster_links = tk.Frame(root, bg="white", width=410, height=250)
fenster_links.place(x = 50, y = 600)

# Werte-Fenster 2
wertefenster = tk.Label(fenster_links, bg="white", fg="black", font=("Helvetica", 16))
wertefenster.grid(row=0, column=0, columnspan=2)

# Die eigentlichen Werte
werte = {
"Lebenskraft:": Maika.lebenskraft,
"Verteidigung:": Maika.verteidigung,
"Ausdauer:": Maika.ausdauer,
"Zauberkraft:": Maika.zauberkraft,
}
spalte = 1
for wert, hoehe in werte.items():
    wertefenster_wert = tk.Label(fenster_links, text=f"{wert}", bg="white", fg="black", font=("Helvetica", 12), anchor="w")
    wertefenster_wert.grid(row=spalte, column=0, sticky="w")
    wertefenster_hoehe = tk.Label(fenster_links, text=f"{hoehe}", bg="white", fg="black", font=("Helvetica", 12),anchor="e")
    wertefenster_hoehe.grid(row=spalte, column=1, padx= 144)
    spalte +=1

# Fenster 3 links für die Waffenauswahl
fenster_links = tk.Frame(root, bg="white", width=100, height=80)
fenster_links.place(x = 50, y = 775)

# Werte-Fenster 3
wertefenster = tk.Label(fenster_links, bg="white", fg="black", font=("Helvetica", 16))
wertefenster.grid(row=0, column=0, columnspan=2, pady=0)

# Die eigentlichen Werte
werte = {"Waffe:": Maika.bewaffnung.name}
spalte = 1
for wert, hoehe in werte.items():
    wertefenster_wert = tk.Label(fenster_links, text=f"{wert}", bg="white", fg="black", font=("Helvetica", 12), anchor="center")
    wertefenster_wert.grid(row=spalte, column=0)
    wertefenster_hoehe = tk.Label(fenster_links, text=f"{hoehe}", bg="white", fg="black", font=("Helvetica", 12),anchor="center")
    wertefenster_hoehe.grid(row=spalte, column=1, padx= 135)
    spalte +=1

# Titel-Fenster
fenster_oben = tk.Frame(root, bg="white", width=1100, height=100, padx=10)
fenster_oben.place(x=325, y=50)

# Titel im Fenster oben
spieltitel = tk.Label(fenster_oben, text="Zeit der Zünfte: Der Preis der Freiheit", bg="white", fg="black", font=("Old English Text MT", 50))
spieltitel.place(y=5)

# Fenster in der Mitte für Textfeld und Dialogoptionen
fenster_mitte = tk.Frame(root, bg="white", width=400, height=600)
fenster_mitte.place(x=500, y=200)

# Text im Fenster in der Mitte anzeigen
anzeige_text = ScrolledText(fenster_mitte, bg="white", fg="black", font=("Helvetica", 14),  wrap="word")
anzeige_text.pack(expand=True, fill=tk.BOTH)

# Fenster rechts für die Fertigkeiten
fenster_rechts = tk.Frame(root, bg="white", width=250, height=600)
fenster_rechts.place(x=1400, y=200)

# Fertigkeiten einblenden
fenster_fertigkeiten = tk.Label(fenster_rechts, text="Fertigkeiten", bg="white", fg="black", font=("Helvetica", 16))
fenster_fertigkeiten.pack(pady=10)

# Die tatsächlichen Fertigkeiten
fertigkeiten = ["Erkennen", "Tarnung", "Magistik", "Religion", "Menschenkenntnis", "Überreden", "Täuschen", "Orientieung"]
for fertigkeit in fertigkeiten:
    schalflaeche_fertigkeit = tk.Button(fenster_rechts, text=fertigkeit, bg="white", fg="black", font=("Helvetica", 12), command = partial(Maika.Fertigkeitswurf_ablegen, fertigkeit))

# Fenster für die Waffenfertigkeiten
fenster_rechts_unten = tk.Frame(root, bg="white", width=100, height=200)
fenster_rechts_unten.place(x=1400, y=596)

# Werte-Fenster Waffenfertigkeiten
wertefenster = tk.Label(fenster_rechts_unten, text="Waffenfertigkeiten", bg="white", fg="black", font=("Helvetica", 12))
wertefenster.place(x=1400, y=200)

# Die eigentlichen Fertigkeiten
kampf_fertigkeiten = {"Magistik": 3, "Schwerter": 1}
spalte = 1
for kampf_fertigkeit, punktzahl in kampf_fertigkeiten.items():
    wertefenster_kampf_fertigkeiten = tk.Label(fenster_rechts_unten, text=f"{kampf_fertigkeit}", bg="white", fg="black", font=("Helvetica", 12), anchor="w")
    wertefenster_kampf_fertigkeiten.grid(row=spalte, column=0)
    wertefenster_kampf_fertigkeiten = tk.Label(fenster_rechts_unten, text=f"{punktzahl}", bg="white", fg="black", font=("Helvetica", 12), anchor="e")
    wertefenster_kampf_fertigkeiten.grid(row=spalte, column=1, padx=45)
    spalte += 1


# print()-GUI-Übersetzer
class Print_zu_gui:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write (self, text):
        self.text_widget.insert(tk.END, text)

    def flush(self):
        pass

# Redirect stdout
sys.stdout = Print_zu_gui(anzeige_text)


# Dialogfenster
fenster_dialog = tk.Frame(fenster_mitte, width= 400,bg="#74b953")
fenster_dialog.pack(side=tk.BOTTOM, pady=20)


# Dialogoptionen

dialog_optionen = {"Loslegen": prolog_1, "Mehr erfahren": dialog_regeln}
anzeige_text.insert(tk.END, ("Willkommen bei 'Der Preis der Freiheit', einem Textabenteuerspiel in der Welt von 'Zeit der Zünfte' von Vitali Hänisch.\n\n"))
Textpause()
anzeige_text.insert(tk.END, ("Du kannst direkt mit dem Abenteuer loslegen oder zunächst mehr über die Regeln erfahren. Klicke dazu einfach auf die entsprechende Schaltfläche.\n\n"))
for dialogoption, reaktion in dialog_optionen.items():
    schalflaeche_dialog = tk.Button(fenster_dialog, text=dialogoption, bg="white", fg="black", font=("Helvetica", 12), command=lambda option =reaktion: antworten(option))
    schalflaeche_dialog.pack(side=tk.TOP, padx=10, pady=5)



def dialog_aktualisieren(neue_optionen):
    dialog_optionen.clear()
    dialog_optionen.update(neue_optionen)
    schaltflaechen_aktualisieren()

# Dialogobuttons aktualisieren

def schaltflaechen_aktualisieren():
    for widget in fenster_dialog.winfo_children():
        widget.destroy()

    for dialogoption, reaktion in dialog_optionen.items():
        schaltflaeche_dialogoption = tk.Button(fenster_dialog, text=dialogoption, bg="white", fg="black", font=("Helvetica", 12), command=lambda option = reaktion: antworten(option))
        schaltflaeche_dialogoption.pack(padx=10, pady=5)


def dialog_uebertragen(dialog):
    for zeile in dialog:
        anzeige_text.insert(tk.END, zeile + "\n\n")
        Textpause()


# Fenster starten

root.mainloop()
