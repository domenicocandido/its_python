'''

Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla. Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."

'''

x:int =  int(input("Inserire valore coordinata X: "))
y:int = int(input("Inserire valore coordinata Y: "))

coordinate:tuple = (x,y)

match coordinate:
    
    case (0,0):
        print("Il punto si trova nell'origine.")
    
    case (x,0):
        print("Il punto si trova sull'asse X.")

    case (0,y):
        print("Il punto si trova sull'asse X.")
    
    case (x,y):
        if x > 0 and y > 0:
            print("Il punto si trova nel primo quadrante.")
    
    case (x,y):
        if x < 0 and y > 0:
            print("Il punto si trova nel secondo quadrante.")

    case (x,y):
        if x < 0 and y < 0:
            print("Il punto si trova nel primo quadrante.")

    case (x,y):
        if x > 0 and y < 0:
            print("Il punto si trova nel primo quadrante.")
    
    case _:
        print("Coordinate non valide.")

