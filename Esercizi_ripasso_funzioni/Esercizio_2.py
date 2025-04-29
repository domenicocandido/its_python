def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:

    dizionario_invertito = {}
    for key,value in dizionario.items():

        if value not in dizionario_invertito:
            dizionario_invertito[value] = key
        
    return dizionario_invertito

print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
print(inverti_mappa({}))

print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))
