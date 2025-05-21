from Lezione_08.classi_astratte.Esercizio1.Circle import Circle
from Rectangle import rectangle

if __name__ == '__main__':
    c = Circle(20)
    print(f"Area e perimetro del cerchio con raggio = {c.raggio()}: (area = {c.area()},perimetro = {c.perimeter()}) ")

    r = rectangle(10,30)
    print(f"Area e perimetro del rettangolo con base = {r.base()} e altezza = {r.altezza()}: (area = {r.area()}, perimetro = {r.perimeter()})")