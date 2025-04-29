def calcola_stipendio(ore_lavorate: int) -> float:
    
    if ore_lavorate <= 40:
        stipendio = ore_lavorate * 10
        return stipendio
    elif ore_lavorate > 40:
        stipendio = (ore_lavorate - 40) * 15 + 400
        return stipendio

print(calcola_stipendio(45))
print(calcola_stipendio(0))


