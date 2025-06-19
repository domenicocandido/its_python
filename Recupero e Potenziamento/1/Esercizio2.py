while True:
    x:float = float(input("Inserire un numero intero positivo: "))
    if x.is_integer():
        break
    else:
        print("Il numero deve essere un intero")
n = None
while n != 0:

    sequenza:list[int] = []

    n:float = float(input("Inserire un numero intero positivo: "))
    if n.is_integer():
        sequenza.append(n)
    else:
        print("Il numero deve essere un intero")
print(sequenza)
somma = 0
prima_appar = 0
for n in sequenza:
    cont = 0
    
    if n in sequenza:
        cont += 1
        if cont == 0:
            prima_appar = n
    
print(f"Il numero {n} compare {cont} volte nella sequenza")
print(f"Il numero {n} compare per la prima volta in posizione {prima_appar} nella sequenza")

if n != x:
    somma += n


    
