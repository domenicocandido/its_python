def sum(n:int) -> int:
    if n < 0:
        print("Error! Inserted negagive's number!")
        return None
    
    else:
        sum:int = 0

        while n:
            
            sum += n
            n -= 1
        return int(sum)


somma = sum(5)
print(somma)