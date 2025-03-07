soglia:int = int(input("Inserisci un valore soglia: "))
cont = 0

while cont != 7:
    n:int = int(input("Inserire un numero: "))
    cont += 1
    
    if n > soglia:
        print(f"Il numero {n} è maggiore del valore soglia ({soglia}.)")

        