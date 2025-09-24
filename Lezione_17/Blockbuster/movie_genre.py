from film import Film

class Azione(Film):

    def __init__(self, id, title, genere:str, penale:float):
        super().__init__(id, title)

        self.__genere = Azione
        self.__penale = 3.0

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni:int):
        return self.__penale * giorni
    
class Commedia(Film):

    def __init__(self, id, title, genere:str, penale:float):
        super().__init__(id, title)

        self.__genere = Azione
        self.__penale = 2.50

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni:int):
        return self.__penale * giorni
    
class Drama(Film):

    def __init__(self, id, title, genere:str, penale:float):
        super().__init__(id, title)

        self.__genere = Azione
        self.__penale = 2

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorni:int):
        return self.__penale * giorni