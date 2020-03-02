---
title: Game of Life
date: 2020
author: Tanguy Segarra
---

# Le Jeu de la Vie de John Conway

## Introduction

C'est en 1970 que le mathematicien britannique John Horton Conway invente le
Jeu de la Vie. Il s'agit d'un automate cellulaire, dont l'evolution depend de
son etat initiale.
Ce n'est pas un vrai jeu, vous entrez simplement une configuration de plateau et
vous observez comment elle evolue.

A intervalle de temps regulier, la disposition des cellules va evoluer en
fonction de leur disposition precedente. On parle de generation, comme si on
regardait une population evoluer. Certaines cellules vont mourir, certaines vont
naitre, et cela dependra uniquement de leur nombre de voisins.

On represente le jeu de la vie par une grille (une matrice) de cellules. chacune
d'elle etant soit morte, soit vivante. Chaque cellule interragit avec
ses voisines pour evoluer (rester vivante, mourir, ou naitre).

Chaque cellule possede 8 voisines, sur ses cotes, et en diagonale. Celles
situees sur les bords du plateau en ont evidemment moins.

Alors comment evoluent ces cellules ? Le jeu de la vie, a defaut de ne pas avoir
de joueur, a au moins des regles. Les voici :

1. Une cellule **vivante** avec strictement moins de deux voisines vivantes,
    meurt (a cause de la sous-population);
2. Une cellule **vivante** avec exactement deux ou trois voisines vivantes,
    reste vivante.
3. Une cellule **vivante** avec strictement plus de trois voisines vivantes,
    meurt (a cause de la surpopulation)
4. Une cellue **morte** avec exactement 3 voisines vivantes, devient vivante
    (grace a la reproduction)

## Tester votre programme

Vous avez a votre disposition un dossier `patterns` contenant des exemples de
configurations.  Pour lancer votre programme, vous devrez lui fournir le nombre
de generations pendant lesquelles il doit tourner et le chemin vers la
configuration initiale que vous voulez.

Par exemple:
```
$ ./jeu-de-la-vie.py 130 patterns/gosper-glider-gun
```

lancera votre programme permettra d'observer l'evolution de la configuration
gosper-glider-gun sur 130 generations.

## Explication du code donne

* expliquer le she-bang
* parler des booleens ALIVE/DEAD = TRUE/FALSE
* justifier les import
* expliquer qu'il faut supprimer les pass

## Implementation en Python

### La classe `Cell`

Elle possede deux attributs :
* `alive` : un booleen qui represente si la cellule est vivante ou morte.
* `char` : le caractere ASCII qui represente la cellule dans le terminal.

Elle possede deux methodes :
* `__init__(self, alive)`
* `set(self, status)`

**Exercice 1** : ecrivez la methode `__init__(self, alive)` pour la classe Cell.
Elle doit prendre en parametre le booleen `alive` qui represente l'etat de la
cellule lors de sa creation, et l'assigner a l'attribut de la cellule `alive`.
Elle doit egalement assigner un caractere a l'attribut `char` en fonction de la
valeur de l'attribut `alive`. Par exemple, '0' si la cellule est vivante, '.'
sinon.

**Exercice 2** : ecrivez la methode `set(self, status)` pour la classe Cell.
Elle doit assigner la valeur `status` a l'attribut `alive` de la cellule, et
modifier l'attribut `char` en fonction du nouvel etat de la cellule.

### La classe `Board`

Elle possede 3 attributs :
* `width` : la largeur du plateau
* `height` : la hauteur du plateau
* `grid` : la matrice qui contient toutes les cellules

**Exercice 1** : ecrivez la methode `__init__(self, width, height, path)`

**Exercice 2** : ecrivez la methode `display(self)`

**Exercice 3** : ecrivez la methode `count_neighbours(self, x, y)`

⚠️⚠️⚠️⚠️⚠️
Attention aux cellules qui se trouvent aux bords du plateau, vous aurez des
erreurs `index out of range` si vous essayez de regarder autour et que vous
sortez de la matrice.
⚠️⚠️⚠️⚠️⚠️

**Exercice 4** : ecrivez la methode `set_cell(self, i, j, status)`

**Exercice 5** : ecrivez la methode `next_generation(self)`

⚠️⚠️⚠️⚠️⚠️
La mise a jour du plateau doit se faire **simultanement** sur toutes les
cellules. Pour cela, construisez un nouveau plateau et mettez a jour les etats
des cellules dedans, en fonction de la configuration actuelle du plateau.
⚠️⚠️⚠️⚠️⚠️

## Ameliorations possibles

**Bonus 1** : ajoutez une condition dans la boucle principale afin d'interrompre
le jeu des qu'il n'y a plus de cellules vivantes sur le plateau.
Pour cela, implemente la methode `is_empty(self)` dans la classe Board qui
verifie simplement si toutes les cellules du plateau sont mortes.

**Bonus 2** : generer une grille aleatoirement `seed_life(self, count)` qui
demande par exemple les dimensions voulues a l'utilisateur, le nombre de
cellules vivantes initialement, etc...
