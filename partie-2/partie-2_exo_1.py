a = "Malek le tricheur"
b = "Balek le tricheur"

# on souhaite créer une fonction qui renvoie le nombre de positions où les deux chaines de caractères sont différentes


def compare_strings(string1, string2):
    if len(string1) == len(string2):
        return len([i for i in range(len(string1)) if string1[i] != string2[i]])
    else:
        return "Erreur: les deux chaines de caractères ne sont pas de la même longueur"


print(compare_strings(a, b))
