n:int = int(input("Inserire un numero: "))
i = 0

while i <= n:

    x:int = int(input("Inserire valore di X: "))
    y:int = int(input("Inserire valore di Y: "))

    if x > 0 and y > 0:
        result = x * y
        
        print(f"Il prodotto tra {x} e {y} è {result}")
    else:
        if x <0 and y > 0:
            print("Errore.")
        
        else:
            result = x - y

            print(f"La differenza tra {x} e {y} è {result}")
    
    i += 1


