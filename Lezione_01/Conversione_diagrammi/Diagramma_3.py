sum = 0
cont = 0

while True:
    n:float = float(input("Inserire un numero: "))
    
    if n > 0:
        sum += n

    cont += 1

    if cont == 5:
        break
        
        
print(f"La somma dei numeri positivi è: {sum}")
