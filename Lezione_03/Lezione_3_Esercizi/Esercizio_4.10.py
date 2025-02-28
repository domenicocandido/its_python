numeri = [numero for numero in range(1,1000001)]

print("I primi tre elementi nell'elenco sono:", numeri[:3])

metà = len(numeri) // 2
print("Tre elementi dal centro dell'elenco sono:", numeri[metà-1:metà+2])