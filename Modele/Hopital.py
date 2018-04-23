class Hopital :


    def __init__(self, id) :
        self.id = id
        self.scoreTransport = (0, 0)
        self.scoreSauve = (0, 0)
        self.malus = (0, 0)

    def transporter(self, num) :
        self.scoreTransport[num] += 10

    def sauver(self, num) :
        self.scoreSauve[num] += self.scoreTransport[num]
        self.scoreTransport[num] = 0



    def transporterEnfant(self) :
        self.transport(0)

    def transporterAdulte(self) :
        self.transport(1)

    def sauverEnfant(self) :
        self.sauver(0)

    def sauverAdulte(self) :
        self.sauver(1)