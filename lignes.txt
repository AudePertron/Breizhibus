class Ligne:

    """Definition d'une classe pour chaque ligne"""

    def __init__(self, id, nom):
        self.id=id
        self.nom=nom

    def __repr__(self):
        return self.nom
