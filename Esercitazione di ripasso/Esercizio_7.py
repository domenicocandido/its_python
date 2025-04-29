def remove_duplicates(list1: list[int,str]) -> list:
    
    list2:list[int, str] = []

    if not list1:
        return list1
    else:
        list2.append(list1[0])

    for element in list1:
        if element not in list2:
            list2.append(element)
    return list2


print(remove_duplicates([1, 2, 3, 1, 2, 4]))
print(remove_duplicates([4, 5, 'a', 4, 6]))

