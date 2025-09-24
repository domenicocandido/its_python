class Film:

    def __init__(self, id:int, title:str):
        
        self.setID(id)
        self.setTitle(title)

    def setID(self, id):
        self.__id = id
    
    def setTitle(self, title):
        self.__title = title

    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def isEqual(self, otherFilm:"Film"):
        return self.getID() == otherFilm.getID()