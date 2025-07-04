def recursivePalindrome(testo:str) -> bool:

    testo = testo.replace(" ", "")
    testo = testo.lower()
    if not testo:
        return True
    elif testo[0] != testo[-1]:
        return False
    else:
        return recursivePalindrome(testo[1:-1])
    
print(recursivePalindrome("Anna"))
