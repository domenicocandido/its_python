def build_profile(nome:str, cognome:str, età:int, città:str, occupazione:str) -> str:
    profile = {

        "nome" : nome,
        "cognome" : cognome,
        "anni" : età,
        "citta" : città,
        "occupazione" : occupazione   
    }
    
    return (f"{nome}, {cognome}, {età}, {città} e {occupazione}.")

dati = build_profile("Domenico", "Candido", 19, "Caserta", "Studente")
print(dati)