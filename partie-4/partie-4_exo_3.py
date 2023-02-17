# Exercice 3: Binary Trees

# on souhaite créer deux arbres binaires distincts.

# on veut ensuite écrire une fonction qui accepte en argument les deux arbres binaires et renvoie un arbre binaire qui est la fusion des deux arbres d'entrée

# enfin nœud de l'arbre fusionné doit avoir une valeur qui est la somme des valeurs des nœuds correspondants dans les deux arbres d'entrée.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1
    merged_node = TreeNode(t1.val + t2.val)
    merged_node.left = mergeTrees(t1.left, t2.left)
    merged_node.right = mergeTrees(t1.right, t2.right)
    return merged_node
