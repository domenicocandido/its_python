def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    
    prod_prezzo = {}
    
    for prodotto,prezzo in prodotti.items():
        
        if prezzo > 20:
            
            prod_prezzo[prodotto] = prezzo * 0.9
    
    return prod_prezzo

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
