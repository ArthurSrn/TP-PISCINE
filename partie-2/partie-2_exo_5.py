# on souhaite créer une fonction qui prend en paramètre une chaine de caractères et qui retourne le nombre de fois que chaque lettre apparaît dans la chaine de caractères
# les lettres doivent être retournées par ordre croissant d'occurence, et si deux lettres apparaissent le même nombre de fois, elles doivent être retournées par ordre alphabétique

def count_letters(string):
    # on crée un dictionnaire qui va contenir les lettres et le nombre d'occurences
    letters = {}
    # on parcourt la chaine de caractères
    for letter in string:
        # on vérifie si la lettre est déjà dans le dictionnaire
        if letter in letters:
            # si oui, on incrémente le nombre d'occurences
            letters[letter] += 1
        else:
            # si non, on initialise le nombre d'occurences à 1
            letters[letter] = 1
    # on crée une liste qui va contenir les lettres et le nombre d'occurences
    letters_list = []
    # on parcourt le dictionnaire
    for letter in letters:
        # on ajoute les lettres et le nombre d'occurences à la liste
        letters_list.append([letter, letters[letter]])
    # on trie la liste par ordre croissant d'occurences
    letters_list.sort(key=lambda x: x[1])
    # on retourne la liste
    return letters_list


print(count_letters("Nagaakira"))
