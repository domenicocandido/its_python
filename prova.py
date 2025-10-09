def prova(nums: list[float]) -> float:
    
    if not nums:

        raise ValueError("Lista vuota")
    
    else:

        media = sum(nums) / len(nums)
        somma = 0

        for n in nums:
            somma += ((n- media)**2)
        varianza = somma / len(nums)
        dev_sta = varianza ** 0.5

    return round(dev_sta, 2)
    
    
print(prova([1.0, 2.0, 3.0, 4.0, 5.0]))