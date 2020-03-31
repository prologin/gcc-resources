---
title: Graphes
date: 2019
author: Tanguy Segarra
---

## Introduction aux graphes

Un peu d'histoire: les 7 ponts de Königsberg

**Comment represente-t-on un graphe ?**

degre
representation des liaisons entre les sommets
    * matrice d'adjacence
    * liste d'adjacence

Un graphe est dit **orienté** si ses arêtes ne peuvent être parcourues que dans
un sens. L'orientation des arêtes est indiquée par des flèches sur les arêtes.
Inversement, un graphe est dit **non oriente** si on peut parcourir ses aretes
dans n'importe quel sens.

Figure d'un graphe oriente | Figure d'un graphe non oriente

Le **degre** d'un sommet est le nombre d'aretes incidentes a ce sommet.
Par exemple, le sommet X dans le graphe G est de degre Y.

Et en Python, ca donne quoi ?

## Testez votre code!

Avec ce sujet est fourni un fichier vous permettant de vérifier que votre code
fonctionne comme il devrait.

Pour que la vérification se passe bien, il faudra
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Lancer les tests avec `./tests-graphs.py <votre-fichier>` dans le terminal


## Pratiquons !

### Exercice : presence dans un graphe

**But** : écrire la fonction `is_in(G)` qui renvoie une liste contenant
les sommets de degre impair.  On considere le graphe G comme non oriente, et
represente a l'aide d'une liste d'adjacence.

Pour rappel, le degre d'un sommet est le nombre d'aretes incidentes a ce sommet.

**Exemple** :

Pour le graphe G0 [insert picture here] -> 4, [(0,3),(3,2),(1,2),(3,1)]

```
print(odd_vertices(G))
```

doit afficher `[0, 3]`.


### Exercice : nombre de sommets a degre impair

**But** : écrire la fonction `odd_vertices(G)` qui renvoie une liste contenant
les sommets de degre impair.  On considere le graphe G comme non oriente, et
represente a l'aide d'une liste d'adjacence.

Pour rappel, le degre d'un sommet est le nombre d'aretes incidentes a ce sommet.

**Exemple** :

Pour le graphe G0 [insert picture here] -> 4, [(0,3),(3,2),(1,2),(3,1)]

```
print(odd_vertices(G))
```

doit afficher `[0, 3]`.

### Exercice : connexite d'un graphe

Un graphe est dit connexe si quels que soient une paire de sommets, il existe
une chaîne reliant le premier sommet au second.

**But** : écrire la fonction `is_connected(G)` qui renvoie `True` si le graphe
est connexe, `False` sinon.

On considere le graphe G comme non oriente, et represente a l'aide d'une liste
d'adjacence.


**Exemple** :

Pour le graphe G1 [insert picture here] -> 4,[(0,1),(2,1),(3,0),(3,1)]

```
print(is_connected(G1))
```

doit afficher `True`.

Pour le graphe G2 [insert picture here] -> 5,[(0,1),(2,1),(2,0),(4,3)]

```
print(is_connected(G2))
```

doit afficher `False`.

### Exercice : graphe eulerien

Un graphe connexe est eulérien si et seulement si chacun de ses sommets est
incident à un nombre pair d'arêtes.

**But** : écrire la fonction `euler(G)` qui renvoie `True` s'il est possible de
parcourir le graphe en partant d'un sommet quelconque et en empruntant
exactement une fois chaque arête pour revenir au sommet de départ, `False` sinon.

On considere le graphe G comme non oriente, et represente a l'aide d'une liste
d'adjacence.

**Exemple** :

Pour le graphe G0 [insert picture here] -> 4, [(0,3),(3,2),(1,2),(3,1)]

```
print(odd_vertices(G))
```

doit afficher `[0, 3]`.
