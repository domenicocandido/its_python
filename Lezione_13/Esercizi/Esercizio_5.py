def armonica(n:float) -> float:

    if n == 1:
        return 1
    else:
        return round(1/n * armonica(n-1),6)

print(armonica(6))    

