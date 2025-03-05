even = 0
odd = 0
cont = 0

while cont < 10:

    n:int = int(input("Inserire un numero: "))

    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    
    cont += 1

print(f"I numeri pari sono: {even}.")
print(f"I numeri dispari sono: {odd}.")