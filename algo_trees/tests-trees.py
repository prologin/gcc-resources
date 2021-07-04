#!/usr/bin/python3

import sys, importlib


if len(sys.argv) == 1:
    print("Usage: " + sys.argv[0] + " <ton_fichier>")
    sys.exit(2)


tp = sys.argv[1]
if tp[-3:] == ".py":
    tp = tp[:-3]
tp = importlib.import_module(tp)


GREEN = "\033[0;32m"
RED = "\033[0;31m"
NC = "\033[0m"


def ok():
    print(f"[{GREEN} OK {NC}]")


def ko():
    print(f"[{RED} KO {NC}]", end="")


def build_tree(L, i=0):
    if i >= len(L) or L[i] == "#":
        return (None, i + 1)
    else:
        B = tp.BinTree(L[i], None, None)
        i = i + 1
        (B.left, i) = build_tree(L, i)
        (B.right, i) = build_tree(L, i)
        return (B, i)


def load_tree(tree_as_list):
    (tree, i) = build_tree(tree_as_list)
    return tree


def test(f, inp, out):
    inpp = ", ".join(str(x) for x in inp)
    try:
        res = f(*inp)
        if res == out:
            ok()
        else:
            ko()
            print(f" {f.__name__}() = {res} | Attendu : {out}")

    except Exception as e:
        print(e, "\033[0;31m[K0]\033[0m")


def test_attr(obj, attr):
    if not hasattr(obj, attr):
        ko()
        print(f" {type(obj).__name__} n'a pas manque l'attribut '{attr}'")
    else:
        ok()


#
#   Binary Trees
#

EMPTY_TREE = []
ROOT_ONLY = ["R"]
TREE1 = [
    "V",
    "D",
    "I",
    "Q",
    "#",
    "U",
    "#",
    "#",
    "#",
    "S",
    "E",
    "#",
    "#",
    "T",
    "#",
    "#",
    "I",
    "E",
    "#",
    "R",
    "#",
    "#",
    "A",
    "T",
    "#",
    "#",
    "S",
    "#",
    "#",
]
SUBTREE1 = ["S", "E", "#", "#", "T", "#", "#"]
SYMTREE1 = ["S", "E", "#", "#", "E", "#", "#"]
SYMTREE2 = ["S", "E", "#", "T", "#", "#", "E", "T", "#", "#", "#"]
ABR1 = tp.BinTree(
    20,
    tp.BinTree(10, tp.BinTree(5, None, None), tp.BinTree(15, None, None)),
    tp.BinTree(30, tp.BinTree(25, None, None), None),
)
ABR1_7 = tp.BinTree(
    20,
    tp.BinTree(
        10,
        tp.BinTree(5, None, tp.BinTree(7, None, None)),
        tp.BinTree(15, None, None),
    ),
    tp.BinTree(30, tp.BinTree(25, None, None), None),
)
ABR1_7_12 = tp.BinTree(
    20,
    tp.BinTree(
        10,
        tp.BinTree(5, None, tp.BinTree(7, None, None)),
        tp.BinTree(15, tp.BinTree(12, None, None), None),
    ),
    tp.BinTree(30, tp.BinTree(25, None, None), None),
)
ABR1_7_12_13 = tp.BinTree(
    20,
    tp.BinTree(
        10,
        tp.BinTree(5, None, tp.BinTree(7, None, None)),
        tp.BinTree(15, tp.BinTree(12, None, tp.BinTree(13, None, None)), None),
    ),
    tp.BinTree(30, tp.BinTree(25, None, None), None),
)
ABR1_7_12_13_0 = tp.BinTree(
    20,
    tp.BinTree(
        10,
        tp.BinTree(5, tp.BinTree(0, None, None), tp.BinTree(7, None, None)),
        tp.BinTree(15, tp.BinTree(12, None, tp.BinTree(13, None, None)), None),
    ),
    tp.BinTree(30, tp.BinTree(25, None, None), None),
)
PASUNABR = tp.BinTree(
    2,
    tp.BinTree(10, tp.BinTree(5, None, None), tp.BinTree(15, None, None)),
    tp.BinTree(3, tp.BinTree(25, None, None), None),
)
ABR3 = tp.BinTree(
    2,
    tp.BinTree(1, tp.BinTree(0.5, None, None), tp.BinTree(1.5, None, None)),
    tp.BinTree(3, tp.BinTree(2.5, None, None), None),
)


bintree = load_tree(TREE1)
subtree = load_tree(SUBTREE1)
symtree1 = load_tree(SYMTREE1)
symtree2 = load_tree(SYMTREE2)
empty_tree = load_tree(EMPTY_TREE)
root_only = load_tree(ROOT_ONLY)


print("~~ ARBRES BINAIRES ~~\n")


# Exercice 0 : classe BinTree
print("Exercice 0 : la classe BinTree")
test_attr(bintree, "key")
test_attr(bintree, "left")
test_attr(bintree, "right")

print()


# Exercice 1 : tailler un arbre
print("Exercice 1 : tailler un arbre")
try:
    test(tp.size, [bintree], 14)
    test(tp.size, [empty_tree], 0)
    test(tp.size, [root_only], 1)

except Exception as e:
    print(e)

print()


# Exercice 2 : prends de la hauteur !
print("Exercice 2 : prends de la hauteur")
try:
    test(tp.height, [bintree], 4)
    test(tp.height, [empty_tree], -1)
    test(tp.height, [root_only], 0)

except Exception as e:
    print(e)

print()


# Exercice 3 : compter les feuilles de l'arbre !
print("Exercice 3 : compter les feuilles de l'arbre")
try:
    test(tp.nb_leaves, [bintree], 6)
    test(tp.nb_leaves, [empty_tree], 0)
    test(tp.nb_leaves, [root_only], 1)

except Exception as e:
    print(e)

print()


# Exercice 4 : recherche dans un arbre
print("Exercice 4 : recherche dans un arbre")
try:
    test(tp.search, [bintree, "V"], True)
    test(tp.search, [bintree, "X"], False)
    test(tp.search, [empty_tree, "V"], False)
    test(tp.search, [root_only, "R"], True)
    test(tp.search, [root_only, "X"], False)

except Exception as e:
    print(e)

print()


# Exercice 5 : sont-ils les memes arbres ?
print("Exercice 5 : sont-ils les memes arbres ?")
try:
    test(tp.equal, [bintree, bintree], True)
    test(tp.equal, [empty_tree, empty_tree], True)
    test(tp.equal, [empty_tree, bintree], False)
    test(tp.equal, [root_only, bintree], False)

except Exception as e:
    print(e)

print()


# Exercice 6 : verifier un sous-arbre
print("Exercice 6 : verifier un sous-arbre")
try:
    test(tp.is_subtree, [bintree, subtree], True)
    test(tp.is_subtree, [bintree, empty_tree], True)
    test(tp.is_subtree, [bintree, None], True)
    test(tp.is_subtree, [empty_tree, bintree], False)
    test(tp.is_subtree, [bintree, bintree], True)

except Exception as e:
    print(e)

print()


# Exercice 7 : dans le miroir
print("Exercice 7 : dans le miroir")
try:
    test(tp.symmetric, [bintree], False)
    test(tp.symmetric, [symtree1], True)
    test(tp.symmetric, [symtree2], True)
    test(tp.symmetric, [empty_tree], True)

except Exception as e:
    print(e)

print()


#
#   Binary Search Trees
#

print("~~ ARBRES BINAIRES DE RECHERCHE ~~\n")


# Exercice 1 : detecter un ABR
print("Exercice 1 : detecter un ABR")
try:
    test(tp.is_bst, [PASUNABR], False)
    test(tp.is_bst, [ABR1], True)
    test(tp.is_bst, [empty_tree], True)

except Exception as e:
    print(e)

print()


# Exercice 2 : trouver le minimum - recursif
print("Exercice 2 : trouver le minimum - recursif")
try:
    test(tp.min_bst_rec, [ABR1], 5)
    test(tp.min_bst_rec, [ABR3], 0.5)
    test(tp.min_bst_rec, [empty_tree], None)

except Exception as e:
    print(e)

print()


# Exercice 2 : trouver le minimum - iteratif
print("Exercice 2 : trouver le minimum - iteratif")
try:
    test(tp.min_bst_iter, [ABR1], 5)
    test(tp.min_bst_iter, [ABR3], 0.5)
    test(tp.min_bst_iter, [empty_tree], None)

except Exception as e:
    print(e)

print()

# Exercice 2 (bonus) : trouver le maximum - recursif
print("Exercice 2 : trouver le minimum - recursif")
try:
    test(tp.max_bst_rec, [ABR1], 30)
    test(tp.max_bst_rec, [ABR3], 3)
    test(tp.max_bst_rec, [empty_tree], None)

except Exception as e:
    print(e)

print()


# Exercice 2 (bonus) : trouver le minimum - iteratif
print("Exercice 2 : trouver le maximum - iteratif")
try:
    test(tp.max_bst_iter, [ABR1], 30)
    test(tp.max_bst_iter, [ABR3], 3)
    test(tp.max_bst_iter, [empty_tree], None)

except Exception as e:
    print(e)

print()


# Exercice 3 : recherche dans un ABR - recursif
print("Exercice 3 : recherche dans un ABR - recursif")
try:
    test(tp.search_rec, [5, ABR1], True)
    test(tp.search_rec, [30, ABR1], True)
    test(tp.search_rec, [3, ABR1], False)
    test(tp.search_rec, [42, ABR1], False)
    test(tp.search_rec, [42, empty_tree], False)

except Exception as e:
    print(e)

print()


# Exercice 3 : recherche dans un ABR - iteratif
print("Exercice 3 : recherche dans un ABR - iteratif")
try:
    test(tp.search_iter, [5, ABR1], True)
    test(tp.search_iter, [30, ABR1], True)
    test(tp.search_iter, [3, ABR1], False)
    test(tp.search_iter, [42, ABR1], False)
    test(tp.search_iter, [42, empty_tree], False)

except Exception as e:
    print(e)

print()


print("Exercice 4 : inserer un element en feuille dans un ABR - recursif")
assert tp.equal(ABR1_7, tp.leaf_insert_rec(ABR1, 7)), ko()
ok()
assert tp.equal(ABR1_7_12, tp.leaf_insert_rec(ABR1, 12)), ko()
ok()

print()

print("Exercice 4 : inserer un element en feuille dans un ABR - iteratif")
assert tp.equal(ABR1_7_12_13, tp.leaf_insert_iter(ABR1, 13)), ko()
ok()
assert tp.equal(ABR1_7_12_13_0, tp.leaf_insert_iter(ABR1, 0)), ko()
ok()
