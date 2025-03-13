x:int = int(input("Inserire un numero intero positivo X: "))
y:int = int(input("Inserire un numero intero positivo Y: "))
z:int = int(input("Inserire un numero intero positivo Z: "))

if x % 1 == 0 and x > 0:
    
    if y % 1 == 0 and y > 0:

        if z % 1 == 0 and z > 0:

            if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0:

                print("Regole rispettate.")

            else:
                print("Regole non rispettate.")

        else:
            print("Z deve dessere intero o positivo.")
    
    else:
        print("Y deve essere intero o positivo")

else:
    print("X deve essere intero o positivo.")

