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





#exemple de code pour info
    """
    @classmethod
    def maj_apprenants(cls, mails):
        cls.ouvrir_connexion()
        promo = {}

        query="SELECT id_personne, nom, prenom, mail FROM personnes"
        cls.cursor.execute(query)
        
        for (id_personne, nom, prenom, mail) in cls.cursor :
            apprenant = Apprenant(id_personne, mail, prenom, nom)
            promo[nom] = apprenant

        for mail in mails :
            nom_mail = mail.split(".")
            
            if len(nom_mail) > 1 :
                debut_nom = nom_mail[1]
                debut_nom = debut_nom[:4].lower().replace("-", " ")
                for cle, apprenant in promo.items():
                    debut_cle = cle[:4].lower()
                    
                    if debut_nom == debut_cle:
                        apprenant.adresse = mail

        for apprenant in promo.values():
            print(apprenant.adresse, apprenant.id)
            cls.cursor.execute("UPDATE personnes SET mail = %s WHERE id_personne = %s", (apprenant.adresse, apprenant.id))
            cls.bdd.commit()


        cls.fermer_connexion()
        print("fin de la mise à jour")"""