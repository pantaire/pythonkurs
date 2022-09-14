gaeste = int(5)
personen = gaeste + 1 #Gastgebi will auch Snacks :)

kuchen = input("wie viel Kuchen? ")
kekse  = input("wie viele Kekse? ")

#nur zum Nachvollziehen, was der Input war
print(kuchen,kekse)

# genug Snacks:
# jeder gleich viel Kuchen (Modulo 0, kein Rest -> wird zu true)
# UND mehr als 0 Kuchen
# ODER mehr als 30 Kekse 
if int(kuchen)%personen == 0 and int(kuchen) > 0 or int(kekse) > 30:
    print("Die Party kann losgehen!")
# nicht genug Snacks
else:
    print("Lieber nochmal einkaufen...")