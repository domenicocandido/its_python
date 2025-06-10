from string import ascii_lowercase

def cifrarioCesare(s:str, key: int ) -> str:

    alfabeto = ascii_lowercase
    new_s:str = " "

    if key < 0:
        print("Il numero non può essere negativo")
    else:

        for char in s:

            c = char.lower()
             
            if c in alfabeto:
                
                pos = alfabeto.index(char)
                new_pos = (pos + key) % 26
                new_s += alfabeto[new_pos]
            else:
                new_s += char
    
        return new_s
            
print(cifrarioCesare("gazebo", 2))





