# on crée une liste de chaines de caractères
noms = ["Malek le tricheur", "Nagaakira", "Mitsuakira", "Tsunakira"]

# on crée une fonction qui prend en paramètre une liste et un entier


def get_element(liste, indice):
    if indice < len(liste):
        # la fonction retourne la chaine de caractères à l'indice donné
        return liste[indice]
    else:
        # si l'indice spécifié n'est pas dans la liste, on retourne une erreur
        return "Erreur: indice non valide"


print(get_element(noms, 0))
