'''
Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

'''

#Definisco una variabile vote richiesta all'utente.
vote:int = int(input("Inserire un voto: "))

#Imposto le condizioni che mostreranno in output un valore differente in base al voto italiano.
match vote:
    case vote if 106 <= vote <= 110:
        print("GPA: 4.0")
    case vote if 101 <= vote <= 105:
        print("GPA: 3.7")
    case vote if 96 <= vote <= 100:
        print("GPA: 3.3")
    case vote if 91 <= vote <= 95:
        print("GPA: 3.0")
    case vote if 86 <= vote <= 90:
        print("GPA: 2.7")
    case vote if 81 <= vote <= 85:
        print("GPA: 2.3")
    case vote if 76 <= vote <= 80:
        print("GPA: 2.0")
    case vote if 70 <= vote <= 75:
        print("GPA: 1.7")
    case vote if 66 <= vote <= 69:
        print("GPA: 1.0")
    case _:
        print("Voto non valido")