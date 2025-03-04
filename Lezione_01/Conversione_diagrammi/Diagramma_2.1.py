max:float = float(input("Inserisci un numero: "))
cont = 1

while cont < 4:
    cont += 1
    n:float = float(input("Inserisci un numero: "))

    if n > max:
        max = n
    else:
        continue

print(f"{max}")