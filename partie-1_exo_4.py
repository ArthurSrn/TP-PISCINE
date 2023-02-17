# on souhaite créer un dictionnaire qui associe des chaines de caractères à des entiers
dict = {
    "Nagaakira": 25,
    "Mitsuakira": 33,
    "Tsunakira": 39
}

# on souhaite créer une fonction qui prend en paramètre un dictionnaire et une chaine de caractères, et qui retourne l'entier associé à la chaine de caractères


def get_value(dict, key):
    if key in dict:
        return True
    else:
        return False


print(get_value(dict, "Toto"))

# on souhaite créer une fonction qui prend en paramètre un dictionnaire, une clé et une chaine de caractères, et qui ajoute la clé et la valeur au dictionnaire


def add_key_value(dict, key, value):
    dict[key] = value
    return dict


print(add_key_value(dict, "Toto", 69))
