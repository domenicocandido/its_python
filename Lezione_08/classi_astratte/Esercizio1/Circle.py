from Shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        super().__init__()
        self._r: float = r

    def area(self):
        return math.pow(self._r, 2)*math.pi
    
    def perimeter(self):
        return 2 * math.pi * self._r
    
    def raggio(self) -> float:
        return self._r

if __name__ == '__main__':
    c = Circle(10.3)
    print(c.area())
    print(c.perimeter())