def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    
    contact = {
        
        "profile" : name,
        "email" : email,
        "telefono" : telefono
    }
    
    return contact
    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    
    if dictionary["profile"] == name:
        
        if email is not None:
            dictionary["email"] = email
            
            if telefono is not None:
                dictionary["telefono"] = telefono
    
    return dictionary

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))