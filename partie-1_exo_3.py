# on crée une variable et on lui affecte la valeur "Malek le tricheur, n'est pas un bon samurai"
variable = "Malek le tricheur, n'est pas un bon samurai"

# on veut transformer cette chaine de caractères en une liste de mots


def split_string(string):
    return string.split()


print(split_string(variable))

# on souhaite afficher le nombre de mots dans la variable
print(len(split_string(variable)))

# on souhaite fusionner les mots de la liste en une seule chaine de caractères séparée par des espaces
print(" ".join(split_string(variable)))

# on souhaite vérifier si la chaine de caractères "tricheur" est dans la variable
print("tricheur" in variable)
