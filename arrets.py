class Arret:

    """Definition d'une classe pour chaque arret"""

    def __init__(self, id, nom, adresse):
        self.id=id
        self.nom=nom
        self.adresse=adresse

    def __repr__(self):
        return self.nom
