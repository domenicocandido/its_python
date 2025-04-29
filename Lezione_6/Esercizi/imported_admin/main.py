from users import User, Privileges, Admin

user1:User = User("Domenico","Candido", 19,"dome05","candidodomenico87@gmail.com")
privileges1:Privileges = Privileges(["Gestione accessi", "Blocco utenti"])

admin1:Admin = Admin(user1, privileges1)

admin1.describe_user()
admin1.show_privileges()
