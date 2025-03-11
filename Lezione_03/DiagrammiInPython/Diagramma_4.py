n_tutor = 10
attesa = 0


while True:
    studente:str = input("Inserire nome studente: ")

    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con successo.")
    else:
        attesa += 1
        print("Studente in attesa.")
    
    if n_tutor == 0 and attesa > 50:
        break

        
