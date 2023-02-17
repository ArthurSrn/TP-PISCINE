
#  on souhaite utiliser une structure d'arbre avec :

# en entrée: Un texte brut contenant un ensemble de caractères uniques.

# en sortie: Un arbre de Huffman avec les fréquences associées à chaque nœud. Un tableau associant chaque caractère au code binaire obtenu en parcourant le chemin depuis la racine de l'arbre jusqu'au nœud associé à ce caractère.


from queue import PriorityQueue


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # On compte les fréquences des caractères dans le texte
    freqs = {}
    for char in text:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

    # Ici, on crée une file de priorité pour les nœuds de l'arbre de Huffman
    priority_queue = PriorityQueue()
    for char, freq in freqs.items():
        priority_queue.put(Node(freq, char))

    # Ici, on construit l'arbre de Huffman à partir de la file de priorité
    while priority_queue.qsize() > 1:
        node1 = priority_queue.get()
        node2 = priority_queue.get()
        parent = Node(node1.freq + node2.freq, left=node1, right=node2)
        priority_queue.put(parent)

    # Ici, le dernier nœud restant dans la file de priorité est la racine de l'arbre de Huffman
    root = priority_queue.get()

    # ici on parcourt l'arbre de Huffman pour générer des codes binaires pour chaque caractère
    codes = {}
    current_code = ""

    def traverse(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")
    traverse(root, current_code)

    return root, codes
