'''

Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, utilizzando un match statement, identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio indicante che il programma non è in grado di classificare l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

'''

animal:str = str(input("Inserire il nome di un animale: "))

mammiferi = ["cane", "gatto", "cavello", "elefante", "leone"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco"]
pesci = ["squalo", "trota", "salmone", "carpa"]

match animal.lower():
    case animal if animal in mammiferi:
        print(f"L'animale {animal} appartiene alla categoria dei Mammiferi.")
    case animal if animal in rettili:
        print(f"L'animale {animal} appartiene alla categoria dei Rettili.")
    case animal if animal in uccelli:
        print(f"L'animale {animal} appartiene alla categoria degli Uccelli.")
    case animal if animal in pesci:
        print(f"L'animale {animal} appartiene alla categoria dei Pesci.")
    case _:
        print(f"Il programma non è in grado di classificare l'animale inserito ({animal}).")