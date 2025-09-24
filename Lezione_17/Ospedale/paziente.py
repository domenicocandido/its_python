from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name, last_name, idCode:str):
        super().__init__(first_name, last_name)

        self.__idCode = idCode

    def setIdCode