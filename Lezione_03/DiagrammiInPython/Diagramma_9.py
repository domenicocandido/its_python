n:int = int(input("Inserire un numero intero: "))

if n > 0:
    if n % 1 == 0:
        cont = 0
        i = 0
        
        for i in range (10):
            x:int = int(input(f"Inserire il {i+1}° numero: "))

            if x % n == 0:
                cont += 1
            else:
                continue
            
            i += 1
        print(f"I numeri inseriti divisibili per {n} sono {cont}.")    
else:
    print("Il numero deve essere positivo.")
        