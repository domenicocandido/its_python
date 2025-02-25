'''

Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

'''
#Definisco la lista vuota objects.
objects =[]

#Avvio il ciclo finchè non avrò ricevuito dall'uitente 3 elementi.
while len(objects) < 3:
    element:str = str(input("Inserire un oggetto: "))

    #Aggiungo ogni elemento alla lista objects.
    objects.append(element)

#Creo le condizioni che in base agli elementi inseriti segnala la categoria corrispondente.
match objects:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("dispositivi elletronici")
    case _:
        print("Categoria sconosciuta")