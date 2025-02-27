'''

Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

'''


animal:str = str(input("Inserire il nome di un animale: "))
habitat:str = str(input("Inserire l'habitat dell'animale: "))

mammiferi = ["cane", "gatto", "cavello", "elefante", "leone"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco"]
pesci = ["squalo", "trota", "salmone", "carpa"]
animal_type = []

match animal.lower():
    case animal if animal in mammiferi:
        animal_type.append("mammiferi")
        print(f"L'animale {animal} appartiene alla categoria dei Mammiferi.")
    case animal if animal in rettili:
        print(f"L'animale {animal} appartiene alla categoria dei Rettili.")
    case animal if animal in uccelli:
        print(f"L'animale {animal} appartiene alla categoria degli Uccelli.")
    case animal if animal in pesci:
        print(f"L'animale {animal} appartiene alla categoria dei Pesci.")
    case _:
        print(f"Il programma non è in grado di classificare l'animale inserito ({animal}).")
        
         