def ricercaBinaria(numeri:list[int], numero:int) -> bool:

    numeri.sort()
    inizio = 0
    fine = len(numeri) - 1

    while inizio <= fine:

        centro = (inizio + fine) // 2
        
        if numeri[centro] == numero:
            return True
        elif numeri[centro] < numero:
            inizio = centro + 1
        elif numeri[centro] > numero:
            fine = centro - 1

    return False
        
print(ricercaBinaria([1,4,3,12,56,7, 91, 84, 59,16], 16))