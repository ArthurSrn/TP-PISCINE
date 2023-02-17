# on crée une liste de chaines de caractères
noms = ["Malek le tricheur", "Nagaakira", "Mitsuakira", "Tsunakira"]

# on crée une fonction qui prend en paramètre une liste et une chaine de caractères, et qui ajoute la chaine à la fin de la liste


def ajouter_element(liste, element):
    liste.append(element)
    return liste

# on crée une autre fonction qui prend en paramètre notre liste et une chaine de caractères, et qui supprime la première occurence de la chaine spécifiée dans la liste, si la chaine n'est pas dans la liste, on retourne une erreur


def supprimer_element(liste, element):
    if element in liste:
        liste.remove(element)
        return liste
    else:
        return "Erreur: l'élément n'est pas dans la liste"


print(ajouter_element(noms, "Toto"))

print(ajouter_element(noms, "Toto"))

print(supprimer_element(noms, "Toto"))
