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


c:Creatura = Creatura("Batman")
print(c)