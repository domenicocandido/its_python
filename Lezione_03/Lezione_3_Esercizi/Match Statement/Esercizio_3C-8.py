'''

Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

'''

sentence:str = str(input("Inserire una frase: "))
last_character = sentence
match sentence:

    case sentence if len(sentence) % 2 == 0 and sentence[-1] == "?":
        print("Si")
    
    case sentnece if len(sentence) % 2 != 0 and sentence[-1] == "?":
        print("No")

    case sentence if sentence[-1] == "!":
        print("Wow")
    
    case _:
        print(f"Tu dici: \"{sentence}\".")
