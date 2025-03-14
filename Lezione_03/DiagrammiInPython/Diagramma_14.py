punteggio = 0

while punteggio < 100:

    D1:int = int(input("Numero del primo dado: "))
    D2:int = int(input("Numero del secondo dado: "))

    if 0 < D1 <= 6 and 0 < D2 <= 6:

        sum = D1 + D2

        if D1 % 2 == 0 and D2 % 2 == 0 and sum > 8:

            punteggio = 100

        else:
            if D1 == 6 or D2 == 6 or sum == 7:

                punteggio += 10
            
            else:
                punteggio = 0
                print("Sconfitta.")
                break

if punteggio == 100:    
    print("Vittoria.")