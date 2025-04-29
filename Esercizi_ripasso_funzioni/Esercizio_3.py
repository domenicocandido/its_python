def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    lista_finale = lista.copy()

    for elemento, numero_di_volte in da_rimuovere.items():

        for volte in range(numero_di_volte):

            if elemento in lista_finale:
                lista_finale.remove(elemento)

    return lista_finale


print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
