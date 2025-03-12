cont = 0
somma = 0

while True:
    
     scelta:str = input("Inserire scelta SI/NO: ")

     match scelta.lower():
          
          case "si":
               voto:float =  float(input("Inserire voto: "))

               if voto > 0:
                    cont += 1
                    somma += voto
                    
               else:
                    print("Errore")
          
          case "no":
               
               if cont > 0:
                    media = somma/cont
                    print(f"La media misura {media:.1f}:")
                    break
               else:
                    print("Nessuo voto inserito")
          
          case _:
               print("Inserire una scelta valida.")