class Documento:

    def __init__(self, testo:str):
        self.setText(testo)

    def getText(self) -> str:
        return self.testo
    
    def setText(self, testo:str) -> None:
        self.testo = testo

    def isInText(self, parola:str) -> bool:
        return parola in self.testo.lower()
    

documento = Documento("Ciao, viva i cani")
print(documento.isInText("ciao"))
    
class Email(Documento):

    def __init__(self, testo:str, mittente:str, destinatario:str, titoloMessaggio:str ):
        super().__init__(testo)

        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitoloMessaggio(titoloMessaggio)

    def getMittente(self) -> str:
        return self.mittente 
    
    def setMittente(self, mittente:str):
        self.mittente = mittente
    
    def getDestinatario(self) -> str:
        return self.destinatario 
    
    def setDestinatario(self, destinatario:str):
        self.destinatario = destinatario

    def getTitoloMessaggio(self) -> str:
        return self.titoloMessaggio
    
    def setTitoloMessaggio(self, titoloMessaggio:str) -> None:
        self.titoloMessaggio = titoloMessaggio
    
    def getText(self) -> str:
        return f"Da: {self.mittente}, A:{self.destinatario}\nTitolo: {self.titoloMessaggio}\nMessaggio: {self.testo}"
    
    def writeToFile(self):
        pass

class File(Documento):

    def __init__(self, testo:str, nomePercorso:str):
        super().__init__(testo)

        self.nomePercorso = nomePercorso

    