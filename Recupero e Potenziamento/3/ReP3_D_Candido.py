import random
class Creatura:

    def __init__(self, nome:str):
        self.__nome = nome

    def getNome(self) -> str:
        return self.__nome
    
    def setNome(self, nome:str) -> None:
        
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def __str__(self):
        return (f"Creatura: {self.__nome}")


c:Creatura = Creatura("Alieno")
print(c)

class Alieno(Creatura):

    def __init__(self, nome:str, matricola:int):
        super().__init__(nome)

        self.__setMatricola()
        self.setMunizioni()
        self.setNome(nome)
        

    def setNome(self, nome:str):
        nome_atteso = f"Robot-{self.matricola}"
        
        if nome == nome_atteso:
            self.nome = nome
        else:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self.nome = nome_atteso


    def getMatricola(self) -> int:
        return self.matricola
    
    def __setMatricola(self) -> None:
        self.matricola = random.randint(10000, 90000)

    def getMunizioni(self) -> list[int]:
        return self.munizioni
    
    def setMunizioni(self):
        self.munizioni = [x**2 for x in range(1, 16)]

    def __str__(self):
        return f"Alieno: {self.nome}\nMunizioni:{self.munizioni}"
    
class Mostro(Creatura):

    def __init__(self, nome, urlo_vittoria:str, gemito_sconfitta:str, assalto:list[int]):
        super().__init__(nome)

        self.urlo_vittoria = urlo_vittoria
        self.gemito_sconfitta = gemito_sconfitta
        self.assalto = assalto

    def get_urlo_vittoria(self) -> str:
        return self.urlo_vittoria
    
    def __setVittoria(self, urlo_vittoria:str) -> None:

        if  isinstance(urlo_vittoria, str):
            self.urlo_vittoria = urlo_vittoria
        else:
            self.urlo_vittoria = "GRAAAHHH"
    
    def get_gemito_sconfitta(self) -> str:
        return self.gemito_sconfitta

    def setSconfitta(self, gemito_sconfitta:str) -> None:

        if not isinstance(gemito_sconfitta, str):
            self.gemito_sconfitta = "Uuurghhh"
        else:
            pass

    def getAssalto(self) -> list[int]:
        return self.assalto
    
    def setAssalto(self) -> None:

        assalto:set[int] = random.sample(range(1,101), 15 )  # funzione sample() torna 15 numeri diversi tra loro
        self.assalto = assalto

    def __str__(self):

        nome = self.getNome()
        nome_alternato = ""

        for i, char in enumerate(nome):     # enumerate torna indice, elemento
            if i % 2 == 0:
                nome_alternato += char.upper()
            else:
                nome_alternato += char.lower()
        return f"Mostro: {nome_alternato}\nAssalto: {self.assalto}"


def pariUguale(a: list[int], b: list[int]) -> list[int]:

    c:list[int] = []

    for i,j in zip(a,b):

        if i % 2 == 0 and j % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c

def combattimento(a:Alieno, m:Mostro):

    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Mostro e/o alieni non validi, im combattimento non può avere inizio.")
        return None
  
    cont = 0
    
    for item in pariUguale(a.getMunizioni(), m.getAssalto()):
        if item == 1:
            cont += 1
        else:
            pass
    
    if cont > 4:
        print("\n".join([m.get_urlo_vittoria()] * 3))
        return m
    else:
        print(m.get_gemito_sconfitta())
        return a
            
        
def proclamaVincitore(c:Creatura):

    if isinstance(c, Mostro):
        result = "I Mostri hanno vinto"
    elif isinstance (c, Alieno):
        result = "Gli Alieni hanno vinto"


    larghezza = len(c.getNome()) + 8

    bordo = "*" * larghezza

    vuota = "*" + (" " * (larghezza - 2) ) + "*"

    centrale = "*   " + c.getNome() + "   *"

    return (f"{result}\n{"\n".join([bordo, vuota, centrale, vuota, bordo]}"