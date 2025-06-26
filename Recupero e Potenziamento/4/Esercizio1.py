import math

h:int = int(input("Inserire ore del parcheggio: "))

def calculateCharges(hParcking:int):

    tariffa:int = 0

    if h <= 3:
        tariffa = 2
    elif 3 < h < 24 :
        hParcking = math.ceil(hParcking)
        tariffa =  (2 + (hParcking - 3) * 0.5)
    else:
        tariffa = 10
    return tariffa
    
print(calculateCharges(h))


clienti:list[int] = [1.5, 4, 5.50, 24.0]

print(f"{'Car':<10} {'Hours':<10} {'Charge':<10}")

totale:int = 0

for item in clienti:
    
    conto:int = calculateCharges(item)
    totale += 10

    print(f"{clienti.index(item)+1:<10} {item:<10} {conto:.2f} $")

print(f"{'TOTAL':<10} {sum(clienti):<10} {totale:.2f} $")