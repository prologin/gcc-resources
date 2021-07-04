---
title: Arbres
date: 2020
author: Tanguy Segarra
---

Prerequis : poo + listes
Il faut parler de : iteratif/recursif
beaucoup de dessins !
lien entre recherche dichotomique et bst

## Testez votre code!

Avec ce sujet est fourni un fichier vous permettant de vérifier que votre code
fonctionne comme il le devrait.

Pour que la vérification se passe bien, il faudra
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Lancer les tests avec `./tests-trees.py <votre-fichier>` dans le terminal

## Introduction aux Arbres

FIXME
Montrer un exemple d'arbre en python :
avec le None en fils pour leur introduire cette notion

## Pratiquons !

### Exercice 0 : definition de la classe Arbre

Pour manipuler des arbres, il faut pouvoir les representer.

**But** : creer une classe BinTree qui a comme constructeur `__init__(self, key,
left_child, right_child)` et a comme attributs `key`, `left_child`,
`right_child`.

### Exercice 1 : tailler un arbre

On appelle taille d'un arbre le nombre de noeuds qui le compose.

Par exemple :

![](figures/tree1.svg)

Cet arbre a une taille de FIXME

**But** : ecrire la fonction `size(tree)` qui prend un arbre `tree` en
parametre et renvoie sa taille.

### Exercice 2 : prends de la hauteur !

On appelle hauteur d'un arbre la plus grande distance qui separe un noeud de la
racine.

Par exemple :

![](figures/tree1.svg)

Cet arbre a une hauteur de FIXME

**But** : ecrire la fonction `height(tree)` qui prend un arbre `tree` en
parametre et renvoie sa hauteur.

### Exercice 3 : compter les feuilles de l'arbre

Pour rappel, on appelle feuilles de l'arbre les noeuds qui ne possedent aucun
fils.

Par exemple :

![](figures/tree1.svg)

Cet arbre possede FIXME feuilles.

**But** : ecrire la fonction `nb_leaves(tree)` qui prend un arbre `tree` en
parametre et renvoie sa hauteur.

### Exercice 4 : recherche dans un arbre

**But** : ecrire la fonction `search(tree, x)` qui prend un arbre `tree` en
parametre et renvoie `True` s'il possede la valeur `x` parmi ses noeuds,
`False` sinon.

### Exercice 5 : comparer deux arbres

**But** : ecrire la fonction equal(tree1, tree2)` qui prend deux arbres `tree1` et `tree2` en
parametres et renvoie `True` s'ils sont egaux, `False` sinon.

### Exercice 6 : verifier un sous-arbre

Pour rappel, on appelle sous-arbre S d'un arbre A un arbre tel que tous les
noeuds et liens de S sont aussi dans A.

Par exemple :

![](figures/tree1.svg)

![](figures/subtree1.svg)

Ici, FIXME est un subtree de FIXME.

**But** : ecrire la fonction `is_subtree(tree, subtree)` qui prend deux arbres
`tree` et `subtree` en parametres et renvoie `True` si `subtree est un
sous-arbre de `tree`, `False` sinon.

### Exercice 7 : dans le miroir

**But** : ecrire la fonction `symmetric(tree1, tree2)` qui prend deux arbres
`tree1` et `tree2` en parametres et renvoie `True` s'ils sont le symetrique
l'un de l'autre, `False` sinon.

Par exemple :

![](figures/tree1.svg)

![](figures/subtree1.svg)

Ici, FIXME et FIXME sont symetriques.

## Arbres Binaires de Recherche

FIXME

## Pratiquons !

### Exercice 1 : detecter un ABR

**But** : ecrire la fonction `is_bst(tree)` qui prend un arbre `tree` en parametre et renvoie `True` s'il s'agit d'un arbre binaire de recherche, `False` sinon.
l'un de l'autre, `False` sinon.

Par exemple :

![](figures/tree1.svg)

![](figures/subtree1.svg)

Ici, FIXME et FIXME sont symetriques.

### Exercice 2 : trouver le minimum (iteratif et recursif)

**But** : ecrire la fonction `min_bst_rec(tree)` qui prend un arbre `tree` en parametre et renvoie `True` s'il s'agit d'un arbre binaire de recherche, `False` sinon.
l'un de l'autre, `False` sinon.

Par exemple :

![](figures/tree1.svg)

![](figures/subtree1.svg)

Ici, FIXME et FIXME sont symetriques.

### Exercice 2 (bonus) : trouver le maximum (iteratif et recursif)

### Exercice 3 : recherche dans un BST (iteratif et recursif)

### Exercice 4 : inserer un element en feuille dans un BST (iteratif et recursif)
