def converter(lista:list[float]) -> dict[str, list[int|float]]:

    my_dict = {}
    my_dict["Positivi"] = []
    my_dict["Negativi"] = []


    for number in lista:

        if number >= 0:
            my_dict["Positivi"].append(number)
        else:
            my_dict["Negativi"].append(number)


    return my_dict

lista_numeri:list[int|float] = [1,2,3,4,5,-6,-7,-8,-9]
print(converter(lista_numeri))