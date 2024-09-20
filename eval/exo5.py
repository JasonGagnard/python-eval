def jeu():
    print("Mémorisez un nombre entier entre 1 et 100, ne trichez pas :")

    min_val = 1
    max_val = 100
    essais = 0

    while True:
        # Proposer un nombre au milieu de l'intervalle
        proposition = (min_val + max_val) // 2
        essais += 1

        # Demander la réponse de l'utilisateur+
        reponse = input(f"Le script propose {proposition}... +, - ou G ? ").strip().lower()

        # pour rappeler les reponses possible si reponse non valide
        if reponse not in ['+', '-', 'g']:
            print("Réponse invalide. Veuillez entrer '+', '-' ou 'G'.")
            essais -= 1
            continue

   
        if reponse == '+' and proposition == max_val:#ici on montre que si il dit + alors qu'il n'y a pas + ca signifie la triche
            print(f"Tricheur !!! Vous ne pouvez pas dire '+' quand la proposition est {proposition} gros nullos")
            print(f"J'ai gagné par forfait en {essais} coups !!!")
            break
        elif reponse == '-' and proposition == min_val:#la même chose mais pour l'inférieur
            print(f"Tricheur !!! Vous ne pouvez pas dire '-' quand la proposition est {proposition} j'ai gagné!!!!!")
            print(f"OUAHHHH!!!! J'ai gagné par forfait en {essais} coups !!! Bravo!")
            break

        # adaptaption des valeur sur la reponse donner
        if reponse == '+':
            min_val = proposition + 1
        elif reponse == '-':
            max_val = proposition - 1
        elif reponse == 'g':
            print(f"Le script a trouvé {proposition} en {essais} coups !!!")
            break

# Lancer le jeu
jeu()
