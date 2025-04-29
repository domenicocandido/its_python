def integerPower(base:int, esponente:int) -> int:

    i = 1
    result = base
    while True:
        result *= base
        i += 1
        if i == esponente:
            return result
    
        
        
        
print(integerPower(3, 4))
print(integerPower(2, 5))

