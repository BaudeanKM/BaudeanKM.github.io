# On commence par l'import du module random qui permet comme son nom l'indique de générer de l'aléatoire.
import random
# Ici on fait la création d'une classe comportant : le nom , les fonds disponibles, la mise enregistrée et le choix sur la roulette
class Joueurs:
    def __init__(self,nom,fond,mise,choix):
         self.nom = nom
         self.fond = fond
         self.mise = mise
         self.choix = choix
# Maintenant on définit directement les j1 j2 et j3 avec leurs fonds respectifs, leur mise de départ qui est nulle 
# et le choix sur la roulette : 1 par défaut
j1 = Joueurs("Jun",500,0,1)
j2 = Joueurs("Mag",500,0,1)
j3 = Joueurs("Ken",500,0,1)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Liste des participants
Participants = []
Participants.append(j1)
Participants.append(j2)
Participants.append(j3)

print(Participants[1].nom)

print(Participants[0].fond)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Boucle des participants (temporaire)
while Participants[0].fond > 0 or Participants[1].fond > 0 or Participants[2].fond > 0:
# Pour un peu plus de lisibilité on commence avec un affichage de texte indiquant la marche à suivre
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Mise des participants
    print("Faites vos jeux, veuillez choisir un montant à miser")
# Le joueur nommé Jun mise. Pour le moment son nom est écrit sous forme de chaîne de caractère mais sera remplacée par la suite
# par la variable : j1.nom suivi d'une "," puis de " misez". Permettant par exemple de remplacer le joueur.


    if j1.fond  > 0 : 
        print("Jun misez")
        j1.mise = int(input("Jun mise:"))
    else : print("Jun est éliminé")
# La boucle while associée au if permet de couvrir les dérives des joueurs voulant insérer un nombre négatif ou supérieur à leur fond.
    while (j1.mise > j1.fond and j1.fond != 0) or j1.mise <= 0 :
        #if  j1.fond == 0 :
            #print("C'est terminé pour Jun")
        if j1.mise > j1.fond :
            print("Vous ne possédez pas les fonds suffisants")
        elif j1.mise == 0 :
            print("Vous ne misez rien")
        else : 
            print("Votre valeur est négative !")
        j1.mise = int(input("Jun misez de nouveau2:"))
        
        
# L'indantation permet de recommencer la boucle en vérifiant sur la valeur entrée pour la mise est bonne.
    
    
    if j2.fond  > 0 : 
        print("Mag misez")
        j2.mise = int(input("Mag mise:"))
    else : print("Mag est éliminé.")
# On reproduit le schéma ici, evidemment faire attention aux ":", aux "()" et à l'indentation.
    while (j2.mise > j2.fond and j2.fond != 0) or j2.mise <= 0 :
        #if  j1.fond == 0 :
            #print("C'est terminé pour Mag")
        if j2.mise > j2.fond :
            print("Vous ne possédez pas les fonds suffisants")
        elif j2.mise == 0 :
            print("Vous ne misez rien")
        else : 
            print("Votre valeur est négative !")
        j2.mise = int(input("Mag misez de nouveau2:"))

    

    if j3.fond  > 0 : 
        print("Ken misez")
        j3.mise = int(input("Ken mise:"))
    else : print("Ken est éliminé.")
    

    while (j3.mise > j3.fond and j3.fond != 0) or j3.mise <= 0 :
        #if  j3.fond == 0 :
            #print("C'est terminé pour Ken")
        if j3.mise > j3.fond :
            print("Vous ne possédez pas les fonds suffisants")
        elif j3.mise == 0 :
            print("Vous ne misez rien")
        else : 
            print("Votre valeur est négative !")
        j3.mise = int(input("Ken misez de nouveau2:"))
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Print et boucle du choix des numéros
# Ici on affiche un texte afin d'inviter le joueur à entrer son numéro, pour le moment pas encore délimitation, tempis pour le joueur
#  il n'avait qu'à bien lire !
# Impossible maintenant de choisir un numéro non compris dans l'intervalle.
    print("Veuillez choisir un numéro entre 1 et 50")
# La valeur choix est déterminée pour chaque objet joueur
    if j1.fond > 0 :
        j1.choix = int(input("Jun choisit le numéro:"))
    else :
        print("Jun est éliminé")
    while j1.choix < 1 or j1.choix > 50 :
        j1.choix = int(input("Jun choisissez un numéro valide !"))
        print("Jun a choisit le numéro:",j1.choix)
    if j2.fond > 0 :
        j2.choix = int(input("Mag choisit le numéro:"))
    else :
        print("Mag est éliminé")
    while j2.choix < 1 or j2.choix > 50 :
        j2.choix = int(input("Mag choisissez un numéro valide !"))
        print("Mag a choisit le numéro:",j2.choix)
    if j3.fond > 0 :
        j3.choix = int(input("Ken choisit le numéro:"))
    else : 
        print("Ken est éliminé")
    while j3.choix < 1 or j3.choix > 50 :
        j3.choix = int(input("Ken choisissez un numéro valide !"))
    print("Ken a choisit le numéro:",j3.choix) 
# La roulette est lancée grace au module random, biensur on associe le nombre généré à une variable sinon ça ne fonctionne pas.
    roulette = random.randint(1, 50)
# Maintenant l'heure du verdict, les joueurs obtiennent la déduction de leurs fonds s'il ont perdu
# Ou l'ajout de 50 fois leur mise s'ils ont gagné, ici 49 fois car la mise de départ n'a en réalité pas été déduite.
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Win or Lose des participants
    if j1.choix == roulette and j1.fond > 0 :
        j1.fond = j1.fond + (j1.mise * 49)
        print(j1.nom," a gagné !")
        print(j1.nom," a ",j1.fond," euros.")
    elif j1.fond == 0 :
        print(j1.nom," est éliminé.")
    else : 
        j1.fond -= j1.mise 
        print(j1.nom," a perdu !")
        print(j1.nom," a ",j1.fond," euros.")
    
    if j2.choix == roulette and j2.fond > 0 :
        j2.fond = j2.fond + (j2.mise * 49)
        print(j2.nom," a gagné !")
        print(j2.nom," a ",j2.fond," euros.")
    elif j2.fond == 0 :
        print(j2.nom," est éliminé.")
    else :
        j2.fond -= j2.mise 
        print(j2.nom," a perdu !")
        print(j2.nom," a ",j2.fond," euros.")
    if j3.choix == roulette and j3.fond > 0 :
        j3.fond == j3.fond + (j3.mise * 49)
        print(j3.nom," a gagné !")
        print(j3.nom," a ",j3.fond," euros.")
    elif j3.fond == 0 :
        print(j3.nom," est éliminé.")
    else :
        j3.fond -= j3.mise 
        print(j3.nom," a perdu !")
        print(j3.nom," a ",j3.fond," euros.")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Affichage du montant sur la roulette
    print("Le numéro était le :",roulette)
print("Fin de partie")
# A la fin les joueurs ont l'information sur le numéro de la roulette. Sur ce code les informations sont maintenant sauvegardées et les joueurs éliminés.
         

   