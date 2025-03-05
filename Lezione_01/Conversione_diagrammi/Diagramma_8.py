soglia:int = int(input("Inserisci un valore soglia: "))
cont = 0

while cont < 7:
    n:int = int(input("Inserie un numero: "))

    if n > soglia:
        print(f"Il numero {n} è maggiore del valore soglia ({soglia}.)")
    else:
        cont += 1

    