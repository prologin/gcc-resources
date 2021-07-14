# **La machine Enigma**

>Prérequis : maîtrise basique des classes et de l'opérateur modulo

## **Culture générale**

Tu en as peut-être déjà entendu parler, Enigma est une machine de cryptologie mise au point et utilisée par les allemands pendant la seconde guerre mondiale. Son fonctionnement est déchiffré par le mathématicien Alan Turing, qui est aujourd'hui considéré comme le père de l'informatique moderne.

## **Mais comment fontionne Enigma ?**

### 1. Les rotors

La machine Enigma est composée de 3 parties mobiles appelées "rotors" (visibles sur la photo ci-dessous).
Ces rotors associent une lettre de l'alphabet à une autre. Les trois rotors sont connectés les uns aux autres. Imaginons que l'on donne un **A** au premier rotor, celui-ci pourrait par exemple le transformer en **F**. Le second rotor transforme le **F** en **O** et le troisième transforme le **O** en **E**. *Note ici que les rotors n'appliquent pas un chiffre de César, si **A** devient **F** avec le premier rotor, cela ne veut pas dire que **B** deviendra **G**.*

![Machine Enigma](imgs/enigma.jpeg "Une machine Enigma")

En code, on peut représenter un rotor par une chaîne de 26 caractères.

| Alphabet | ABCDEFGHIJKLMNOPQRSTUVWXYZ |
|---|---|
| Rotor 1 | **EKMFLGDQVZNTOWYHXUSPAIBRCJ** |

>Ici, on peut comprendre que le rotor 1 donnera **E** en sortie pour un **A** en entrée, un **K** pour un **B**, etc... (voir le schéma suivant)

Dernière chose, afin de changer l'état de la machine et de rendre plus complexe le déchiffrement, les rotors peuvent tourner d'un 26ième de tour. Quand cela se produit, les lettres transformées par le rotor changent. Si l'on tourne d'un cran le rotor 1 défini au dessus, le fil dans le rotor qui reliait **A** à **E** reliera désormais **B** à **F**. De la même manière, le fil qui reliait **B** à **K** reliera désormais **C** à **L**, etc...

Puisque cela serait trop simple de tourner les 3 rotors à chaque fois, les cryptologues allemands ont mis au point le système suivant : Pour chaque lettre tapée, le rotor 1 tourne d'un cran. Le rotor 2 tourne lui d'un cran quand le rotor 1 a fait un tour complet (c'est-à-dire toutes les 26 lettres tapées), et le rotor 3 tourne d'un cran à chaque tour complet du rotor 2 (toutes les 676 lettres tapées).

### 2. Le réflecteur

Après avoir fait passer la lettre dans les 3 rotors, on la passe dans une pièce appelée le *réflecteur*. Le réflecteur est une partie similaire à un rotor, car il associe une lettre à une autre, mais reste fixe sans tourner. Enfin, on fini par renvoyer la lettre dans les rotors en sens inverse, et le tour est joué !

### 3. Le tableau de permutations

Comme si cela n'était pas déjà assez compliqué, on rajoute une couche avec le **tableau de permutations**. Le fonctionnement de celui-ci est très simple. Il s'agit simplement de brancher des lettres 2 par 2 pour échanger leur place (on peut échanger comme cela jusqu'à 10 paires de lettres). On branche ce tableau avant le système de rotor. Par exemple, si l'on échange les lettres **A** et **O**, alors chaque **A** tapé par l'opérateur de la machine deviendra un **O** pour le système des rotors, et chaque **A** "renvoyé" par ce dernier sera un **O** pour l'opérateur (et vice-versa, le **O** devient un **A**).

Schéma de fonctionnement d'Enigma

!["schéma fonctionnement"](imgs/enigma_scheme.jpg "Schéma de fonctionnement")

>Si ces explications manquent de clarté, voici [un site très pratique pour visualiser le chemin d'une lettre dans le système](https://observablehq.com/@tmcw/enigma-machine)

### 4. Et pour décoder un message ?

Tu viens d'apprendre le fonctionnement général de la machine Enigma, mais une question persiste : Avec un système aussi complexe, comment fait-on pour décoder un message crypté avec une machine Enigma ? La réponse est sûrement plus simple qu'il n'y paraît : Il suffit de taper le message chiffré sur une machine Enigma qui a les mêmes paramètres initiaux que pour encoder le message ! En effet, prenons le message "GirlsCanCode" et imaginons que tous les rotors soient sur le cran 0 au début du message. Taper **G** sur la machine donnera une lettre différente, peut-être un **V**. Mais de la même manière, si l'on avait tapé **V**, on aurait obtenu **G**, car le chemin de la lettre dans la machine est le même, seulement il est parcouru à l'envers.

## **Exercices**

À ton tour de créer ton propre programme Enigma !

> Afin d'implémenter notre propre machine Enigma, nous utiliserons une classe qui nous sera utile pour sauvegarder l'état actuel des rotors.

Voici le squelette du code:

```py
class Enigma:
    def __init__(self, r1, r2, r3, ref):
        """
        Initialise la machine avec les rotors et le réflecteur donnés
        Appelé par Enigma(...)
        r1 : rotor1
        r2 : rotor2
        r3 : rotor3
        ref : reflecteur
        """
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.ref = ref
        
        # on initialise le décalage des rotors à 0
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
    
    def reset_rotors(self):
        # on réinitialise le décalage des rotors à 0
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
    
    def encode_letter(self, letter):
        pass # À toi de jouer !

    
    def encode_message(self, msg):
        pass # À toi de jouer !

# Exemples

# on déclare notre variable Enigma (avec les rotors définis ci-dessous)
# état initial: tous les décalages à 0
>>> en = Enigma(rotor_I, rotor_II, rotor_III, reflector_A)

>>> en.encode('A')
'N' 
# Etat interne des rotors après opération: x1 = 1, x2 = 0, x3 = 0
```

Voici également 2 simples fonctions permettant de trouver le nombre d'une lettre dans l'alphabet (en partant de `0`), et vice-versa:

```py
def letter_to_number(letter):
    """
    Donne la position d'une lettre dans l'alphabet
    """
    letter = letter.upper() # on transforme la lettre en majuscule
    return ord(letter) - ord('A') 

def number_to_letter(number):
    """
    Donne la lettre majuscule correspondante au nombre donné
    """
    return chr(number + ord('A'))

# Examples
>>> letter_to_number('A')
0
>>> letter_to_number('z')
25


>>> number_to_letter(0)
A
>>> number_to_letter(23)
X
```

Enfin, voici des rotors et réflecteurs qui ont réellement été utilisés pendant la seconde guerre mondiale:

```py
rotor_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

reflector_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
reflector_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
```

---

### **Partie 1 : encode_letter()**

Dans cette méthode de la classe Enigma, tu dois crypter la lettre donnée en paramètre.

>Entrée(s):

- letter: la lettre à chiffrer

>Sortie:

- La lettre chiffrée correspondante

**ATTENTION**: après avoir trouvé la lettre, il ne faut pas oublier de **modifier la position des rotors**.

---

### **Partie 2 : encode_message()**

Dans cette méthode, il te faut encoder tout un message avec le programme Enigma !

>Entrée(s):

- msg: le message à chiffrer

>Sortie: Le message chiffré

- N'oublie pas que tu peux utiliser la méthode `encode_letter()` dans `encode_message()`.
- Attention aux caractères spéciaux dans ton message, les chiffres, espaces et caractères de ponctuation ne peuvent pas être chiffrés par Enigma.

Une fois implémentée, tu peux tester ton code de la manière suivante:

```py
>>> msg = 'HELLO WORLD'
>>> en.reset_rotors()
>>> coded = en.encode_message(msg)
>>> print(coded)
# message chiffré
>>> en.reset_rotors()
>>> decoded = en.encode_message(coded)
>>> print(decoded)
# 'HELLOWORLD'
```

Si tous fonctionne normalement, le programme devrait afficher la version chiffrée puis déchiffrée de ton message !

---

### **Partie 3 : Bonus**

Bien joué!

Pour aller plus loin:

> Tu peux modifier le programme pour ajouter la fonctionnalité du tableau de permutation, qui n'est pas montrée ici.

> **Info**: une particularité de la machine Enigma qui a aidé A. Turing et son équipe de casser le code est la suivante : Enigma ne donnait jamais de lettre identique à celle donnée en entrée. Mais peux-tu expliquer pourquoi ?

# FIN
