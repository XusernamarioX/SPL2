eingabe = input("Bitte Anzahl der Haltestellen eingeben:")
eingabe = int(eingabe)
for i in range(1,eingabe+1):
    eingabe2 = input("Bitte personen eingeben:")
    eingabe2 = eingabe2
    eingabe3 = input("Steigen welche aus?")
    aussteigen = eingabe2-eingabe3
    print("Bei ",eingabe , " Haltestellen sind ",eingabe2 , " Personen eingestiegen")
    if(eingabe2 == 60):
        print("Bus voll!")
