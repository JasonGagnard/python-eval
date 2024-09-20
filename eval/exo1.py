def sommeZero(liste):
    resultats = []
    n = len(liste)

    for i in range(n - 2): # on parcourt chaque chiffre jusqu'à l'avant-dernier                     pour s'assurer qu'il reste deux éléments après.
        for j in range(i + 1, n - 1):#prend le chiffre juste apres i et on s'arrete a l'avant-dernier pour éviter de choisir le même élément que i
            for k in range(j + 1, n): # prend les derniers chiffres restants jusqu'a n
                if liste[i] + liste[j] + liste[k] == 0:
                    resultats.append([liste[i], liste[j], liste[k]])
    
    return resultats
liste1 = [2, 7, 9, -9]
liste2 = [-33, -10, -8, -2, 1, 4, 9, 10]
liste3 = [7,-3,-4,-2,8,-6]

print("Liste 1 :", sommeZero(liste1))
print("Liste 2 :", sommeZero(liste2))
print("Liste 3 :", sommeZero(liste3))
