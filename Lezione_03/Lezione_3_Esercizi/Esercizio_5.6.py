age:int = int(input("Inserisci un età: "))

if 0 <= age < 2:
    print("La persona è un neonato.")
elif 2 <= age < 4:
    print("La persona è un bambino.")
elif 4 <= age < 13:
    print("La persona è un bambino.")
elif 13 <= age < 20:
    print("La persona è un adolescente.")
elif 20 <= age < 65:
    print("La persona è un adulto.")
elif age > 65:
    print("La persona è un anziano.")
else:
    print("Età non accettata.")

