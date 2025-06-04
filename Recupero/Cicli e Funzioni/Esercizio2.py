def moltiplicazione(lista_numeri:list[int], threshold:int) -> int:

    prodotto = 1
    for i in lista_numeri:

        if i < threshold:

            prodotto *= i
        else:
            pass

    return prodotto

casi_di_test = [
    ([1, 2, 3, 4, 5], 4, 6),          
    ([10, 20, 30], 25, 200),          
    ([5, 3, 7, 1], 5, 3),              
    ([5, 6, 7], 5, 1),                 
    ([2, 3, 0, 4], 4, 0),             
    ([], 10, 1),                       
]

for lista, soglia, atteso in casi_di_test:
    risultato = moltiplicazione(lista, soglia)
    print(f"Lista= {lista}, Soglia= {soglia} ➜ Risultato= {risultato}, Atteso= {atteso}")