
while True:

    n:float = float(input("Inserire un numero intero: "))

    if n % 1 == 0:
        if n % 2 == 0 and n > 10:
            print("Numero valido.")
            break
    
        else:
            print("Numero non valido.")
            break
    else:
        continue