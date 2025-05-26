import math

def safe_sqrt(number:int) -> float|str :

    try:
        return math.sqrt(number)
    except ValueError:
        return"Errore: impossibile calcolare la radice di un numero negativo."

    
print(safe_sqrt(5))
print(safe_sqrt(-1))