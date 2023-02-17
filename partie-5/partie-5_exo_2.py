# on souhaite écrire une fonction en Python qui implémente un algorithme de tri topologique sur un graphe orienté acyclique (DAG) représenté sous forme d'une liste d'adjacence où les clés sont des noeuds et les valeurs sont des listes de noeuds adjacents

def topological_sort(graph):
    """
    Implémente l'algorithme de tri topologique sur un DAG représenté sous forme de liste d'adjacence.

    Args:
        graph (dict): Le graphe orienté acyclique représenté sous forme de liste d'adjacence où les clés sont des noeuds et les valeurs sont des listes de noeuds adjacents.

    Returns:
        list: La liste ordonnée des noeuds du graphe.
    """
    # Initialisation des variables
    # Le degré d'entrée de chaque noeud
    in_degree = {node: 0 for node in graph}
    queue = []  # La file d'attente pour les noeuds avec un degré d'entrée nul
    result = []  # La liste ordonnée des noeuds

    # Calcul du degré d'entrée de chaque noeud
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Ajout des noeuds avec un degré d'entrée nul à la file d'attente
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    # Parcours du graphe
    while queue:
        node = queue.pop(0)
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Vérification que le graphe est acyclique
    if len(result) != len(graph):
        raise ValueError("Le graphe contient un cycle !")

    return result


# exemple d'utilisation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

print(topological_sort(graph))
