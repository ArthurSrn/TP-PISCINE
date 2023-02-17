chiffreRomain = "MCMXCIV"

# on souhaite créer une fonction qui prend en paramètre un chiffre romain et qui retourne son équivalent en chiffre


def roman_to_int(param):
    # on crée un dictionnaire qui associe chaque lettre à un chiffre
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # on crée une variable qui va contenir le résultat
    result = 0
    # on crée une boucle qui va parcourir chaque lettre du chiffre romain
    for i in range(len(param)):
        # si la lettre actuelle est inférieure à la lettre suivante, on soustrait la valeur de la lettre actuelle à la variable result
        if i < len(param) - 1 and dict[param[i]] < dict[param[i + 1]]:
            result -= dict[param[i]]
        # sinon, on ajoute la valeur de la lettre actuelle à la variable result
        else:
            result += dict[param[i]]
    # on retourne le résultat

    # on gère les cas de 1 à 3999
    if result > 3999:
        return "Erreur: chiffre trop grand"
    else:
        return result


print(roman_to_int(chiffreRomain))
