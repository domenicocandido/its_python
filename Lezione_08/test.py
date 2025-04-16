from persona import Persona
from studente import Studente

# creo un oggetto p della classe Persona

p: Persona = Persona("Domenico", "Candido", 19)

# visualizzare le informazioni dell'oggetto p
print(p)

# creare un oggetto studente1 della classe studente
studente1:Studente = Studente("Mario", "Rossi", 20, "0123456")

# visualizzare le informazioni relative all'oggetto
print(studente1)


# controllare se studente1 è istanza della classe Studente
# isinstance (obj, Class) -> controlla se l'oggetto obj sia istanza della classe Class
# in caso affermativo -> True
# in caso negativo -> False

if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")

# controllo se studente1 sia anche un'istanza della classe Persona
if isinstance(studente1, Persona):
    print("\nstudente1 è un oggetto della classe Studente ma è anche un oggetto della classe Persona")

if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")

# controllare se l'oggetto p sia anche un'istanza della classe studente
if isinstance(p, Studente):
    print("\np è un oggetto della classe Persona ma è anche un oggetto della classe Studente")
else:
    print("\np è un oggetto della classe Persona ma non è un oggetto della classe Studente")

# come controllare se una classe è sottoclasse di un'altra
# controllo che la classe Studente sia sottoclasse della classe Persona
# issubClass(Class1, Class2) -> controlla se la classe Class1 è sottoclasse della classe Class2
# in caso affermartivo -> True
# in casi negativo -> False

if issubclass(Studente, Persona):
    print("\nLa classe studente è sottoclasse della classe Persona")
