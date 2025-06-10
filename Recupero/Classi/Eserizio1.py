class ContactManager:

    def __init__(self, contacts: dict[str, list[str]] ):
        self.contacts = contacts

    def create_contact(self, name:str, phone_numbers:list[str]):
            
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
        else:
            print("Il nome esiste già")

    def add_phone_number(self, contact_name:str, phone_number:str) -> None:

        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                print("Errore! Il numero di telefono esiste già.")
            else:
                self.contacts[contact_name].append(phone_number)
        else:
            print("Errore! Il contatto non esiste")

    def remove_phone_number(self, contact_name:str, phone_number:str )-> None:

        if contact_name in self.contacts:

            if phone_number in self.contacts[contact_name]:

                self.contacts[contact_name].remove(phone_number)
            else:
                print("Il numero non è presente.")
        else:
            print("Il contatto non esiste.")

    def update_phone_number(self,contact_name:str, old_phone_number:str, new_number:str) -> None:

        if contact_name in self.contacts:

            if old_phone_number in self.contacts[contact_name]:

                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_number)
            else:
                print("Il numero non è presente")
        else:
            print("Il contatto non esiste")

    def list_contacts(self) -> list[str]:

        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name:str) -> list[str]:

        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            print("Errore il contatto non esiste")
            return []
            
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        result = []
        for name,numbers in self.contacts.items():
            
            if phone_number in numbers:
                result.append(name)
            if result:
                return result
            else:
                print( "Il numero non esiste.")
                return []

11111
#Test
rubrica = ContactManager({})

rubrica.create_contact("Mario", ["11111"])
rubrica.create_contact("Luca", ["22222"])
rubrica.create_contact("Anna", ["33333"])

rubrica.add_phone_number("Mario", "44444")
rubrica.add_phone_number("Luca", "44444")  
rubrica.add_phone_number("Anna", "55555")

rubrica.remove_phone_number("Anna", "33333")

print("Contatti:", rubrica.list_contacts())
print("Numeri di Mario:", rubrica.list_phone_numbers("Mario"))
print("Numeri di Luca:", rubrica.list_phone_numbers("Luca"))
print("Numeri di Anna:", rubrica.list_phone_numbers("Anna"))

print("Contatti con il numero 44444:", rubrica.search_contact_by_phone_number("44444"))

            




        
