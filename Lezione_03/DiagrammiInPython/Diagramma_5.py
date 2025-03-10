n:int = int(input("Inserire un numero intero positivo: "))

if n % 1 == 0 and n > 0:
    sum = 0
    i = 1
    if i > n:
        print(sum)
    else:
        sum = sum + i*i
        i += 1
else:
    print("Errore, n deve essere positivo.")    