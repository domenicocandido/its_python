def producer(n:int) -> int:

    if n == 0:
        return (n + 2)
    else:
        return (n + 2) * producer(n - 1)
    
print((producer(7)))