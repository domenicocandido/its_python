s1= "CAGCTGATCGATGCTAGCCTG"
s2= "AGCCTGTTGCACCTAGA"

sovrapposte:str = ""
sovrapposizione:int = 6
s1_ultime:str = s1[-sovrapposizione:]
s2_priime:str = s2[:sovrapposizione]
print(s1[-6:])
print(s2[:6])

for i, j in zip(s1_ultime, s2_priime):
    if i==j:
        sovrapposte += i
        

print(sovrapposte)