def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    
    nome_voti = {}
    
    for voto in voti:
        
        nome = voto["nome"]
        valutazione = voto ["voto"]
        
        if nome in nome_voti:
            
            nome_voti[nome].append(valutazione)
        else:
            
            nome_voti[nome] = [valutazione]
    
    return nome_voti
    
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([])) 
