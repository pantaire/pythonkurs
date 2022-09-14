geheimes_wort = "Luftschloss"
angezeigtes_wort = ___________"

versuch = input("Rate einen Buchstaben in diesem Wort: " + angezeigtes_wort)
# erstmal sichergehen, dass es nur ein Buchstaben war
if len(versuch) > 1
    print("Bitte gib nur einen Buchstaben ein!")
else:
    if versuch in geheimes_wort: # Das ist erlaubt! "in" ist ein "membership operator". Das Gegenteil ist "not in"...
        print("Der Buchstabe kommt im Wort vor.")
    else:
        print("Probiers noch einmal")
