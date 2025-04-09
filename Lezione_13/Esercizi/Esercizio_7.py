def producer(n:int) -> int:

    if n == 1:
        return (n ** 3)
    else:
        return (n ** 3) * producer(n - 1)


print((producer(5)))