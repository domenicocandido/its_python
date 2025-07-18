from abc import ABC,abstractmethod
import string

class CodificatoreMessaggio(ABC):
    
    @abstractmethod
    def codifica(testoInChiaro):
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato):
        pass
    

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):


    pool = string.ascii_letters + string.punctuation

    def __init__(self, chiave:int):

        self.setChiave(chiave)

    def getChiave(self) -> int:
        return self.chiave
    
    def setChiave(self,chiave) -> None:
        self.chiave = chiave

    def codifica(self, testoInChiaro):

        testoCriptato = ''

        for c in testoInChiaro:
            for l in __class__.pool:
                if c == l:
                    c = l + self.getChiave()
                    testoCriptato += c

        return testoCriptato
    
    def decodifica(self, testoCodificato:str):

        testoDecriptato = ''

        for c in testoCodificato:
            testoDecriptato -= 
        
        return testoDecriptato

    def __sposta_carattere(self, c):
        index = __class__.pool.index(c)
        




class CifratoteACombinazione(CodificatoreMessaggio,DecodificatoreMessaggio):

    def __init__(self, n:int):
        self.n = n

    def combinazione(testo):

        testoCombinato = ''

        mid:int = len(testo) // 2
        part1:list[int] = list(testo[:mid])
        part2:list[int] = list(testo[-mid:])

        for x,y in enumerate(part1,part2):
            testoCombinato += x,y

    def codifica(self, testoInChiaro):
