users = ["Admin", "Jack", "Paul", "Michael", "Rich"]

for name in users:
    if name == "Admin":
        print("Ciao Admin, vuoi vedere un rapporto sul tuo stato?")
    else:
        print(f"Ciao {name}, grazie per aver effettuato di nuovo l'accesso.")
