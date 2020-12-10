from connexion import Connexion
class Bus:
    def __init__(self, *infos):
        self.id = infos[0]
        self.ligne = infos[1]
        self.immat = infos[2]
        self.nb_places = infos[3]
        self.numero = infos[4]

    def __str__(self):
        return self.numero