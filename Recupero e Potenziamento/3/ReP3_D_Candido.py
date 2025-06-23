from random import *
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

    def __init__(self, nome:str, matricola:int, munizioni:list[int]):
        super().__init__(nome)

        self.__setMatricola()
        self.setMunizioni(munizioni)
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
        return f"Alieno: {self.nome}"
    
class Mostro(Creatura):

    def __init__(self, nome, urlo_vittoria:str, gemito_sconfitta:str, assalto:list[int]):
        super().__init__(nome)

        self.urlo_vittoria = urlo_vittoria
        self.gemito_sconfitta = gemito_sconfitta
        self.assalto = assalto

    def get_urlo_vittoria(self) -> str:
        return self.urlo_vittoria
    
    def __setVittoria(self, urlo_vittoia:str) -> None:

        if not isinstance(urlo_vittoia, str):
            self.urlo_vittoria = "GRAAAHHH"
        else:
            pass
    
    def get_gemito_sconfitta(self) -> str:
        return self.gemito_sconfitta

    def setSconfitta(self, gemito_sconfitta:str) -> None:

        if not isinstance(gemito_sconfitta, str):
            self.gemito_sconfitta = gemito_sconfitta
        else:
            pass

    def getAssalto(self) -> list[int]:
        return self.assalto
    
    def setAssalto(self) -> None:

        assalto:set[int] = set(sample(range(1,101), 10 ))  # funzione sample() torna 15 numeri diversi tra loro
        self.assalto = assalto

    def __str__(self):

        nome = self.getNome()
        nome_alternato = ""

        for i, char in enumerate(nome):     # enumerate torna indice, elemento
            if i % 2 == 0:
                nome_alternato += char.upper()
            else:
                nome_alternato += char.lower()
        return f"Mostro: {nome_alternato}"


def pariUguale(a: list[int], b: list[int]) -> list[int]:

    c:list[int] = []

    for i,j in zip(a,b):

        if i % 2 == 0 and j % 2 == 0:
            c.append(1)
        else:
            c.append(0)

def combattimento(a:Alieno, m:Mostro)


        
