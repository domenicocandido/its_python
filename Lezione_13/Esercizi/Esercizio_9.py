def vowelRemover(s:str) -> str:

    vowels = ["a", "e", "i", "o", "u"]

    if not s:
        return " "
    
    if s[0].lower() in  vowels:
        return vowelRemover(s[1:])
    else:
        return s[0] + vowelRemover(s[1:])
    
print(vowelRemover("Cane"))
