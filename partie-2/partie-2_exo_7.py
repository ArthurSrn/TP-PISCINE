# on souhaite créer une liste de 10 nombres aléatoires compris entre 0 et 100

liste = [
    {
        'nom': 'Malek le tricheur',
        'score': 1000,
        'niveau': 5
    },
    {
        'nom': 'Nagaakira',
        'score': 800,
        'niveau': 4
    },
    {
        'nom': 'Mitsuakira',
        'score': 700,
        'niveau': 3
    },
    {
        'nom': 'Tsunaakira',
        'score': 600,
        'niveau': 2
    },
    {
        'nom': 'Tsunaga',
        'score': 500,
        'niveau': 1
    }
]

# on souhaite trier la liste par ordre décroissant de score
liste.sort(key=lambda x: x['score'], reverse=True)
# print(liste)

# on souhaite afficher les 3 meilleurs scores
# print(liste[:3])

# on souhaite créer une fonction qui prend en paramètre le nom d'un joueur et qui retourne son score


def get_score(nom):
    for joueur in liste:
        if joueur['nom'] == nom:
            return joueur['score']
    return 'Joueur introuvable'


# print(get_score('Tsunaga'))

# on souhaite créer une fonction qui retourne le score moyen de tous les joueurs


def get_score_moyen():
    total = 0
    for joueur in liste:
        total += joueur['score']
    return total / len(liste)


# print(get_score_moyen())

# on souhaite créer une fonction qui prend en paramètre le nom d'un joueur et un nouveau score et qui met à jour le score du joueur


def update_score(nom, score):
    for joueur in liste:
        if joueur['nom'] == nom:
            joueur['score'] = score
            return joueur['score']
    return 'Joueur introuvable'


# print(update_score('Tsunaga', 1000))
# print(liste)

# on souhaite créer une fonction qui accepte 3 paramètres: nom, score, niveau et qui ajoute un nouveau joueur à la liste
# on veut vérifier que le nom n'existe pas déjà dans la liste
# s'il n'existe pas, on ajoute le joueur à la liste, et on affiche les 3 meilleurs scores


def add_player(nom, score, niveau):
    for joueur in liste:
        if joueur['nom'] == nom:
            return 'Joueur déjà existant'
    liste.append({
        'nom': nom,
        'score': score,
        'niveau': niveau
    })
    liste.sort(key=lambda x: x['score'], reverse=True)
    return liste[:3]


print(add_player('Izuku Midoriya', 6000, 1))
