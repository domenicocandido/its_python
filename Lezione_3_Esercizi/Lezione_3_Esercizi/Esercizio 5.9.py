users = ["admin", "mario", "luigi", "peach", "yoshi"]
users.clear()

if not users:
    print("Dobbiamo trovare alcuni utenti!")
else:
    for user in users:
        if user == "admin":
            print("Ciao Admin, vuoi vedere un report dello stato del sistema?")
        else:
            print(f"Ciao {user}, grazie per aver effettuato l'accesso!")
