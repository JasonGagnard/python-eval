def separationMotsEspace(phrase):
    # Séparer la phrase en mots en utilisant les espaces comme séparateurs
    mots = []
    espace = []
    
    # On commence par le début de la phrase
    parcourPhrase = 0

    # Parcourir chaque caractère de la phrase
    for i, char in enumerate(phrase):
        # Si le caractère est un espace ou une virgule
        if char in [' ', ',']:
            # Ajouter le mot trouvé à la liste des mots
            mots.append(phrase[parcourPhrase:i])
            # Ajouter les espaces à la liste qui est faite pour
            espace.append(char)
            # Mettre à jour l'index du dernier mot trouvé
            parcourPhrase = i + 1
    
    # Ajouter le dernier mot s'il y en a un
    mots.append(phrase[parcourPhrase:])

    if parcourPhrase < len(phrase):
        espace.append('')

    return [mots, espace]

phrase1 = "J'ai découvert Python cette semaine"
phrase2 = "La lune sera pas toujours pleine, PNL"
phrase3 = "Je suis Jason Gagnard"



print(separationMotsEspace(phrase1))
print(separationMotsEspace(phrase2))
print(separationMotsEspace(phrase3))

