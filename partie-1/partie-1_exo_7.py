import lorem  # pip install lorem
import random


def merge_sets(set1, set2):
    # Fusionner les deux sets en un set unique sans éléments dupliqués
    merged_set = set1.union(set2)

    # Trier les sets par ordre décroissant et les stocker dans des listes
    sorted_set1 = sorted(set1, reverse=True)
    sorted_set2 = sorted(set2, reverse=True)

    # Calculer la somme des valeurs non dupliquées du set 1 et du set 2
    sum_unique_values = sum(merged_set - set1.intersection(set2))

    # Générer une chaîne de caractères "lorem ipsum" avec un nombre de mots équivalent à la somme totale des entiers des deux sets
    lorem_words = lorem.text().split()
    sum_integers = sum(merged_set)
    lorem_text = " ".join(lorem_words[:sum_integers])

    # Créer le dictionnaire contenant toutes les valeurs calculées
    result = {
        "merged_set": merged_set,
        "sorted_sets": [sorted_set1, sorted_set2],
        "sum_unique_values": sum_unique_values,
        "lorem_text": lorem_text
    }
    return result


# Exemple d'utilisation
set1 = set(random.sample(range(50), 10))
set2 = set(random.sample(range(50), 10))
result = merge_sets(set1, set2)
print(result)
