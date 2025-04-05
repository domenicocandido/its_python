def prime_factors(n: int) -> list[int]:
    
    divisori = []
    i = 2
    
    while i <= n:
        
        if n % i == 0:
            divisori.append(i)
            n = n // i
        
        else:
            i += 1
    
    return divisori

print(prime_factors(4))
print(prime_factors(60))
