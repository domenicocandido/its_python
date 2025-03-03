max:float = float(input("Inserisci un numero: "))
cont = 0

for i in range(3):
    cont += 1
    n:float = float(input("Inserisci un numero: "))

    if n > max:
        max = n
    else:
        continue

print(f"Il valore massimo è: {max}")