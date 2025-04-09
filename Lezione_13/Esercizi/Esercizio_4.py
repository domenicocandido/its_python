def recursiveDigitalCounter(n:int) -> int:

    if n < 0: 
        print("Error! Inserted number is negative!")
        return None
    
    elif n < 10:
        return 1
    else:
        return 1 + recursiveDigitalCounter(n//10)

print(recursiveDigitalCounter(229988774455))