a:int = int(input("Inserire un numero: "))
b:int = int(input("Inserire un numero: "))

while True:
    
    if a < b:
        if a > 0 and b > 0:
            if a % 1 == 0 and b % 1 == 0:
                somma = 0
                i = a
                
                while i <= b:
                    somma += i
                    i +=  1
                print(somma)
                break
            else:
                print("A e B devono essere interi.")
                break
        
        else:
            print("A e B devono essere positivi.")
            break
    
    else:
        print("A deve essere minore di B.")
        break
        
    