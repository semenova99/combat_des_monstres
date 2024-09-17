"""
Artemiy Semenov 307
13 Septembre 2024
Le combat des monstres
"""

import random

niveau_vie = 20
force_monstre = None
n_monstre = 0
n_victoires = 0
n_defaites = 0
n_victoires_consecutives = 0

def is_boss():
    global n_victoires
    # à chaque 3 victoires, il y a un boss. Si la bataille avec le boss a été perdue, on ne recommence pas la bataille avec un nouveau boss (n_victoires_consecutives est 0 et non plus grand dans ce cas-ci.)
    return n_victoires % 3 == 0 and n_victoires != 0 and n_victoires_consecutives != 0

def play_game():
    global force_monstre, n_monstre, niveau_vie, n_victoires, n_defaites, n_victoires_consecutives
    if(is_boss()):
        force_monstre = 10
        print("Vous tombez face à face avec un boss!!! sa difficulté est de 10 et vous n'avez pas le choix de le contourner.")
    else:
        force_monstre = random.randint(1, 10)
        print("Vous tombez face à face avec un monstre de difficulté: " + str(force_monstre))

    n_monstre += 1




    reponse = "none"
    while not reponse.isdigit() or not int(reponse) < 5 or not int(reponse) > 0 or (int(reponse) == 2 and is_boss()):
        if is_boss():
            affiche = """Que voulez-vous faire?
1- Combattre cet adversaire
3- Afficher les règles du jeu
4- Quitter la partie"""
        else:
            affiche = """Que voulez-vous faire?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie"""
        reponse = input(affiche)

    reponse = int(reponse)

    if reponse == 1:
        print("Monstre numéro " + str(n_monstre))
        print("Force: " + str(force_monstre))
        print("Votre niveau de vie: " + str(niveau_vie))
        print("Combat " + str(n_monstre) + ": " + str(n_victoires) + " victoires vs " + str(n_defaites) + " défaites")

        reponse_de = de() + de()
        print("Somme de deux lancers de dés: " + str(reponse_de))
        if reponse_de > force_monstre:
            n_victoires += 1
            niveau_vie += force_monstre
            print("Vous avez gagné le combat!")
            print("Niveau de vie: " + str(niveau_vie))
            n_victoires_consecutives += 1
            print("Nombre de victoires consécutives: " + str(n_victoires_consecutives))
            play_game()
        else:
            n_defaites += 1
            niveau_vie -= force_monstre
            print("Vous avez perdu le combat...")
            n_victoires_consecutives = 0
            if(niveau_vie > 0):
                print("Niveau de vie: " + str(niveau_vie))
                play_game()
            else:

                print("Vous êtes mort. La partie est terminée, vous avez vaincu " + str(n_victoires) + " monstre(s).")
                restart_game()

    elif reponse == 2:
        niveau_vie -= 1
        print("Vous avez perdue une vie, car vous avez décidé de fuir.")
        if (niveau_vie > 0):
            print("Niveau de vie: " + str(niveau_vie))
            play_game()
        else:

            print("Vous êtes mort. La partie est terminée, vous avez vaincu " + str(n_victoires) + " monstre(s).")
            restart_game()
    elif reponse == 3:
        print("""Pour réussir un combat, il faut que la valeur de deux dés lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent à 0 (ou moins).

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.""")
        play_game()
    elif reponse == 4:
        print("Merci et au revoir...")


def de():
    return random.randint(1, 6)

def restart_game():
    global niveau_vie, force_monstre, n_monstre, n_victoires, n_defaites, n_victoires_consecutives
    niveau_vie = 20
    force_monstre = None
    n_monstre = 0
    n_victoires = 0
    n_defaites = 0
    n_victoires_consecutives = 0
    print("\n\n\n\n\n--- NOUVELLE PARTIE ---")
    play_game()


play_game()