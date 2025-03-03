n:int = int(input("Inserire un numero: "))

if n < 2:
    print("Il numero non è primo.")
else:
    div = 2
    
    
while div < n:

    if n % div == 0:
        print(f"{n} non è primo")
    else:
        div +=  1

print(f"{n} è primo.")