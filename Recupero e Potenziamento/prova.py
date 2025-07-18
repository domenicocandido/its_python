from random import *

print("*****************")
print("*               *")
print("*    capiamo    *")
print("*               *")
print("*****************")

def output(mostro):

    larghezza = len(mostro) + 8

    bordo = "*" * larghezza

    vuota = "*" + (" " * (larghezza - 2) ) + "*"

    centrale = "*   " + mostro + "   *"

    return "\n".join([bordo, vuota, centrale, vuota, bordo])

prova = output("Alieno: Robot-25855 ")
print(prova)


setEsempio = {randint(1,100) for x in range(1,16)}
print(setEsempio)
print(len(setEsempio))


testo:str = "Ciao, viva il gatto"

def cerca_parola(parola:str, testo:str):

    return parola in testo.lower()

print(cerca_parola("ciao", testo))



testo = 'ciao'



