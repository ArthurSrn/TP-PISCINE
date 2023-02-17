# on souhaite créer un tableau de 10 entiers, de 0 à 9
entiers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# on souhaite créer une fonction qui prend en paramètre un tableau d'entiers de 0 à 9 et qui les formatte en numéro de téléphone américain


def create_phone_number(param):
    # on crée une variable qui va contenir le résultat
    # on crée une boucle qui va parcourir chaque entier du tableau
    formatted_number = "(" + str(param[0]) + str(param[1]) + str(param[2]) + ") " + str(param[3]) + str(
        param[4]) + str(param[5]) + "-" + str(param[6]) + str(param[7]) + str(param[8]) + str(param[9])

    # on retourne le résultat
    return formatted_number


print(create_phone_number(entiers))
