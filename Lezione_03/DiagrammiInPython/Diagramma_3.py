nome_corso:str = input("Inserire il nome del corso: ")
max_posti = 100

while True:

    opzione:str = input("Inserire un'opzione: ")

    match opzione.lower():
        
        case "iscrivi":
            if max_posti > 0:
                max_posti -= 1
            else:
                print("Non ci sono posti disponibili.")

        case "annulla":
            if max_posti < 100:
                max_posti += 1
            else:
                print("Tutti i posti sono già disponibili.")
        
        case "visualizza":
            print(f"I posti liberi sono: {max_posti}")
            print(f"I posti occupati sono: {100 - max_posti}")
        
        case "elimina":
            continue
        
        case "esci":
            break

        case _:
            print("Inserire un'opzione valida.")