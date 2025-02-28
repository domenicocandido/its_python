alien_color = "Verde"

if alien_color == "Verde":
    print("Complimenti!!! Hai guadagnato 5 punti.")
elif alien_color == "Giallo":
    print("Complimenti!!!Hai guadagnato 10 punti.")
elif alien_color == "Rosso":
    print("Complimenti!!!Hai guadagnato 15 punti.")

alien_color = "Giallo"

if alien_color == "Verde":
    print("Complimenti!!! Hai guadagnato 5 punti.")
elif alien_color == "Giallo":
    print("Complimenti!!!Hai guadagnato 10 punti.")
elif alien_color == "Rosso":
    print("Complimenti!!!Hai guadagnato 15 punti.")

alien_color = "Rosso"

if alien_color == "Verde":
    print("Complimenti!!! Hai guadagnato 5 punti.")
elif alien_color == "Giallo":
    print("Complimenti!!!Hai guadagnato 10 punti.")
elif alien_color == "Rosso":
    print("Complimenti!!!Hai guadagnato 15 punti.")

#Versione con input
alien_color:str = str(input("Scrivi il colore"))

if alien_color == "Verde":
    print("Complimenti!!! Hai guadagnato 5 punti.")
elif alien_color == "Giallo":
    print("Complimenti!!!Hai guadagnato 10 punti.")
elif alien_color == "Rosso":
    print("Complimenti!!!Hai guadagnato 15 punti.")
else:
    print("Colore non valido.")