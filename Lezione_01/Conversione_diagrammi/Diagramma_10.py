r:float  = float(input("Inserire valore reddito familiare: "))
m:float = float(input("Inserire il valore della media dei voti: "))

if r < 20000 and m > 27:
    print("Borsa di studio approvata.")
else:
    print("Borsa di studiop rifiutata. (Motivo: media o reddito insufficiente)")