#
#   Binary Trees
#

"""
Exercice 0 : definition de la classe arbre
"""


class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


"""
Exercice 1 : tailler un arbre
"""


def size(tree):
    if tree is None:
        return 0
    else:
        return 1 + size(tree.left) + size(tree.right)


"""
Exercice 2 : prends de la hauteur !
"""


def height(tree):
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.left), height(tree.right))


"""
Exercice 3 : compter les feuilles de l'arbre
"""


def nb_leaves(tree):
    count = 0

    if tree is None:
        return 0

    if tree.left is None and tree.right is None:
        count += 1
    if tree.left:
        count += nb_leaves(tree.left)
    if tree.right:
        count += nb_leaves(tree.right)

    return count


"""
Exercice 4 : recherche dans un arbre
"""


def search(tree, x):
    if tree is None:
        return False
    else:
        if x == tree.key:
            return True
        else:
            return search(tree.left, x) or search(tree.right, x)


"""
Exercice 5 : comparer deux arbres
"""


def equal(tree1, tree2):
    if tree1 is None:
        return tree2 is None
    elif tree2 is None:
        return False
    elif tree1.key == tree2.key:
        return equal(tree1.left, tree2.left) and equal(tree1.right, tree2.right)
    else:
        return False


"""
Exercice 6 : verifier un sous-arbre
"""


def is_subtree(tree, subtree):
    if subtree is None:
        return True
    elif tree is None:
        return False
    else:
        if subtree.key == tree.key:
            return equal(subtree, tree)
        else:
            return is_subtree(subtree, tree.left) or is_subtree(
                subtree, tree.right
            )


"""
Exercice 7 : dans le miroir
"""


def __symmetric(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1.key == tree2.key:
        return __symmetric(tree1.left, tree2.right) and __symmetric(
            tree1.right, tree2.left
        )
    else:
        return False


def symmetric(tree):
    if tree is None:
        return True
    else:
        return __symmetric(tree.left, tree.right)


#
#   Binary Search Trees
#

"""
Exercice 1 : detecter un ABR
"""


def __is_bst(tree, inf, sup):
    if tree is None:
        return True
    else:
        return (
            tree.key > inf
            and tree.key <= sup
            and __is_bst(tree.left, inf, tree.key)
            and __is_bst(tree.right, tree.key, sup)
        )


def is_bst(tree):
    return __is_bst(tree, -float("inf"), float("inf"))


"""
Exercice 2 : trouver le minimum (iteratif et recursif)
"""


def min_bst_rec(tree):
    if tree is None:
        return None
    else:
        if tree.left is None:
            return tree.key
        else:
            return min_bst_rec(tree.left)


def min_bst_iter(tree):
    if tree is None:
        return None
    else:
        while tree.left is not None:
            tree = tree.left
        return tree.key


"""
Exercice 2 (bonus) : trouver le maximum (iteratif et recursif)
"""


def max_bst_rec(tree):
    if tree is None:
        return None
    else:
        if tree.right is None:
            return tree.key
        else:
            return max_bst_rec(tree.right)


def max_bst_iter(tree):
    if tree is None:
        return None
    else:
        while tree.right is not None:
            tree = tree.right
        return tree.key


"""
Exercice 3 : recherche dans un BST (iteratif et recursif)
"""


def search_rec(x, tree):
    if tree is None:
        return False
    if tree.key == x:
        return True

    if tree.key < x:
        return search_rec(x, tree.right)

    return search_rec(x, tree.left)


def search_iter(x, tree):
    while tree is not None:
        if tree.key == x:
            return True
        if x <= tree.key:
            tree = tree.left
        else:
            tree = tree.right
    return False


"""
Exercice 4 : inserer un element en feuille dans un BST (iteratif et recursif)
"""


def leaf_insert_rec(tree, key):
    if tree is None:
        return BinTree(key, None, None)

    if key <= tree.key:
        tree.left = leaf_insert_rec(tree.left, key)
    else:
        tree.right = leaf_insert_rec(tree.right, key)

    return tree


def leaf_insert_iter(root, key):
    curr = root
    parent = None

    if root is None:
        return BinTree(key, None, None)

    while curr:
        parent = curr
        if key <= curr.key:
            curr = curr.left
        else:
            curr = curr.right

    if key <= parent.key:
        parent.left = BinTree(key, None, None)
    else:
        parent.right = BinTree(key, None, None)

    return root
