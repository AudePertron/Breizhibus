from connexion import Connexion


lignes = Connexion.lister_lignes()

print("liste des lignes de bus de Ploukusanagi :" + str(lignes))

ligne_utilisateur = input("tapez le nom d'une ligne : ")

arrets = Connexion.lister_arrets(ligne_utilisateur)

print("liste des arrets de la ligne :" + str(arrets))
