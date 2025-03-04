sum = 0
for i in range (1,11):
    sum += i
print(f"Sum of integers from 1 to 10 is {sum}")

sum= 0
for i in range (20,38):
    sum += i
print(f"Sum of integers from 1 to 10 is {sum}")

sum = 0
for i in range(35,50):
    sum += i
print(f"Sum of integers from 1 to 10 is {sum}")

#Come si definisce una funzione

def sum_range(a:int, b:int):  #Nelle parentesi sono presenti i due parametri della funzione.
    
    result:int = 0              #Variabile inizializzata a 0
    for i in range (a, b + 1):
        result += i

    return result

sum_range(1,10)

'''

def nome_funzione (parametro1, parametro2)
varibaile_inizializzata_a_zero = 0

scrivo il codice da eseguire


'''