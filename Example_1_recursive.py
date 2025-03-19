def recursiveSum (n:int) -> int:
    if n < 0:
        print("Error! Inserted negagive's number!")
        return None
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n - 1))
        
print(recursiveSum(5))