class Victime(object) :


    def __int__(self, id, type, position) :
        self.id = id
        self.type = type
        self.position = position
        self.disponible = True

    def isDisponible(self) :
        return self.disponible

    def getType(self) :
        return self.type

    def getPosition(self) :
        return self.position

    def setNonDisponible(self) :
        self.disponible = False