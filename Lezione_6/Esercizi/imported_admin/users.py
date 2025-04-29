class User:

    def __init__(self, name:str, lastname:str, age:int, nickname:str, email:str ):
        
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.email = email
        self.age = age
    
    def describe_user(self) -> None:

        print(f"\nName: {self.name}")
        print(f"Lastname: {self.lastname}")
        print(f"Location: {self.age}")
        print(f"Nickname: {self.nickname}")
        print(f"Email: {self.email}")
    
    def greet_user(self) -> None:

        print(f"Benvenuto {self.nickname}")

class Privileges:

    def __init__(self, privileges:list[str]) -> None:

        self.privileges = privileges
    
    def show_privileges(self) -> None:

        print("\nI privilegi sono:")
        for privilege in self.privileges:
            print(f"|{privilege}|")

class Admin:

    def __init__(self, user:User, privileges:Privileges):

        self.user = user
        self.privileges = privileges
    
    def describe_user(self) -> None:

        self.user.describe_user()
    
    def show_privileges(self) -> None:

        self.privileges.show_privileges()

        




        

