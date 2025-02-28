'''
 Scrivere un programma in Python che utilizzi un match statement per classificare un voto scolastico in base alla scala italiana.
Il programma deve accettare in input un voto numerico intero da 1 a 10 e stampare la valutazione corrispondente:

'''

#Definisco la varibile voto richiesta all'utente.
vote:int = int(input("Inserire un voto: "))

#Imposto le condizioni che mostreranno in output una frase differente in base al voto.
match vote:
    case vote if 1 <= vote <= 3:
        print("Gravemente insufficiente")
    case 4|5:
        print("Insufficiente")
    case 6|7:
        print("Sufficiente")
    case 8|9:
        print("Molto Buono")
    case 10:
        print("Eccellente")
    case _:
        print("Voto non valido.")