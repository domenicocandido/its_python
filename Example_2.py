def sumInRange (a:int, b:int) -> int:

    if a > b:
        temp:int = a
        a = b
        b = temp
    
    somma = 0
    while b >= a:
        somma += b
        b -= 1

    return somma

print(sumInRange(5,10))
    





