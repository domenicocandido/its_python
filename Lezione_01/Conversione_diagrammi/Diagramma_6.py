

while True:

    n:int = int(input("Inserire un numero: "))
    
    if n >= 0:
        break
    print("Il numero deve essere positivo")

fattoriale = 1

for i in range(1, n + 1):
    
    fattoriale *= i
        
print(fattoriale)



