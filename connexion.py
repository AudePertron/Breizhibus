#gestion et connexion à la bdd
import mysql.connector as mysql
from lignes import Ligne
from arrets import Arret


class Connexion :
    @classmethod
    def ouvrir_connexion(cls):
        cls.bdd = mysql.connect(user='root', password='root', host='localhost', port="8081", database='breizhibus')
        cls.cursor = cls.bdd.cursor()


    @classmethod
    def fermer_connexion(cls):
        cls.cursor.close()
        cls.bdd.close()


    @classmethod
    def lister_lignes(cls):
        cls.ouvrir_connexion()
        ligne_liste=[]
        get_query="Select * from ligne"
        cls.cursor.execute(get_query)

        for row in cls.cursor:
            ligne = Ligne(row[0], row[1])
            ligne_liste.append(ligne)
        cls.fermer_connexion()
        return ligne_liste


    @classmethod
    def lister_arrets(cls, ligne):
        cls.ouvrir_connexion()
        arret_liste=[]
        get_query=f"SELECT * FROM arrets JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret JOIN ligne ON arrets_lignes.id_ligne = ligne.id_ligne WHERE ligne.nom = '{ligne}';"

        cls.cursor.execute(get_query)

        for row in cls.cursor:
            arret = Arret(row[0], row[1], row[2])
            arret_liste.append(arret)
        cls.fermer_connexion()
        return arret_liste

    @classmethod
    def lister_bus(cls, ligne):
        cls.ouvrir_connexion()
        bus_liste=[]
        get_query=f"SELECT numero FROM bus JOIN ligne ON bus.id_ligne = ligne.id_ligne WHERE ligne.nom = '{ligne}';"
        cls.cursor.execute(get_query)

        for row in cls.cursor:
            bus_liste.append(row)
        cls.fermer_connexion()
        return bus_liste

    @classmethod
    def ajouter_bus(cls, ligne, immat, nb_places, numero):
        
        cls.ouvrir_connexion()
        cls.cursor.execute(f"INSERT INTO bus ( id_ligne, immatriculation, nombre_places, numero) VALUES ((SELECT id_ligne from ligne WHERE nom = '{ligne}' ), '{immat}', '{nb_places}', '{numero}' )")
         
        cls.bdd.commit()
        cls.fermer_connexion()


    @classmethod
    def nom_lignes(cls):
        cls.ouvrir_connexion()
        ligne_liste=[]
        get_query="Select nom from ligne"
        cls.cursor.execute(get_query)
        for row in cls.cursor:
            ligne_liste.append(row)
        cls.fermer_connexion()
        return ligne_liste