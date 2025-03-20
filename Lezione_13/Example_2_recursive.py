def recursivesumInrange (a:int, b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp

    if b == a:
        return int(a)
    else:
        return int(b + recursivesumInrange(a, b - 1))
    
print(recursivesumInrange(10,5))