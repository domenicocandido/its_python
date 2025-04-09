def recursiveFactorial(n:int) -> int:
    
    if n == 0:
        return 1
    else:
        return (n * recursiveFactorial(n - 1))

print(recursiveFactorial(3))