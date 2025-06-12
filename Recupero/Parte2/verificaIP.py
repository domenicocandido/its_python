import string

def verifica_ip(ip:str) -> bool:

    ip = ip.split(".")
    
    if len(ip) != 4:
        return False
    try:
        numeri = [int(n) for n in ip]
    except ValueError:
        print("Indirizzo Ip non valido")
        return False
        

    if 0 <= numeri[0] <= 255:
        if 0 <= numeri[1] <= 255:
            if 0 <= numeri[2] <= 255:
                if 0 <= numeri[3] <= 255:
                    return True

    return False

print(verifica_ip("123.123.0.0"))