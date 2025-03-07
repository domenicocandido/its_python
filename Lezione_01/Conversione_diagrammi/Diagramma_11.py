from re import match


liberi:int = 20
opzione:str = input("Inserire un'opzione: ")

while True:
    
    opzione:str = input("Inserire un'opzione: ")

    match opzione:
        case "prenota":
            if liberi > 0:
                liberi = liberi - 1
            
            else:
                print("Non ci sono posti liberi")
        case "libera":
            if liberi < 20:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili.")
    
        case "visualizza":
            print(f"I posti liberi sono: {liberi}")
            print(f"I posti occupati sono:{20 - liberi}")
    
        case "esci":
            print("Uscita dal sistema.")
            break

        case _:
            print("Inserire un'opzione valida")

            

