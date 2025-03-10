max_posti:int = int(input("Inserire numero posti: "))
liberi = max_posti

while True:
    
    opzione:str = input("Inserire un'opzione: ")

    match opzione:

        case "ingresso":
            if liberi > 0:
                liberi -=1
            else:
                print("Non ci sono posti disponibili")
        
        case "uscita":
            if liberi < max_posti:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili.")
        
        case "stato":
            print(f"I posti liberi sono: {liberi}")
            print(f"I posti occupati sono:{max_posti - liberi}")
        
        case "esci":
            print("Uscita dal sistema.")
            break

        case _:
            print("Inserire un'opzione valida")
            