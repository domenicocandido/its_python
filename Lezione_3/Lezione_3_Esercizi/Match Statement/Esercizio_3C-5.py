'''
Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

'''

name:str = str(input("Digitare il nome dell'utente: "))
rules:str = str(input("IDigitare il ruolo dell'utente: "))
age:int = int(input("Digitare l'età dell'utente: "))

user = {
    "Nome": name,
    "Ruolo": rules,
    "Età": age
}

# Determinazione del livello di accesso con match-case
match rules:
    
    case "Admin":
        print("Accesso completo a tutte le funzionalità.")
    case "Moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case "Utente":
        if age >= 18:
            print("Accesso standard a tutti i servizi.")
        else:
            print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case "Opsite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

print(user)

