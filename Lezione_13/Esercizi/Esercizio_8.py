def vowelsCounter (s:str) -> int:

    vocals = ["a", "e", "i", "o", "u"]
    if not s:
        return 0
    if s[0].lower() in  vocals:
        return 1 + vowelsCounter(s[1:])
    else:
        return 0 + vowelsCounter(s[1:])
    
test = vowelsCounter("Ciao")
print(test)