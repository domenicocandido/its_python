max:float = float(input("Inserisci un numero: "))
cont = 1

while True:
    cont += 1
    n:float = float(input("Inserisci un numero: "))

    if n > max:
        max = n
    else:
        continue

    if cont == 4:
        break

print(f"Il valore massimo è: {max}")