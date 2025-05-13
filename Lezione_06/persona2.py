class Persona:
    def __init__(self):
        self.name = " "
        self.lastname = " "
        self.age = 0

    # funzione della classe Persona che visualizza in outpuy i dati di una persona   
    def displayData(self) -> None:

        print(f"Nome: {self.name}\nCognome: {self.lastname}\nAge: {self.age}")


    # funzione che sonsente du umpostare il valore self.name
    def setName(self, name:str) -> None:
        self.name = name

    # funzione che consente di impostare il valore di self.lastname
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    # funzione che consente di impostare il valore di self.lastname
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.name = 0
        else:
            self.age = age
    
    # funzione che mi restituisce il valore self.name
    def getName(self) -> str:
        return self.name
    
    # funzione che mi restituisce il valore di self.lastname
    def getLastname(self) -> str:
        return self.lastname
    
    # funzione che mi restituisce il valore di self.age
    def getAge(self) -> int:
        return self.age
    
