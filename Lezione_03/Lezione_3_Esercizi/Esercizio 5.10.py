current_users = ["Domenico05", "Luca00", "Matteo01", "Giuseppe99", "Giovanni87"]
new_users = ["Luigoi67", "Marco91", "Francesco65", "Valerio06", "Giuseppe99"]

for user in new_users:
    if user in current_users:
        print("Nome utente già in uso, scegline uno diverso.")
    else:
        print("Il nome utente è disponibile.")


