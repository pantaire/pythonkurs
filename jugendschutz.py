#bisschen Freestyle - Piko hat uns aufgefordert, selbst zu experimentieren :)

fragen = ("wie heisst du?", "wie alt bist du?", "wo wohnst du?")
nummer = input("Welche Frage willst du? Gib Nummer von 1-"+ str(len(fragen)))

prnt = int(nummer)
print (fragen[prnt])

#Problem: tupel können 
appendfrage = (input("Füge eine Frage hinzu:"))
fragen = fragen + appendfrage
print(fragen)