from abc import ABC,abstractmethod

class CodificatoreMEssaggio(ABC):
    
    @abstractmethod
    def codifica(self):
        pass

    
