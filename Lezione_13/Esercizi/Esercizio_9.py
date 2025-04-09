def vowelRemover(s:str) -> str:

    vocals = ["a", "e", "i", "o", "u"]

    if vocals not in s:
        return s
    
    if s[0].lower() in  vocals:
        return 0 + vowelRemower(s[1:])
    else:
        return s[0] + vowelRemover(s[1:])
    
print(vowelRemover("Cane"))
