class Persona:

    def __init__(self, first_name:str, last_name:str):
    
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa")
            self.__first_name = None

        if not isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa")
            self.__last_name = last_name
        
        if isinstance(first_name, str) and isinstance(last_name, str):
            self.__age = 0
        elif not isinstance(first_name, str) and not isinstance(first_name, str):
            self.__age = None


    def setName(self, first_name:str):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa")
            self.__last_name = None

    def getName(self):
        return self.__first_name
    
    def setName(self, last_name:str):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            print("Il cognome inserito non è una stringa")
    
    def getLastName(self):
        return self.__last_name
    
    def setAge(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("L'età inserita non è un intero")

    def getAge(self):
        return self.__age
    
    def greet(self):
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")






    

        



    








