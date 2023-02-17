# on souhaite créer une fonction qui prend une chaine de caractères en paramètre, qui convertit les deux tirets en camelCase, et qui retourne la chaine de caractères modifiée

def convert_to_camel_case(string):
    # Remplacer tous les types de tirets par des espaces
    string = string.replace('-', ' ').replace('_', ' ')
    # Diviser la chaîne en mots
    words = string.split()
    # La première partie du mot reste en minuscules
    result = words[0]
    # Les parties suivantes du mot ont la première lettre en majuscule
    for word in words[1:]:
        result += word.capitalize()
    return result


print(convert_to_camel_case("Malek-le_tricheur"))
