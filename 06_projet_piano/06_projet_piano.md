---
title: Un piano avec `pygame`
date: 2020
---

# Un piano avec `pygame`

Un des instruments les plus utilisés dans les livres de théorie de la musique
est le *piano*.  Une des raisons de son utilisation pour apprendre la musique
est que le piano est très visuel. En effet, un piano n'est rien de plus qu'une
répétition d'une suite de 12 touches, 7 blanches entremêlées de 5 noires, et
permet donc voir les _cycles_ dans les suites de notes et mieux comprendre le
concept de _gammes_.

Le but de ce sujet est de vous aider à obtenir, à l'aide de `pygame`, un
clavier visuel et sonore afin de pouvoir s'amuser en faisant de la musique.

Si vous suivez bien les instructions dans l'énoncé vous devriez obtenir un
résultat similaire à cette image:

TODO: insérer une image du clavier.

## Théorie de la musique

TODO: expliquer des bêtises sur la musique:

* fréquence
* note
* touche blanche
* touche noire
* octave (cycles)

## Rappels

Afin de nous préparer pour le projet d'aujourd'hui, nous allons revoir certains
éléments qui ont été vu dans les sujets précédents.

### Les types simples

Pour pouvoir mettre en place notre piano, nous allons utiliser trois différents
types de données:

* les nombres entiers comme `42`, `0` ou `-1`.
* les chaînes de caractères comme `"ordinateur"` ou `"Girls can code!"`.
* les booléens: `True` ou `False`.

### Les variables

Afin de pouvoir manipuler ces données, il nous faut leur donner un nom. On peut
donc assigner ces données à des variables.

Voici quelques exemples d'assignation de variable:

```python

# Des exemples avec des entiers
mon_entier = 42
quarante_trois = mon_entier + 1

# Des exemples avec des chaînes de caractères
premiere_moitie = "J'aime le"
deuxieme_moitie = " Python!"
mon_message = premiere_moitie + deuxieme_moitie

# Des exemples avec des booléens
ceci_est_vrai = True
ceci_est_faux = False
ceci_est_vrai2 = (42 == 42)
ceci_est_faux2 = (mon_entier > quarante_trois)

```

### Les conditions

Au cours de notre programme nous allons devoir effectuer ou non des actions en
fonction d'une condition qui pourra être vraie ou fausse. Par exemple nous
aurons sûrement envie de pouvoir jouer une note musicale si une touche est
appuyée sur le clavier. Pour cela nous pouvons utiliser les mots-clés
suivants: `if`, `elif` et `else`.

Prenez l'exemple suivant:

\newpage

```python

if condition1:
    corps1
elif condition2:
    corps2
elif condition3:
    corps3
else:
    corps4

```

Le corps1 sera exécuté si condition1 est vraie.

Le corps2 sera exécuté si condition1 est fausse et condition2 est vraie.

Le corps3 sera exécuté si condition1 est fausse, condition2 est fausse et
condition3 est vraie.

Le corps4 sera exécuté si condition1 est fausse, condition2 est fausse et
condition3 est fausse.

### Les boucles

Parfois, il devient nécessaire de pouvoir exécuter du code plusieurs fois
d'affilée pour réussir à atteindre notre but. On pourrait imaginer une
situation où on voudrait le décompte d'un nombre en particulier. Pour ce faire,
il faudrait avoir une variable qu'on initialise en lui donnant une valeur
initiale de 0 avant de la faire augmenter par palier de `1` jusqu'au nombre
voulu en affichant le résultat à chaque fois.

La boucle `while` permet de représenter la situation. En supposant qu'on
veuille compter jusqu'à 42 on pourrait écrire le code suivant:

```python

mon_compteur = 0
while compteur < 43:
    print(mon_compteur) # affiche la valeur actuelle du compteur
    mon_compteur = mon_compteur + 1

```

Si on connaît déjà le nombre de fois qu'on veut exécuter le code dans le corps
de la boucle, on peut aussi utiliser une boucle `for` comme suit:

```python

for mon_compteur in range(43):
    print(mon_compteur)

```

Dans les deux cas, en rentrant dans le corps de la boucle la variable
`mon_compteur` aura pour valeurs successives 0, 1, 2, 3 ... 41, 42.

### Les fonctions

De la même manière qu'on peut associer un nom à une donnée en utilisant une
variable, il est possible d'associer un nom à des petits bouts de code: des
fonctions.

Voici un exemple de définition de fonction simple:

```python

mon_entier = 21

# La définition de la fonction
def doubler_mon_entier():
    mon_entier = mon_entier * 2

# Un appel de la fonction
doubler_mon_entier()

# mon_entier est maintenant égal à 42

# Un deuxième appel de la fonction
doubler_mon_entier()

# mon_entier est maintenant égal à 84

```

Les fonctions peuvent aussi prendre des paramètres comme par exemple:

```python

# La définition de la fonction qui prend des paramètres
def regarder_si_plus_de_42(entier):
    if entier > 42:
        print('Plus grand que 42 !')
    elif entier == 42:
        print('Egal à 42 !')
    else:
        print('Plus petit que 42 !')

# Trois appels de cette fonction

regarder_si_plus_de_42(100)
# Affiche 'Plus grand que 42 !'

regarder_si_plus_de_42(42)
# Affiche 'Egal à 42 !'

regarder_si_plus_de_42(23)
# Affiche 'Plus petit que 42 !'

```

### Les imports

Lorsque l'on veut faire appel à des fonctions, méthodes ou classes d'autres bibliothèques (ou module), on voudrait ne pas avoir à écrire nous même la fonction, ou à la copier-coller... C'est à ça que servent les import !

```
import math
```

Dit à notre programme Python de charger la bibliothèque math, et nous donne accès aux fonctions qui ont été écrites dans cette bibliothèque.

On peut renommer le module _math_ en `m` en faisant :

```
import math as m
```

On peut le renommer autrement en changeant ce qu'il y a après `as`.

Cependant, ces deux méthodes d'import sont généralement déconseillées si vous
n'avez besoin que d'une fonction : vous ne voulez pas forcément importer toute
la bibliothèque ! En effet, imaginons que l'on ait seulement besoin de la
fonction sqrt(x), qui renvoie la racine carrée de x, et qui provient de la
bibliothèque _math_, vous n'avez pas envie que toutes les autres fonctions
soient chargées, mais seulement la (ou les) fonction dont vous avez besoin !

Pour ce faire, on écrit :

```
from math import sqrt
```

Une dernière chose à savoir, et vous l'avez peut-être déjà vu dans certains codes en Python :

```
if __name__ == "__main__":
    # le point d'entrée de notre programme
```

Cette condition permet de séparer les appels de notre programme "voulus", des imports de notre programme : lorsqu'on lance notre code avec `python <fichier.py>`, on veut que notre code soit executé, mais lorsqu'on importe notre code (et donc nos fonctions, classes, etc.), on ne veut pas que le code soit executé avant que le développeur appelle explicitement la fonction de notre code.

C'est pour cela qu'au lieu d'avoir :

```
class Test:
    def __init__(self, ...):
        # des choses
    
    def methode(self, ...):
        # des choses

def fonction(params):
    # des choses

def fonction_que_lon_veut_lancer(args):
    # des choses

fonction_que_lon_veut_lancer(params)
```

On préfère avoir cette condition autour de `fonction_que_lon_veut_lancer` :

```
if __name__ == "__main__":
    fonction_que_lon_veut_lancer(params)
```

En pratique, et dans nos TP, cela ne fait aucune différence, mais c'est une bonne chose à savoir, et une bonne habitude à prendre !

## Nouvelles notions

On va avoir besoin de plus que ces notions là.

### `pygame`

Explication rapide du setup MIDI et la gestion de la fenêtre.

### Les classes


Note : Si vous avez déjà fait le TP sur les objets, le chapitre qui suit ne sera qu'un rappel pour vous !

Une classe, en Python, est un moyen de créer un modèle pour des données. Elle nous permet de regrouper des données ensemble, en leur donnant un nom.

Disons que nous voulons faire une liste des personnes de notre classe. On veut par exemple trier nos camarades selon leur âge. Avec une liste, c'est très simple :

```
age = [16, 15, 14, 16, 17, 15]
age.sort() # on trie la liste
print(age)
```

Nous donnera :

```
[14, 15, 15, 16, 16, 17]
```

Cependant, on remarque que nous n'avons aucun moyen d'identifier une personne en particulier ! Il serait possible d'utiliser des variables et des listes pour chacun.e de nos camarades, mais on se rend vite compte que c'est très long, et pas vraiment intéressant !

C'est là où les classes rentrent en jeu : elles permettent de "classer" des données, de leur donner un type particulier, que l'on aura imaginé pour un problème donné.

On veut donc avoir l'âge de la personne **et** son prénom (pour pouvoir la différencier des autres !).

En Python ça donne :

```
class Camarade:
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age
```

Expliquons un peu ce code :

On déclare une nouvelle classe que l'on appelle "Camarade", c'est ce nom que l'on utilisera après pour faire appel à notre nouvelle classe. (**ligne 1**)

Pour pouvoir initialiser un nouvel objet de la classe _Camarade_ (on parle aussi d'instancier la classe _Camarade_), on utilise une fonction spéciale en Python : _\_\_init\_\__. On appelle les fonctions d'une classe **méthodes**. La méthode _\_\_init\_\__ est un constructeur : elle nous permet de construire, avec des données de base, un type (ou modèle) plus complexe. Ici, avec le prenom et l'âge de l'un.e de nos camarades, on va créer un **objet** _Camarade_. (**ligne 2**)

Les **lignes 3 et 4** permettent d'affecter les arguments du constructeur _prenom_ et _age_ aux variables internes de l'objet _Camarade_ que l'on est en train de créer. Ces variables internes sont appelées **attributs** d'une classe.

L'utilisation du mot clef _self_ permet de savoir que l'on parle de l'object courant d'une classe.

Plus précisement, lorsque l'on écrit :

```
self.prenom = prenom
self.age = age
```

On explicite au programme Python que l'attribut _prenom_ prend la valeur de l'argument _prenom_ et que l'attribut _age_ prend la valeur de l'argument _age_.

Avec tout ça, on peut maintenant créer un objet _Camarade_ comme suit :

```
Tanguy = Camarade("Tanguy", 20)
```

On aimerait pouvoir faire :

```
print(Tanguy)
```

Malheureusement, cela n'a pas le résultat que l'on pourrait attendre ! Et c'est normal ! Une fois executé, le programme va simplement nous dire que la variable _Tanguy_ est un objet de la classe _Camarade_.

Il nous faut donc une nouvelle méthode pour la classe _Camarade_ pour nous afficher les informations d'un objet _Camarade_. Reprennons notre code et ajoutons une méthode informations(self) qui affiche les informations d'un _Camarade_.

```
class Camarade:
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age
    
    def informations(self):
        print("Je suis " + self.prenom + " et j'ai " + str(self.age) + " ans.")
```

Note : str(self.age) transforme l'age (un entier) en une chaîne de caractères.

Comme les types usuels (c'est-à-dire **int**, **str**, etc.), on peut faire des listes de _Camarade_.

```
Tanguy = Camarade("Tanguy", 20)
Garance = Camarade("Garance", 21)

liste_camarades = [Tanguy, Garance]
```

Ensuite, on peut itérer sur chacun des éléments de la liste comme d'habitude :

```
for camarade in liste_camarades:
    camarade.informations()
```

Et voilà ! Vous savez désormais créer vos propres classes et leur ajouter des attributs et méthodes, à vous de jouer maintenant !

Exercice 1 :

En utilisant la classe Camarade vue au dessus, ajouter un attribut nom, qui correspond au nom de famille de la personne. Mettre à jour la méthode informations(self) pour afficher le nom de famille.


Exercice 2 :

En utilisant la classe Camarade vue au dessus, ajouter une méthode est_plus_grand_que(self, other) qui affiche un texte en fonction de si le camarade est plus âgé que l'autre camarade.

Par exemple, en prenant Tanguy et Garance, déclarés plus haut, on a :

```
Tanguy.est_plus_grand_que(Garance)
# doit être affiché : "Tanguy est plus petit.e que Garance"
Garance.est_plus_grand_que(Tanguy)
# doit être affiché : "Garance est plus grand.e que Tanguy"
Tanguy.est_plus_grand_que(Tanguy)
# doit être affiché : "Tanguy a le même âge que Tanguy"
```

Exercice 3 :

En utilisant la classe Camarade vue au dessus, écrire une méthode tri_camarades(liste) permettant de trier une liste de Camarades en fonction de leur âge (croissant). Afin de pouvoir afficher des listes, écrire une méthode afficher_liste(liste) qui affiche le prenom des camarades dans la liste.

```
Tanguy = Camarade("Tanguy", 20)
Garance = Camarade("Garance", 21)
Maya = Camarade("Maya", 20)

liste_camarades = [Tanguy, Garance, Maya]

afficher_liste(liste_camarades)
# doit être affiché : ["Tanguy", "Garance", "Maya"]
tri_camarades(liste_camarades)
afficher_liste(liste_camarades)
# doit être affiché : ["Tanguy", "Maya", "Garance"]
```

Note : la solution la plus simple serait d'utiliser la méthode spéciale _\_\_lt\_\_(self, other)_ qui existe dans Python, et qui vous permettra d'utiliser la méthode sort() ! Mais libre à vous de nous supprendre avec un autre algorithme de tri ! :)

### Les dictionnaires

Explications et petits exos/fonctions auxiliaires à écrire sur les dictionnaires.

## Utiliser vos connaissances

Nous pouvons enfin commencer à travailler sur notre piano. Comme pour beaucoup
de programmes, notre code va être divisé en deux grosses parties:
l'_initialisation_, où on va préparer tout ce dont on a besoin dans notre
programme (ouvrir une fenêtre, dessiner le piano initial, préparer la sortie
pour le son...), et le _corps_, où on va exécuter le même chose en boucle.

### La structure globale du programme

Abordons donc ces deux parties : l'_initialisation_ puis le _corps_.

#### L'_initialisation_

##### Quelques variables utiles:

Lors de l'_initialisation_, nous allons préparer tout pour que notre piano
puisse afficher les touches et jouer du son.

Avant tout, nous allons avoir besoin de quelques variables pour notre piano:

* 5 couleurs pour l'affichage
* le nombre de notes contenues dans un octave (nombre de touches avant que le
  clavier ne se répète)
* l'octave dans lequel on veut que les sons soient jouées (plus ou moins grave,
  je vous conseille 4)
* le volume avec lequel on veut jouer (entre `0` et `127`)

Les couleurs dans `pygame` sont représentées par des *tuples* de trois valeurs
entre `0` et `255` qui correspondent à l'intensité en rouge, vert et bleu.

Par exemple, la couleur noire correspond à `(0, 0, 0)` et le blanc à `(255,
255, 255)`.

On pourrait donc initialiser nos variables comme suit:

```python

# La couleur du fond
couleur_gris  = (127, 127, 127)

# La couleur des touches blanches
couleur_blanc = (255, 255, 255)

# La couleur des touches noires
couleur_noir = (0, 0, 0)

# La couleur des touches blanches enfoncées
couleur_rouge = (255, 0, 0)

# La couleur des touches noires enfoncées
couleur_bleu = (0, 0, 255)

# Le nombre de notes
nombre_de_notes = 12

# L'octave dans lequel on veut jouer
octave = 4

# Le volume
volume = 127

```

##### Initialiser `pygame`:

Ensuite, pour pouvoir utiliser `pygame`, il faut importer les deux parties
dont on va avoir besoin:

```python

import pygame.midi
import pygame.display

```

Pour initialiser ces deux systèmes (affichage et son), `pygame` fournit deux
fonctions qu'on peut appeler au tout début de notre programme comme suit:

```python

# Pour initialiser le son
pygame.midi.init()

# Pour initialiser l'affichage
pygame.display.init()

```

##### Un dictionnaire pour nos touches:

Afin de pouvoir stocker et mettre à jour l'état de notre clavier, nous allons
utiliser un dictionnaire.

Lorsqu'on va demander à `pygame` quelles touches sont enfoncées, il va nous
répondre en appelant les touches par les noms utilisés par `pygame`.

Il semble donc logique d'utiliser ces noms comme _clés_ pour notre
dictionnaire.

En ce qui concerne les _valeurs_ associées à ces _clés_, nous allons vouloir
stocker plusieurs informations:

* le numéro qui correspond à la note (pour pouvoir jouer le son correspondant)
* un booléen nous indiquant si la touche est noire ou blanche
* un booléen nous indiquant si la touche est enfoncée

Afin de pouvoir stocker toutes ces informations dans le dictionnaire, nous
allons utiliser un _tuple_ pour valeur dans le dictionnaire.

L'initialisation de nos touches de piano pourrait ressembler à ceci pour un
clavier AZERTY:

```python

etat_des_touches = {
        pygame.K_q: (12, False, False),  # C0       ( Do  )
        pygame.K_z: (13, True,  False),  # C#/Db0   ( Do# )
        pygame.K_s: (14, False, False),  # D0       ( Ré  )
        pygame.K_e: (15, True, False),   # D#/Eb0   ( Ré# )
        pygame.K_d: (16, False,  False), # E0       ( Mi  )
        pygame.K_f: (17, False, False),  # F0       ( Fa  )
        pygame.K_t: (18, True,  False),  # F#/Gb0   ( Fa# )
        pygame.K_g: (19, False, False),  # G0       ( Sol )
        pygame.K_y: (20, True, False),   # G#/Ab0   ( Sol#)
        pygame.K_h: (21, False,  False), # A0       ( La  )
        pygame.K_u: (22, True, False),   # A#/Bb0   ( La# )
        pygame.K_j: (23, False,  False), # B0       ( Si  )
}

```

#### Le corps de notre programme

Une fois l'_initialisation_ finie, nous allons rentrer dans le _corps_ de notre
prgramme.

Ce _corps_ va prendre la forme d'une boucle qui va tourner tant que notre
programme est en route.

Si l'on suppose dans un premier temps que notre clavier ne va jamais s'arrêter
et que nous sommes donc dans une boucle infinie, nous pouvons décrire le
contenu du _corps_ comme suit:

\newpage

```

pour toujours:
    pour chaque évènement dans les évènements récupérés par pygame:
        si c'est un appui de touche:
            traiter la touche enfoncee
        sinon si c'est un lâché de touche:
            traiter la touche lâchée
    redessiner l'écran

```

#### Afficher notre clavier

Dans la boucle décrite dans la section précédente, nous redessinons la fenêtre
correspondant de notre programme à chaque tour.

Nous allons donc devoir écrire une fonction qui prend en paramètre une fenêtre
`pygame` et qui dessine notre clavier dedans à partir de l'état des touches
décrit dans le dictionnaire `etat_des_touches`.

Afin de dessiner notre clavier, nous allons avoir besoin dessiner des
rectangles pour representer les touches.

En réalité, nous allons avoir besoin de dessiner deux types de rectangles,
décalés sur notre clavier: un type de rectangle pour les touches blanches et un
type de rectangle pour les touches noires.

#### Que la musique soit

Comme nous l'avons vu précedemment, qu'il s'agisse d'une touche enfoncée ou
relevée, `pygame` va nous dire l'état des touches dans l'évènement
qu'il reçoit.

De plus `pygame` nous fournit deux fonctions utiles pour gérer le son:

* `note_on(note, volume)` pour allumer une note
* `note_off(note)` pour eteindre une note

Toutes les fonctions que nous allons écrire qui concernent la lecture ou
l'arrêt d'une note vont donc prendre un paramètre la touche concernée et en
faire quelque chose.

Nous allons avoir besoin de deux fonctions: `allumer_touche` et
`eteindre_touche`.

##### Exercice

Ecrivez une fonction `allumer_touche` qui prend en paramètre une touche et
lance le son correspondant à cette touche en mettant à jour l'état de la touche
en question dans notre dictionnaire `etat_des_touches`.

Ecrivez une fonction `eteindre_touche` qui prend en paramètre une touche et
arrête le son correspondant à cette touche en mettant à jour l'état de la
touche en question dans notre dictionnaire `etat_des_touches`.
