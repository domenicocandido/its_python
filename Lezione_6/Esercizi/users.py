class User:

    def __init__(self, name:str, lastname:str, age:int, nickname:str, email:str ):
        
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.email = email
        self.age = age
    
    def describe_user(self) -> str:

        print(f"\nName: {self.name}")
        print(f"Lastname: {self.lastname}")
        print(f"Location: {self.age}")
        print(f"Nickname: {self.nickname}")
        print(f"Email: {self.email}")
    
    def greet_user(self) -> str:

        print(f"Benvenuto {self.nickname}")

user1:User = User("Domenico","Candido", 19,"dome05","candidodomenico87@gmail.com")
user1.describe_user()
user1.greet_user()

user2:User = User("Mario", "Rossi", 28, "mario_rossi", "mariorossi97@gmail.com")
user2.describe_user()
user2.greet_user()

user3:User = User("Kenan", "Yildiz", 19, "yildiz10", "kenanayildiz05@gmail.com")
user3.describe_user()
user3.greet_user()


