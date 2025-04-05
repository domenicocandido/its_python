def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    lista_tot = []
    i = 0
    while i < len(x) and i < len(y):
        lista_tot.append(x[i] + y[i])
        i += 1
    return lista_tot

print(somma_elementi([1,1,1],[1,1,1]))


