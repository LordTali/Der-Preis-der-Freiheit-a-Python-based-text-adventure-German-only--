import time
import tkinter as tk
import pygame
import mixer

def Textpause():
    time.sleep(0.8)

pygame.mixer.init()
def verzoegerung (zeilen, index):
    from ZdZ_GUI import root, anzeige_text
    if index < len(zeilen):
        anzeige_text.insert(tk.END, zeilen[index] + "\n")
        anzeige_text.see(tk.END)
        anzeige_text.update()
        root.after(1000, verzoegerung, zeilen, index + 1)


def spielstart():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    zeilen = ["Willkommen bei 'Der Preis der Freiheit', einem Textabenteuerspiel in der Welt von 'Zeit der Zünfte' von Vitali Hänisch.\n\n",
            "Du kannst direkt mit dem Abenteuer loslegen oder zunächst mehr über die Regeln erfahren. Klicke dazu einfach auf die entsprechende Schaltfläche.\n\n"
              ]
    verzoegerung (zeilen, 0)

    #dialog_aktualisieren({"Loslegen": prolog_1(), "Mehr erfahren": dialog_regeln()})

def dialog_regeln():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    print("'Der Preis der Freiheit' ist ein Textabenteuerspiel.\n")
    Textpause()
    print ("Du schlüpfst dabei in die Rolle von Maika Sommerfeld - einer Frau, die nach vielen Jahren in ihr Heimatdorf zurückkehrt.\n")
    Textpause()
    print ("Was wird dort passieren?\n")
    Textpause()
    print("Beginne das Spiel und finde es heraus!\n")
    Textpause()
    print("In diesem Spiel wirst du oft aufgerufen, eine Entscheidung oder eine Dialogption auszuwählen und auf die entsprechendende Schaltfläche zu klicken.\n")
    Textpause()
    print("Meistens wirst du keine vollen Antworten bekommen, die Optionen werden dir aber grob verraten, wie Maika auf die jeweilige Situation reagiert.\n")
    Textpause()
    print("Die Geschichte entwickelt sich deinen Reaktionen entsprechend. Wie sie Geschichte ausgeht, hängt von deinen Antworten und dem Würfelglück ab.\n")
    Textpause()
    print("Im Verlauf der Geschichte lernst du einen Charakter auch ein Stück weit kennen, und kannst ihn auch gewissermaßen formen. Überlege dir also gut, was du tust.\n")
    Textpause()
    print("An mehreren Stellen wirst du zudem aufgerufen oder hast die Möglichkeit, einen Fertigkeitswurf abzulegen. Maika hat nämlich eine Ausbildung genossen und hat Einiges drauf.\n")
    Textpause()
    print("Dazu würfelst du einen 12-seitigen Würfel und addierst verschiedene Boni. Das Ergebnis, und damit der Erfolg, hängt davon ab, ob dein Wurf einen bestimmten Wert erreicht.\n")
    Textpause()
    print("Es gibt noch weitere Regeln, aber die gehen wir durch, wenn es soweit ist.\n")
    Textpause()
    print("Und nun: Klicke auf 'Spiel starten', such dir eine angenehme Sitzposition und tauche ab in die Geschichte. Der Entwickler dieses Spiels wünscht dir viel Spaß!\n")
    dialog_aktualisieren({"Spiel starten": prolog_1})

def prolog_1():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    anzeige_text.insert(tk.END, ("Der Nebel vor deinen Augen scheint sich langsam zu lichten.\n"))
    anzeige_text.insert(tk.END, ("Es dauert einen Moment, aber langsam begreifst du, wo du bist.\n"))
    dialog_aktualisieren({"Auf einer grünen Wiese": prolog_wiese1, "Auf einem leeren Feld": prolog_feld1, "In einer Höhle": prolog_hoehle1, "Vor einem großen Haus": prolog_haus1, "In einer gähnenden schwarzen Leere": prolog_leere1})

def prolog_wiese1():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    from Regeln import Maika
    Maika.hoffnung +=1
    zeilen = [
        "Vor dir ersteckt sich eine große, ja gar scheinbar unendliche, grüne Wiese.\n",
        "Die Sonne steht hoch, es wird wohl in etwa Mittag sein. Ein angenehm warmer Frühlingsmittag noch dazu.\n",
        "Du versuchst dich fieberhaft daran zu erinnern, wie du hierher gekommen bist, aber du kommst einfach nicht drauf.\n",
        "Zumindest wirkt deine Umgebung sehr friedlich. Der Wind weht leise durch hohe Gras, irgendwo in der Ferne zwitschern die Vögel.\n",
        "Eine Idylle, würden Viele Menschen sagen. Unter anderen Umständen hättest du ihnen vermutlich sogar zugestimmt.\n"
        ]
    verzoegerung(zeilen, 0)
    pass

def prolog_feld1():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    from Regeln import Maika
    Maika.trauer += 1
    zeilen = [
        "Vor dir ersteckt sich ein großes Feld.\n",
        "Einmal wuchs hier sicherlich etwas, doch was immer es war, das Feld ist längst gemäht bar jeden Lebens, wie es scheint.\n",
        "Du versuchst dich fieberhaft daran zu erinnern, wie du hierher gekommen bist, aber du kommst einfach nicht drauf.\n",
        "Die Sonne ist längst untergegangen, aber die Abenddämmerung spendet noch genug Licht, um deine Umgebung wahrzunehmen.\n",
        "Nicht, dass es hier viel zu entdecken gäbe. Deine Umgebung besteht aus verschiedenen Grau- und Brauntönen.\n",
        "Eine durchaus hässliches Bild, würden Viele Menschen sagen. Unter anderen Umständen hättest du ihnen vermutlich sogar zugestimmt, in diesem Augenblick findest du diese Aussicht aber auch irgendwie beruhigend.\n",
        "Wenn der duchs Feld wehende Herbstwind nur nicht so kalt wäre!\n \n"
    ]
    verzoegerung(zeilen, 0)
    pass

def prolog_hoehle1():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    from Regeln import Maika
    Maika.angst +=1
    zeilen = [
        "Du findest dich in einer großen Höhle wieder, durchzogen vom Säuseln des Winds und Geräuschen tropfenden Wassers.\n",
        "Wie es scheint, bist du hier ganz allein, es sei denn, man zählt die Moosbestände zum einheimischen Leben.\n",
        "Du kannst dich sagen, wie spät es gerade sein soll, oder wie du überhaupt hierhergekommen bist. Aus irgendeinem Grund kannst du deine Umgebung aber trotzdem noch gut genug wahrnehmen.\n",
        "Nicht, dass es hier viel zu entdecken gäbe. Deine Umgebung besteht aus verschiedenen Grautönen. Hier und da siehst du etwas Moosgrün, im Großen und Ganzen zählt das aber nicht.\n",
        "Man kann sich sicherlich darüber streiten, was man von Höhlen allgemein halten soll. Es gibt Menschen, und nicht nur sie, die eine solche Umgebung beruhigend oder gar angenehm finden. Und du kannst darauf wettern, dass Zwerge oder Dunkelelfen da zustimmen würden!\n",
        "Du gehörst ganz sicher nicht dazu.\n",
        "Du verstehst dich, warum, aber du hast Angst. Panische Angst.\n",
        "Dennoch tragen dich deine Beine weiter. \n \n"
    ]
    verzoegerung(zeilen, 0)
    pass

def prolog_leere1():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    from Regeln import Maika
    zeilen = [
        "Genauer genommen siehst du aber, dass du nichts siehst. Alles, was du wahrnimmst, ist Schwarz.\n",
        "Ein endloses, unnachgiebiges, erdrückendes Schwarz.\n"
        "Du vestehst nicht, wo du bist oder wie du hierher gekommen bist. Und genauso wenig ist dir klar, was du von dieser Umgebung halten solst.\n",
        "Nach einiger Zeit begreifst du aber, dass die Vorstellung, du würdest nichts sehen, falsch ist. Dieses endlose Schwarz ist nicht die Abwesenheit von Licht oder ein Problem mit deinem Augenlicht.\n"
        "Diese schwarze Leere ist deine Umgebung, und du kannst sie deutlich sehen. Wie ist das möglich?\n",
        "Du bist hier ganz allein, und alles, was du hörst, ist dein eigener Herzschlag. Vielleicht noch dein Atem.\n",
        "Dennoch tragen dich deine Beine weiter, und wie es scheint, ist diese Leere genauso dein Boden wie die Wände, die Decke und die Abwesenheit von Raum. \n \n"
    ]
    verzoegerung(zeilen, 0)

    pass

def prolog_haus1():
    from ZdZ_GUI import dialog_aktualisieren, schaltflaechen_aktualisieren, anzeige_text
    from Regeln import Maika
    Maika.wut +=1
    zeilen = [
        "Du stehst vor einem großen und reichlich dekorierten Haus\n",
        "Es kommt dir bekannt vor, aber du kannst dich weder daran erinnern, wem es gehört, noch wie du hierhergekommen bist.\n",
        "Hinter dem Haus siehst du einen großen runden Vollmond, das die Umgebung in ein blasses weißes Licht taucht.\n",
        "Viele Menschen würden diese Aussicht möglicherweise als schön, beruhigend, vielleicht auch als beängstigend empfinden. Unter anderem Umständen hättest du ihnen vermutlich sogar zugestimmt.\n",
        "Moment empfindest beim Anblick dieses Hauses aber nur ein Gefühl: Wut.\n",
        "Du kannst es dir nicht erklären, aber du kannst nichts außer Verachtung und regelrechte Raserei für dieses Huas empfinden - und genau so für seinen Besitzer.\n",
        "Dein Blick fällt auf die große rote Eingangstür, die meisterhaft in die Wand aus ganzen Eichenstämmen eingearbeitet ist. \n \n"
    ]
    verzoegerung(zeilen, 0)
    pass
