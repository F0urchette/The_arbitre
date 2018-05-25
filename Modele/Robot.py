class Robot(object) :

    def __init__(self, id, position) :
        self.id = id
        self.scoreTransport = (0, 0)
        self.scoreSauve = (0, 0)
        self.malus = (0, 0)
        self.position = position

    def isPlaceDisponible(self) :
        return ((2 - self.nbTransporte()) == 0)

    def nbTransporte(self):
        return ((self.scoreTransport[0] + self.scoreTransport[1]) / 10)

    def transporter(self, num) :
        self.scoreTransport[num] += 10

    def sauver(self, num) :
        self.scoreSauve[num] += self.scoreTransport[num]
        self.scoreTransport[num] = 0

    def transporterEnfant(self) :
        self.transporter(0)

    def transporterAdulte(self) :
        self.transporter(1)

    def sauverEnfant(self) :
        self.sauver(0)

    def sauverAdulte(self) :
        self.sauver(1)

    def majPosition(self, position) :
        self.position = position

    def ajouterMalusLigne(self) :
        self.malus[0] += 2

    def getPosition(self) :
        self.position