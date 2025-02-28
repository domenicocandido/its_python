'''

Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

'''

i = 0
counter_testa = 0
counter_croce = 0

while i < 8:
    
    lancio:str = str(input("Inserire se è uscito testa (\" t \" o \" T \") o croce (\" c \" o \" C \"): " ))
    i += 1
    
    match lancio:

        case "T"| "t":
            counter_testa += 1
        
        case "C"| "c":
            counter_croce += 1
        
        case _:
            print("Il valore inserito non è valido.")


percentuale_testa = (counter_testa * 100) / i
print(f"\"Testa\" è uscito: {counter_testa} volte.")
print(f"La percentuale di \"Testa\" è: {percentuale_testa:.2f}")

percentuale_croce = (counter_croce * 100) / i
print(f"\"Croce\" è uscito: {counter_croce} volte.")
print(f"La percentuale di \"Croce\" è: {percentuale_croce:.2f}")