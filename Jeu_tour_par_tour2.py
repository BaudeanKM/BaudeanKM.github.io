import random
#Deuxieme Version 
from sys import version
 
if version[0] == "3":
    raw_input = input
#////////////////////////////////////////
#///////////Armes disponibles////////////
#////////////////////////////////////////
poings = random.randint(1,3)
branche = random.randint(1,4)
#La classe joueur
class Personnage:
        def __init__(self,nom,niveau,experience,pdv,arme):
            self.nom=nom
            self.niveau=niveau
            self.experience=experience
            self.pdv=pdv
            self.arme=arme
            
def combat(Ken,Anthony):
        while Anthony.pdv > 0 and Ken.pdv > 0 :
            print ("Au tour de Zentama.")
            print ("1.Attaquer")
            print ("2.Fuir")
            i = int(input("Choisissez 1 ou 2: "))
            if i == 1:
                armes()
                Anthony.pdv -= Ken.arme
                print(Ken.nom," inflige ",Ken.arme," dégats à ",Anthony.nom)
                print("Il reste ",Anthony.pdv," points de vie à ",Anthony.nom,".")
                armes()
            elif i == 2:
                print (Ken.nom," a fui le combat")
                break
            else :
                print ("Choix incorrect !")
#/////////////////////////////////////////////
#///////////////Tour de Jun///////////////////
#/////////////////////////////////////////////
            print ("Au tour de Jun.")
            print ("1.Attaquer")
            print ("2.Fuir")
            i = int(input("Choisissez 1 ou 2: "))
            if i == 1:
                armes()
                Ken.pdv -= Anthony.arme
                print(Anthony.nom," inflige ",Anthony.arme," dégats à ",Ken.nom)
                print("Il reste ",Ken.pdv," points de vie à ",Ken.nom,".")
                armes()
            elif i == 2:
                print (Anthony.nom," a fui le combat")
                break
            else :
                print ("Choix incorrect !")

#Armes disponibles
def armes():
    Ken.arme = random.randint(1,3)
    Anthony.arme = random.randint(1,4)

Ken = Personnage("Zentama",1,0,10,random.randint(1,3))
Anthony = Personnage("Jun",1,0,10,random.randint(1,4))
print("Un", Anthony.nom, "sauvage apparait !")
print(Ken.nom," Go !")
combat(Ken,Anthony)