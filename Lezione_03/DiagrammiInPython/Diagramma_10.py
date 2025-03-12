eta:int = int(input("Inserire l'età: "))

if eta >= 18 and eta <= 65:
    print("Puoi partecipare all'attività.")
    
else:
   
    if eta < 18:
        print("Non puoi partecipare all'attività perchè non hai raggiunto l'età minima richiesta.")
   
    else:
        print("Non puoi partceipare all'attività perchè hai superato l'età massima consentita.")
