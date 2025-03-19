def countdown(n:int) -> None:

    if n >= 0:
        while n:
            print(n)
            n -= 1

    else:
        print("Errore! Inserire un numero positivo")

countdown(-9)
countdown(9)



