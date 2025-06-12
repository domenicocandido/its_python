import string

def count_unique_words(text:str) -> dict:

    risultato = {}

    tokens = text.split()

    for token in tokens:

        token = token.lower()
        token = token.strip(string.punctuation)
        print(token)

        if token == "":
            print("La stringa è vuota")
        else:
            if token not in risultato:
                risultato[token] = 0
            risultato[token] += 1
        
    return risultato

print(count_unique_words(" Gli animali: cane, gatto, volpe, cane, gatto, canarino."))

