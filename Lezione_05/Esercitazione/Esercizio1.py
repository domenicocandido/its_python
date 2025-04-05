def even_odd_pattern(numbers:list[int]) -> list[int]:
    list_odd = []
    list_even = []
    for i in numbers:
        if i % 2 == 0:
            list_even.append(i)
        elif i % 2 != 0:
                list_odd.append(i)
    numbers = list_even + list_odd
    return numbers

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
