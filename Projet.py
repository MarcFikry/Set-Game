#Marc Fikry
#Projet : le jeu “Set”, [INF204] 

import random
from turtle import *

#4.1 Initialisation du jeu et affichage textuel
#4.1.1 Fonction texte_carte

def texte_carte(dcarte):
    return dcarte['forme'] + " " + dcarte['couleur'] + " " + dcarte['texture'] + " " + str(dcarte['nombre'])

#4.1.2 Fonction afficher_texte_liste
def afficher_texte_liste(lcartes):
    for i in range(len(lcartes)):
        print(i, texte_carte(lcartes[i]))

#4.1.3 Fonction init_pioche_alea

def init_pioche_alea():
    carac = {'couleur': ['rouge', 'vert', 'violet'], 'forme': ['ovale', 'losange', 'vague'], 'nombre': [1, 2, 3], 'texture': ['vide', 'raye', 'plein']}
    pioche = []
    for i in carac['couleur']:
        for j in carac['nombre']:
            for k in carac['forme']:
                for l in carac['texture']:
                    pioche.append({'couleur': i, 'nombre': j, 'forme': k, 'texture': l})
    random.shuffle(pioche)
    return pioche

#4.1.4 Fonction piocher_cartes

def piocher_cartes(nb, pioche, expo):
    if nb > len(pioche):
        nb = len(pioche)
    for i in range(nb):
        expo.append(pioche[0])
        pioche.pop(0)
    
#4.2 Affichage graphique
#4.2.1 Fonction rectangle

def rectangle(x, y, largeur, hauteur):
    up()
    goto(x,y)
    forward(5)
    down()
    for i in range(2):
        forward(largeur-10)
        right(180)
        circle(5, -90)
        right(180)
        forward(hauteur-10)
        right(180)
        circle(5, -90)
        right(180)

#4.2.2 Fonction carte_vers_nom_fichier

def carte_vers_nom_fichier(dcarte):
    return "images/" + dcarte['forme'] + "_" + dcarte['couleur'] + "_" + dcarte['texture'] + ".gif"

#4.2.3 Fonction afficher_carte

# fournie
def charger_images():
    """ Ouvre la fenetre graphique et permet de charger les images correspondant aux differents
    dessins du jeu, en vue de l'affichage graphique en turtle"""
    # ouvrir et dimensionner fenetre turtle
    fenetre = Screen()
    setup(width=1100, height=800)
    # charger toutes les images
    base = "images/"
    extension = ".gif"
    for forme in ["losange", "ovale", "vague"]:
        for couleur in ["rouge", "vert", "violet"]:
            for texture in ["plein", "raye", "vide"]:
                nom_fichier = base + forme + "_" + couleur + "_" + texture + extension
                fenetre.register_shape(nom_fichier)

# fournie
def reinitialiser_affichage():
    """Efface l'affichage actuel et restaure les parametres
    de vitesse de tortue (au plus rapide) et de cacher le curseur"""
    # effacer fenetre graphique
    reset()
    # mais on a aussi rénitialisé certains paramètres, on restaure :
    # accelerer l'affichage et cacher la tortue
    speed("fastest")
    hideturtle()


# fournie
def afficher_symbole(x, y, nom_fichier):
    """Affiche le symbole correspondant a l'image stockee dans le fichier de nom indiqué dans
    nom_fichier. Le centre du symbole est aux coordonnees (x,y) de la fenetre.La taille du symbole est
    de 100 (en largeur) sur 50 (en hauteur)."""
    up()
    goto(x, y)
    shape(nom_fichier)
    stamp()  # pour afficher le symbole (comme un tampon)
    down()
    hideturtle()


# fournie
def ecrire_xy(texte, x, y):
    """Ecrit le texte contenu dans l'argument texte, a une position dont le centre est
    aux coordonnees (x,y)"""
    up()
    goto(x, y)
    write(texte, True, font=("Arial", 14, "normal"))
    down()

def afficher_carte(dcarte, x, y, num):
    rectangle(x, y, 140, 200)
    ecrire_xy(num, x+5, y-20)
    nombre = dcarte['nombre']
    if nombre == 1:
        afficher_symbole(x+70, y-100, carte_vers_nom_fichier(dcarte))
    elif nombre == 2:
        for i in range(2):
            afficher_symbole(x + 70, y - 70 - 65*i, carte_vers_nom_fichier(dcarte))
    else :
        for i in range(3):
            afficher_symbole(x + 70, y - 35 - 65*i, carte_vers_nom_fichier(dcarte))

#4.2.4 Fonction afficher_cartes_exposees

def afficher_cartes_exposees(expo):
    reinitialiser_affichage()
    for i in range(len(expo)):
        afficher_carte(expo[i], -400 + ((i // 3) * 170), 350 - ((i % 3) * 230), i)

#4.2.5 Fonction mettre_en_valeur_set

def mettre_en_valeur_set(lset):
    for i in lset:
        up()
        goto(-410 + ((i // 3) * 170), 360 - ((i % 3) * 230))
        forward(5)
        down()
        color("blue")
        width(2)
        for i in range(2):
            forward(150)
            right(180)
            circle(5, -90)
            right(180)
            forward(210)
            right(180)
            circle(5, -90)
            right(180)

#4.3 Règles du jeu
#4.3.1 Fonction toutes_differentes

def toutes_differentes(carte1, carte2, carte3, cle):
    if carte1[cle] == carte2[cle] or carte2[cle] == carte3[cle] or carte3[cle] == carte1[cle] :
        return False
    else:
        return True

#4.3.2 Fonction toutes_egales

def toutes_egales(carte1, carte2, carte3, cle):
    if carte1[cle] == carte2[cle] and carte2[cle] == carte3[cle] :
        return True
    else:
        return False

#4.3.3 Fonction set_valide

def set_valide(carte1, carte2, carte3):
    for cle in ['couleur', 'forme', 'texture', 'nombre']:
        if (toutes_differentes(carte1, carte2, carte3, cle) == False) and (toutes_egales(carte1, carte2, carte3, cle) == False):
            return False
    return True

#4.3.4 Fonction chercher_set

def chercher_set(expo):
    for i in range(len(expo)):
        for j in range(i+1,len(expo)):
            for l in range(j+1,len(expo)):
                if set_valide(expo[i], expo[j], expo[l]) == True:
                    return [i, j, l]
    return None

#4.3.5 Fonction supprimer_set

def supprimer_set(expo, lset):
    lset.sort(reverse=True)
    for i in lset:
        expo.pop(i)

#4.4 Partie en mode automatique et statistiques
#4.4.1 Fonction partie_auto

def partie_auto(nb_cartes=12, affichage=True):
    pioche = init_pioche_alea()
    expo = []
    piocher_cartes(nb_cartes, pioche, expo)
    if affichage:
        afficher_cartes_exposees(expo)
    while len(pioche) != 0 or chercher_set(expo) != None:
        if chercher_set(expo) != None:
            lset = chercher_set(expo)
            if affichage:
                print("Set trouvé :", lset)
                mettre_en_valeur_set(lset)
                input("Appuyez entrée pour continuer")
                print("Set supprimée")
            supprimer_set(expo, lset)
            if len(pioche) != 0 and len(expo) < 12:
                piocher_cartes(3, pioche, expo)
        elif chercher_set(expo) == None and len(pioche) != 0:
            if affichage:
                print("Pas de set trouvé, exposition de nouveaux 3 cartes...")
                input("Appuyez entrée pour continuer")
                print("3 nouveaux carte exposée")
                piocher_cartes(3, pioche, expo)
        if affichage:
            afficher_cartes_exposees(expo)
    if affichage:
        print("Pas de set restant, partie terminée"+"\n"+"Nombre de cartes restant =", len(expo))
    return len(expo)

#4.4.2 Fonction statistiques

def statistiques(nb_sim, nb_cartes=12, affichage=True):
    aucun = 0; somme = 0; min = 81; max = 0
    for i in range(nb_sim):
        reste = partie_auto(nb_cartes, affichage)
        somme += reste
        if reste < min:
            min = reste
        if reste > max:
            max = reste
        if reste == 0:
            aucun += 1
    if affichage:
        print("Pour", nb_sim, "parties automatiques avec", nb_cartes,
              "cartes exposées :"+"\n"+"Nombre de fois ou il ne reste aucune carte :",
              str(aucun) + "\n" + "Il reste au minimum", min, "cartes, au maximum", max,
              "cartes" + "\n" + "avec une moyenne de", somme/nb_sim, "cartes restantes.")
    return aucun, min, max, somme/nb_sim

#4.5 Partie pour des joueurs humains
#4.5.1 Fonction saisie_noms

def saisie_noms(nb_joueurs):
    i = 1
    joueurs = []
    while i <= nb_joueurs:
        nom = input("Nom du joueur " + str(i) + " : ")
        if nom.lower() == 'help':
            print("Erreur, le nom help est interdit à utiliser")
        elif nom in joueurs:
            print("Erreur, ce nom est déjà pris ")
        else:
            i += 1
            joueurs.append(nom)
    return joueurs

#4.5.2 Fonction init_score

def init_score(lnoms):
    scores_i = {}
    for joueur in lnoms:
        scores_i[joueur] = 0
    return scores_i

#4.5.3 Fonction afficher_score

def afficher_score(scores):
    print("Scores intermediaires :")
    for joueur in scores :
        print("  ", joueur, ":", scores[joueur], "cartes gagnées")

#4.5.4 Fonction afficher_gagnants

def afficher_gagnants(scores):
    gagnants = []
    for joueur in scores:
        max = 0
        for score in joueur:
            if int(score) > max:
                max = score
        if max > 0:
            gagnants.append(joueur)
    return gagnants

#4.5.5 Fonction tour_de_jeu

def maxi(liste):
    maxi = 0
    for i in range(len(liste)):
        if int(liste[i]) > maxi :
            maxi = int(liste[i])
    return maxi

def tour_de_jeu(pioche, expo, dscore):
    afficher_cartes_exposees(expo)
    joueur = input("Qui sera le plus rapide ?"+"\n"+"Entrez le nom du joueur qui a trouve un set"+"\n"+"ou ’help’ pour demander de l’aide a l’ordinateur : ")
    while (joueur not in dscore) and (joueur != "help"):
        joueur = input('Erreur, veuillez entrez un nom valide ou "help" : ')
    if joueur == "help":
        if chercher_set(expo) != None:
            aide = input("Il y a un set dans les cartes exposées, voulez-vous en prendre connaissance? (oui/non) : ")
            if aide.lower() == "oui":
                lset = chercher_set(expo)
                print("Voici le set :", lset)
                mettre_en_valeur_set(lset)
                input("Taper sur entrée pour continuer")
                supprimer_set(expo, lset)
                if len(expo) < 12:
                    piocher_cartes(3, pioche, expo)       
        else:
            print("Pas de set dans les cartes exposées, trois cartes en plus seront affichées.")
            piocher_cartes(3, pioche, expo)   
    else:
        lset = []
        for i in range(1,4):
            lset.append(int(input("Entrez le carte numéro " + str(i) + " : ")))
        if maxi(lset) >= len(expo):
            print("Un carte ou plus n'existe pas")
        elif not set_valide(expo[lset[0]], expo[lset[1]], expo[lset[2]]): 
            print("Set incorrecte")
        else:
            mettre_en_valeur_set(lset)
            supprimer_set(expo, lset)
            input("Set selectionée, appuyez entrée pour continuer : ")
            if len(pioche) != 0 and len(expo) < 12:
                piocher_cartes(3, pioche, expo)
            dscore[joueur] += 3
            
                
#4.5.6 Fonction partie_humain

def partie_humain(nb_joueurs=1):
    lnoms = saisie_noms(nb_joueurs)
    dscore = init_score(lnoms)
    pioche = init_pioche_alea()
    expo = []
    piocher_cartes(12, pioche, expo)
    while len(pioche) != 0 or chercher_set(expo) != None:
        tour_de_jeu(pioche, expo, dscore)
        afficher_score(dscore)   
    print("Fin de la partie"+"\n""Nombre de cartes restantes :", expo, "cartes."+"\n"+"Les gagnants sont", afficher_gagnants(dscore))

#Programme principale

if __name__ == '__main__' :
    # charger les images pour affichage graphique
    charger_images()  # a mettre en commentaire si le programme principal n'utilise pas d'affichage graphique
    nb_joueurs = int(input("Combie de joueurs ? : "))
    partie_humain(nb_joueurs)