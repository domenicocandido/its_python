from Shape import Shape

class rectangle(Shape):
    def __init__(self, base:float, altezza:float):
        self._base = base
        self._altezza = altezza

    def area(self) -> float:
        return self._base * self._altezza
    
    def perimeter(self):
        return (self._base + self._altezza) * 2
    
    def base(self) -> float:
        return self._base
    
    def altezza (self) -> float:
        return self._altezza 
