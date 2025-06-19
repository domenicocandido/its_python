
# 8.A
class Frazione:

    _numeratore:int
    _denominatore:int

    def __init__(self, numeratore:float, denominatore:float):

        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def numeratore(self) -> int:
        return self._numeratore
    
    def set_numeratore(self, numeratore:float) -> None:
        numeratore = float(numeratore)
        if numeratore.is_integer():
            self._numeratore = int(numeratore)
        else:
            self._numeratore = 13

    def denominatore(self) -> int:
        return self._denominatore
    
    def set_denominatore(self, denomoinatore:float) -> None:
        denomoinatore = float(denomoinatore)
        if denomoinatore.is_integer() and denomoinatore != 0:
            self._denominatore = int(denomoinatore)
        else:
            self._denominatore = 5

    def value(self) -> float:

        result= self._numeratore/self._denominatore
        return round(result, 3)

    def __str__(self):
        return(f"{self.numeratore()}/{self.denominatore()}")

f: Frazione = Frazione(15.1, 4)

print(f)
print(f.numeratore())
print(f.denominatore())
f.set_numeratore(8)
f.set_denominatore(9)
print(f.numeratore())
print(f.denominatore())
print(f.value())


# 8.B

def mcd(x:int, y:int) -> int:

    divisoriX = []
    divisoriY = []

    for n in range(1,x + 1):
        if x % n == 0:
            divisoriX.append(n)
    for n in range(1, y + 1):
        if y % n == 0:
            divisoriY.append(n)
    
    comuni = set(divisoriX).intersection(divisoriY)
    if comuni:
        return max(comuni)
    else:
        return 1
        
print(mcd(45,30))

# 8.C

i:list[Frazione] = [Frazione(15,3), Frazione(45,9)]

def semplifica(frazioni:list[Frazione]) -> list[Frazione]:
        
        frazioni_semplificate = []

        for frazione in frazioni:
            
            divisore = mcd(frazione.numeratore(), frazione.denominatore())
            if divisore == 1:
                frazioni_semplificate.append(frazione)
            else:
                num_sempl = int(frazione.numeratore()/divisore)
                den_sempl = int(frazione.denominatore()/divisore)

                frazioni_semplificate.append(str(Frazione(num_sempl, den_sempl)))

        return frazioni_semplificate

print(semplifica(i))

# 8.D

def fractionCompare(frazioni:list[Frazione], frazioni_semplificate:list[Frazione] ):
    
    for fra1, fra2 in frazioni, frazioni_semplificate:
        return f"Valore frazione originale: {fra1.value()} --- Valore farzione ridotta {fra2.value()} "
    

print(fractionCompare(i,(semplifica(i))))
    