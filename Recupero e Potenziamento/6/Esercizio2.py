nomi:list[str] = []
nome_max = " "
while True:

    nome:str = input("Inserire un nome: ")
    if len(nome) > 20 and nome:
        print("ATTENZIONE! Nome non valido.")

    elif nome in nomi or len(nomi) == 30:
        print(f"Sono stati inseriti {len(nomi)} nomi.")
        for nome in nomi:
            if len(nome) > len(nome_max):
                nome_max = nome
            else:
                pass
        print(f"Il nome più lungo è: {nome_max}.")
        print(f"Il nome più lungo ha {len(nome_max)} caratteri.")
        break
    else:
        nomi.append(nome)

