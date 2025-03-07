nome:str = input("Inserire il nome: ")
vendite:int = int(input("Inserire il numero vendite: "))

max_nome = nome
max_vendite = vendite
min_nome = nome
min_vendite = vendite

for cont in range(19):
    new_nome = input("Inserire il nome del venditore: ")
    new_vendite = input("Inserire il numero di vendite: ")

    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite

    if new_vendite < max_vendite:
        min_nome = new_nome
        min_vendite = new_vendite

print(f"Il venditore con più vendite è {max_nome} con {max_vendite} vendite.")
print(f"Il venditore con meno vendite è {min_nome} con {min_vendite} vendite.")