---
title: Graphes
date: 2019
author: Tanguy Segarra
---

TODO Format md

## Introduction aux graphes

La ville de Königsberg (aujourd'hui Kaliningrad) est construite autour de deux
îles situées sur le Pregel et reliées entre elles par un pont. Six autres ponts
relient les rives de la rivière à l'une ou l'autre des deux îles, comme
représentés sur le plan ci-dessus. Le problème consiste à déterminer s'il
existe ou non une promenade dans les rues de Königsberg permettant, à partir
d'un point de départ au choix, de passer une et une seule fois par chaque pont,
et de revenir à son point de départ, étant entendu qu'on ne peut traverser le
Pregel qu'en passant sur les ponts.

(source : Wikipédia)

TODO Refaire un peu cette partie ?

### Qu'est-ce qu'un graphe ? A quoi ça sert ?

Un graphe est une collection de sommets et d'arêtes, possiblement pondérées par
des poids.

On note G = (V, E), avec V la liste des sommets, et E les arêtes (Vertices et
Edges en anglais). C'est cette forme qui sera utilisée la plupart du temps en
entrée de nos fontions.

TODO image graphe basique

Ils peuvent par exemple servir à modéliser des réseaux informatiques, ou comme
on l'a vu plus haut pour résoudre des problèmes pas forcément liés à
l'informatique.

TODO d'autres exemples

Un graphe est dit **orienté** si ses arêtes ne peuvent être parcourues que dans
un sens. L'orientation des arêtes est indiquée par des flèches sur les arêtes.
Inversement, un graphe est dit **non orienté** si on peut parcourir ses arêtes
dans les deux sens.

TODO Figure d'un graphe oriente & poids | Figure d'un graphe non oriente &
poids

TODO Le **degré** d'un sommet est le nombre d'arêtes reliant ce sommet à un
autre sommet. Pour les graphes non orientés, une boucle (arête (a) dans Fig x)
compte deux fois. Pour les graphes orientés, on parle de degré entrant et de
degré sortant. La somme des deux nous donne le degré.

TODO Par exemple, le sommet X dans le graphe G est de degre Y.


### Comment représente-t-on un graphe ?

Il existe trois façons de représenter des graphes :
- les matrices d'incidence
- les matrices d'adjacence
- les listes d'adjacence

Nous ne parlerons pas de la première méthode : les matrices d'incidence, en
effet, par pure habitude, nous allons privilégier les deux méthodes d'après, si
vous voulez en savoir plus, demandez à un organisateur !

#### Les matrices d'adjacence

Une matrice d'adjacence permet de représenter un graphe avec ... une matrice !

Les lignes et les colonnes de la matrice représentent les sommets du graphe.
Les cases de la matrices indiquent s'il existe une arête entre les deux sommets
(le sommet de la colonne et le sommet de la ligne).

TODO Exemple matrice du graphe non orienté

Pour les graphes non orientés, vu que l'on peut se déplacer d'un sommet vers
l'autre et inversement avec une seule arête, on remarque que la matrice est
symétrique selon une diagonale.

La matrice d'un graphe orienté ne sera cependant pas forcément symétrique.

TODO Exemple matrice du graphe orienté

TODO Exemple d'implémentation de matrice d'adjacence en Python

#### Les listes d'adjacence

Une liste d'adjacence permet quant à elle de représenter un graphe à l'aide ...
d'une liste !

Ou plus précisément une liste de listes : pour chaque sommet, on récupère tous
ses sommets adjacents et on les stocke dans l'index de la liste correspondant.

TODO Exemple liste du graphe non orienté

TODO Exemple d'implémentation de liste d'adjacence en Python

#### L'un ou l'autre ?

Alors pourquoi choisir telle ou telle représentation ?

La première raison que l'on a choisi de vous donner est la praticité de l'un
par rapport à l'autre. Avant de lire le prochain paragraphe, posez-vous la
question : avec quoi préférez-vous travailler ? Des listes ? Des matrices ?

Nous préférons personnellement les listes d'adjacence pour représenter les
graphes ; cependant, si vous préférez les matrices d'adjacence, vous pourrez
bien entendu réaliser ce TP avec cet outil !

Maintenant d'un point de vue plus objectif, selon la densité du graphe,
c'est-à-dire le rapport entre le nombre d'arête que votre graphe a et le nombre
d'arête "maximal" de ce graphe. Cette définition est floue, principalement car
elle dépend du contexte dans lequel nous travaillons.

### Comment parcourir un graphe ?

DFS & BFS (rec et iter ??)

Différence d'approche

Peu de différence en code

Utilité des uns & des autres (pourquoi bfs & pas dfs ?)

### Compréhension de liste ??  Ou pas ?

## Testez votre code!

Avec ce sujet est fourni un fichier vous permettant de vérifier que votre code
fonctionne comme il devrait.

Pour que la vérification se passe bien, il faudra
- Respecter les noms de fonctions précisés dans les énoncés suivants
- Lancer les tests avec `./tests-graphs.py <votre-fichier>` dans le terminal


## Pratiquons !

### Exercice : présence dans un graphe

**But** : écrire la fonction `is_in(G, A)` qui renvoie un booléen : `True` si
le sommet `A` est dans le graphe `G`, `False` sinon.

**Exemple** :

Pour le graphe G0 [insert picture here] -> 4, [(0,3),(3,2),(1,2),(3,1)]

``` print(is_in(G, 4)) ```

doit afficher `True`.


### Exercice : nombre de sommets a degre impair

**But** : écrire la fonction `odd_vertices(G)` qui renvoie une liste contenant
les sommets de degre impair.  On considere le graphe G comme non oriente, et
represente a l'aide d'une liste d'adjacence.

Pour rappel, le degré d'un sommet est le nombre d'arêtes incidentes a ce
sommet.

**Exemple** :

Pour le graphe G0 [insert picture here] -> 4, [(0,3),(3,2),(1,2),(3,1)]

``` print(odd_vertices(G)) ```

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

``` print(is_connected(G1)) ```

doit afficher `True`.

Pour le graphe G2 [insert picture here] -> 5,[(0,1),(2,1),(2,0),(4,3)]

``` print(is_connected(G2)) ```

doit afficher `False`.

### Exercice : graphe eulerien

Un graphe connexe est eulérien si et seulement si chacun de ses sommets est
incident à un nombre pair d'arêtes.

**But** : écrire la fonction `is_eulerian(G)` qui renvoie `True` s'il est
possible de parcourir le graphe en partant d'un sommet quelconque et en
empruntant exactement une fois chaque arête pour revenir au sommet de départ,
`False` sinon.

On considere le graphe G comme non oriente, et represente a l'aide d'une liste
d'adjacence.

**Exemple** :

Pour le graphe G0 [insert picture here] -> 4, [(0,3),(3,2),(1,2),(3,1)]

``` print(is_eulerian(G)) ```

doit afficher `True`.


### Graphe pondéré

### Plus court chemin

### Exercices

Redo de certains, mais avec des poids ? Degré d'un sommet ?  Plus
court(s) chemin(s) ofc
