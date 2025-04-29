def transform(x: int) -> int:
    
    if x % 2 == 0:
        
        return x/2
    
    elif x % 2 != 0:
        
        return (x*3)-1
    
print(transform(9))
print(transform(-10))