class Contatore:
    
    def __init__(self):

        self.conteggio = 0

    def get(self) -> int:
        return self.conteggio

    def setZero(self) -> None:
        self.conteggio = 0

    def add1(self) -> None:
        self.conteggio += 1

    def sub1(self) -> None:
        if self.conteggio == 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self.conteggio -= 1
    
    def mostra(self) -> None:
        print(f"Conteggio attuale: {self.conteggio}")
    
c = Contatore() 
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()  
c.add1()
c.add1()
z  = c.get()
print(z)