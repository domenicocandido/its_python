class Veicolo:

    def __init__(self, marca:str, modello:str, anno:int):

        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")


class Auto(Veicolo):

    def __init__(self, marca:str, modello:str, anno:int, numero_porte:int):
        super().__init__(marca, modello, anno)

        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")

class Moto(Veicolo):

    def __init__(self, marca:str, modello:str, anno:int):
        super().__init__(marca, modello, anno)
 