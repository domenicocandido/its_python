def check(X:bool, Y:bool, Z:bool) -> str:

    if X and (Y or Z):
        return("Azione permessa.")
    else:
        return("Azione negata.")


combinazioni = [
    (True, True, False),   
    (True, False, True),   
    (True, False, False),  
    (False, True, True),   
    (False, False, False), 
]

for x, y, z in combinazioni:
    risultato = check(x, y, z)
    print(f"X={x}, Y={y}, Z={z} ➜ {risultato}")
