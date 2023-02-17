# on souhaite créer une liste d'entiers désordonnés de 20 éléments


# on souhaite créer une fonction qui établit un arbre binaire à partir de la liste, et qui retourne la valeur minimale de l'arbre


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    if not nums:
        return None

    nums.sort()
    mid = len(nums) // 2

    root = TreeNode(nums[mid])

    root.left = create_binary_tree(nums[:mid])
    root.right = create_binary_tree(nums[mid+1:])

    return root


def min_value(root):
    if not root:
        return None

    while root.left:
        root = root.left

    return root.val


liste = [8, 3, 10, 1, 6, 14, 4, 7, 13, 9, 12, 2, 5, 11, 15, 16, 17, 18, 19, 20]
root = create_binary_tree(liste)
print(min_value(root))
