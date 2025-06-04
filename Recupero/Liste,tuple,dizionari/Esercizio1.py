from typing import Any

def converter(lista:list[tuple[Any, Any]]) -> dict:

    my_dict = {}

    for tupla in lista:

        if tupla[0] in my_dict:

            my_dict[tupla[0]] += tupla[1]
        else:
            my_dict[tupla[0]] = tupla[1]
             

    return my_dict

lista_tuple = [(0, "a"), (1, "b"), (2, "c"), (0, "g")]
print(converter(lista_tuple))