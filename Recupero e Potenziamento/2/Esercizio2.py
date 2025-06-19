def proDict() -> dict[tuple[int], int ]:

    myDict:dict[tuple[int], int ] = {}

    for x in range (101):

        for y in range(2, 89, 2):

            prodotto = x * y

            myDict[x,y] = prodotto
    return myDict

print(proDict())


            