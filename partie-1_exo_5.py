# on souhaite créer une fonction qui recoit un entier n compris entre 5 et 30

# La fonction doit retourner toutes les combinaisons possibles pour obtenir n avec 5 dés à 6 faces

def get_combinations(n):
    # on crée une liste qui va contenir toutes les combinaisons possibles
    combinations = []
    # on crée une boucle qui va parcourir toutes les combinaisons possibles
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    for m in range(1, 7):
                        # on vérifie si la somme des dés est égale à n
                        if i + j + k + l + m == n:
                            # on ajoute la combinaison à la liste
                            combinations.append([i, j, k, l, m])
    # on retourne la liste
    return combinations


print(get_combinations(20))
