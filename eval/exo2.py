def total(n1, n2):
    # ici nous inversons la liste pour pouvoir commencer avec l'unité et pas la centaine
    n1 = n1[::-1]
    n2 = n2[::-1]
    
    # On ajoute les zero manquant afin qu'il n'y ait pas de probleme sur l'adition exemple 7 =007
    max_len = max(len(n1), len(n2))
    n1 += [0] * (max_len - len(n1))
    n2 += [0] * (max_len - len(n2))
    
    resultat =[]
    carry = 0

    # Addition des chiffres un par un avec la retenue 
    for i in range(max_len):
        somme = n1[i] + n2[i] + carry
        resultat.append(somme % 10)
        carry = somme // 10

    # Si une retenue reste à la fin pour l'ajouter
    if carry:
        resultat.append(carry)

    # on remet le resultat à son ordre d'origine
    return resultat[::-1]

print(total([8, 4, 0], [8, 3]))  
print(total([1, 8, 3], [7]))     
print(total([1, 2, 3], [0]))     
print(total([8, 3, 0], [0, 11, 3]))
