def baricentro(v:list[int]) -> int|None:

    if v:
        puntoM = len(v)//2
        sommaA = sum(v[:puntoM+1])
        sommaB = sum(v[puntoM+1:])

    if sommaA == sommaB:
        return puntoM
    else:
        return None

v = [1, 2, 3, 3, 2, 1]
print(baricentro(v))