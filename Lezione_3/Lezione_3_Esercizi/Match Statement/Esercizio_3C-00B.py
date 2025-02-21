'''

Scrivere un programma in Python che chieda all'utente di inserire il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi lo statement match per fornire una risposta adeguata da inserire in un documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.

'''
#Definisco le due variabili, name che richiede il nome all'utente e gen che richiede il genere.
name:str = str(input("Inserisci il tuo nome: "))  
gen:str = str(input("Inserisci il  tuo genere (m se sei maschio o f se sei femmina): "))

#Definisco le condizonioni che in base al genere definiscono il nome dell'utente come Maschio o Femmina.
match gen:
    case "m":
        print(f"{name} è un Maschio.")
    case "f":
        print(f"{name} è una Femmina.")
    case _:
        print("ERRORE!!! Impossibile generare un documento d'identità.")