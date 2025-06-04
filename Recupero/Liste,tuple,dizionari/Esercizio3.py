def aumento(dizionario:dict[str, float]) -> dict[str, int|float]:

    for prodotto, prezzo in dizionario.items():

        if prezzo < 50:

            prezzo += (prezzo * 10 )/100
            dizionario[prodotto] = float(f"{prezzo:.2f}")
        
        else:
            continue
        
    return dizionario




        