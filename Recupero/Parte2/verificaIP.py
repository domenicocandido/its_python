def verifica_ip(ip:str) -> bool:

    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:

        if not part.isdigit():
            
            print("Indirizzo IP non valido")
            return False
        number = int(part)
        if number < 0 or number > 255:
            return False

    return True

print(verifica_ip("123.123.0.0"))