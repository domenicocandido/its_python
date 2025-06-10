def prime_factors(n:int) -> list[int]:    
    """
    Restituisce una lista dei fattori primi del numero intero positivo n.
    """
    fattori = []
    divisore = 2
    while n > 1:
        while n % divisore == 0:
            fattori.append(divisore)
            n = n // divisore
        divisore += 1
    return fattori

print(prime_factors(60))