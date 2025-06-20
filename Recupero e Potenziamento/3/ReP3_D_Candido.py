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
    
    def __setMatricola(self, nuova_matricola:int) -> None:
        self.matricola = random.randint(10000, 90000)

    def getMunizioni(self) -> list[int]:
        return self.munizioni
    
    def setMunizioni(self, munizioni:list[int]):
        self.munizioni = [x**2 for x in range(1, 16)]

    def __str__(self):
        return f"Alieno: {self.nome}"
    
class Mostro(Creatura):

    def __init__(self, nome):
        super().__init__(nome)


