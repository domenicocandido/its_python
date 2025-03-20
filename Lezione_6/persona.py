class Persona:

    #costruttore
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age

    # funzione della classe Persona che visualizza in oltput i dati di una persona

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nAge: {self.age}")
