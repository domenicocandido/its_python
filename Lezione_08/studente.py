# dal modulo persona.py importo la classe persona
from persona import Persona

# la classe studente eredita dalla classe persona
class Studente(Persona):

    '''
    Attributi della classe Persona in quanto Studente eredita da Persona:
    self.name: str
    self.lastname: str
    self.age: str

    Attributi dello studente
    self.matricola: str

    '''

    # inizializzare un oggetto della classe Studente
    def __init__(self, name: str, lastname:str, age: int, matricola:str) :
        # inizializzo la classe Persona richiamando il metodo __init__ della superclasse
        super().__init__(name, lastname, age)  

        # istruzioni che inizializzano un oggetto della classe studente

        self.setMatricola(matricola)
    
    # metodo setter
    # metodo che imposta il valore dell'attributo self.matricola
    def setMatrciola(self, matricola:str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("\nErrore! La matricola non può essere rappresentata da una stringa")
        
    def getMatricola(self) -> int:
        return self.matricola

    # ridefinire il metodo __str__ (overiding)
    def __str__ (self) -> str:
        return f"\nNome: {self.name}\nCognome: {self.getLastname()}\nMatricola: {self.getMatricola()}"

