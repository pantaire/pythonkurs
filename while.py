# erste While-Schleife am Beispiel einer Obstschale

hatnochplatz = True
obstschale = ("apfel", "banane", "pfirsich", "ananas")
verfuegbarerplatz = 100

while hatnochplatz:
    print("Inhalt der Obschale): ", obstschale)
    #noch nicht voll (weniger als 10 Obst), deswegen fügen wir einen Apfel hinzu
    #nur Tupel können an Tupel gehängt werden, deswegen Klammer und Komma bei Apfel
    obstschale = obstschale + ("apfel",)
    print("Hab noch was reingetan, Inhalt: ", len(obstschale))

    #Warnung, wenn der Platz knapp wird
    if(verfuegbarerplatz - len(obstschale) <= 2):
        print("Langsam wird der Platz knapp!")
    
    #Abbruch, sobald die Schale voll ist
    if len(obstschale) >= verfuegbarerplatz:
        hatnochplatz = False
        print("Jetzt ist die Schale voll.")
