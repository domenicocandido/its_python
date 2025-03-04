a:float = float(input("Inserire la misura dell'ipotenusa: "))
b:float = float(input("Inserire la misura del cateto: "))

if a > b:
    c:float = (a**2 - b**2  )** 0.5
    print(f"Il cateto minore misura: {c}")
else:
    print("Errore")