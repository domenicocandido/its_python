n:int = int(input("Inserire un numero: "))

if n > 0:
    if n == 1:
        print("1st")
    elif n == 2:
        print("2nd")
    elif n == 3:
        print("3rd")
    elif n > 3:
        print(f"{n}th")
else: 
    print("Il numero non è pari.")