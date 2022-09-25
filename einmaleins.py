eingabe = input("Welche Zahl soll multipliziert werden? ")

int_eingabe = int(eingabe)
multiplikator = 1
gesamt = int(eingabe) * multiplikator

while gesamt <= 100:

    print(gesamt)
    int_eingabe += 1
    gesamt = int_eingabe * multiplikator