x:int =  int(input("Inserire un numero positivo: "))

if x > 0:
    i = 0
    somma = 0
    while i < 10:

        n:int = int(input("Inserire un numero positivo o negativo: "))
        i +=  1

        if x % 2 == 0:
            if n > x/2:
                somma =  somma + n
        else:
            if n < x:
                somma = somma + n

    print(somma)
else:
    print("errore, x deve essere positivo.")
