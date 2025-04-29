def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
    list_even = []
    list_odd = []
    dict1= {"pari": list_even, "dispari": list_odd}
    
    for  number in lista:
        if number % 2 == 0:
            list_even.append(number)
        elif number % 2 != 0:
            list_odd.append(number)
    
    return dict1

print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
print(classifica_numeri([]))

