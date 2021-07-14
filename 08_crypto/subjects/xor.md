# **XOR / Ou Exclusif**

>Prérequis : l'hexadécimal, la table ASCII

## Quelques rappels

---

_Explication du binaire à ajouter ?_

### **L'hexadécimal**

L'hexadécimal est un système d'écriture en base 16. Il utilise 16 symboles : les lettres de A à F (inclus) et les chiffres de 0 à 9 (inclus).

À titre d'exemple, voici comment compter de 0 à 20 en hexadécimal :

```sh
base 10 : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
base 16 : 0 1 2 3 4 5 6 7 8 9  A  B  C  D  E  F 10 11 12 13 14
```

> **Remarque :** on utilise le système décimal, en base 10, dans la vie courante. Il utilise donc 10 symboles : les chiffres de 0 à 9.

### **La table ASCII**

La table ascii (American Standard Code for Information Interchange), est une norme d'encodage des caractères. C'est une représentation qu'utilisent les ordinateurs pour garder en mémoire des caractères. Par exemple, avec la table ASCII, le `A` correspond à `65` et le `a` correspond à `97`.

![Ascii](../imgs/ascii.png "Table ASCII")

## Un peu de théorie

---
Le XOR est un opérateur logique, on l'appelle également le **OU Exclusif** et en anglais **eXclusive OR**. Il est souvent représenté avec le symbole :  **⊕** ". En Python, on utilisera : **^**.

Table de vérité :

- On définit A et B deux opérandes sur lesquelles on va appliquer XOR.

|A|B|A ⊕ B|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

En observant la table de vérité, on peut dire que le XOR peut se définir de la façon suivante:

- Si les deux opérandes sont différentes, alors le résultat est 1
- Si les deux opérandes sont identiques, alors le résultat est 0

## Chiffrer des messages avec XOR

Dans cet exercice, vous allez chiffrer des messages avec XOR. Cet opérateur logique possède en effet des propriétés intéressantes qui vont permettre de chiffrer et déchiffrer un message avec la même clé.

Pour mieux vous faire comprendre le processus, appliquons-le avec un exemple en binaire. Admettons que le message que l'on souhaite chiffrer est `01100101 01110000 01101001` et que la clé est `01110100 01100001 01100001`.

```sh
Étape de chiffrement
Message :         01100101 01110000 01101001
Clé :             01110100 01100001 01100001
Message ⊕ Clé =  00010001 00010001 00001000 (Message chiffré)

Étape de déchiffrement
Message chiffré :        00010001 00010001 00001000
Clé :                    01110100 01100001 01100001
Message chiffré ⊕ clé = 01100101 01110000 01101001

On retrouve bien le message initial !
N'hésitez pas à essayer par vous même !
```

Cette explication avait pour but de vous faire comprendre le fonctionnement de XOR et du processus de chiffrement / déchiffrement. Lorsque vous allez coder cette méthode de chiffrement en Python, vous n'aurez pas besoin de passer par du binaire, vous utiliserez de l'hexadécimal.

Maintenant que vous connaissez le XOR, il est temps d'écrire les fonctions !

## Let's code

---
Pour implémenter cette méthode de chiffrement, il va être plus simple de diviser le problème en plusieurs parties, et donc en plusieurs fonctions. Comme écrit précedemment, pour appliquer le XOR, pas besoin de passer par du binaire, nous allons utiliser de l'hexadécimal. La première fonction va donc transformer du texte en hexadécimal. La deuxième va appliquer XOR sur le message transformé en hexadecimal avec une clé en hexadecimal de la même longueur. Finalement, la troisième va transformer de l'hexadecimal en lettres, texte lisible pour nous !

**Comment obtenir une clé en hexadécimal de la même longueur que le message que l'on souhaite chiffrer ?**

C'est tout simple, une fonction générant des clés en hexadécimal vous est fournie : `randomHexa(lenstr)`. Elle prend en paramètre `lenstr` qui correspond à la longueur du message initial en lettres et renvoie une clé générée aléatoirement. Cette fonction vous sera grandement utile pour effectuer vos tests !

Voici la fonction :

```py
import random

def randomHexa(lenstr):
    string = ""
    for i in range(lenstr):
        rdm_int = random.randint(0, 255) # on génère un entier entre 0 et 255
        string += chr(rdm_int) # on convertit en caractère et on concatène
    res = stringToHexa(string) # on convertit en hexa pour avoir une clé en hexa
    return res
```

Elle utilise une fonction que vous devez implémenter. En cas de difficulté, n'hésitez pas à demander de l'aide :)

Exemple d'application :

```py
>>> s = "Hey !"
>>> randomHexa(len(s))
02d5ff5087
```

Ainsi, il va falloir implémenter les fonctions `stringToHexa(s)`, `msgXor(m, key)` et `hexaToString(hexa)`.

### La fonction `stringToHexa(s)`

Cette fonction va se charger de transformer une chaîne de caractères formée de lettres en une chaîne de caractères en hexadécimal. Elle prend en paramètre `s`, une chaîne de caractères.

Pour convertir une chaîne de caractères en hexadécimal. Il va falloir le faire lettre par lettre et appliquer quelques transformations à chacune des lettres :

- Transformer la lettre en caractère ASCII (en nombre entier)
- Convertir le caractère ASCII en hexadécimal
- Adapter le résultat de l'étape précédente pour qu'il soit de longueur 2 (ajouter des 0 si besoin) et qu'il ne contienne que de l'hexadecimal (sans "0x", voir la fonction `hex()`expliquée plus bas)

**Quelques fonctions utiles !**

```py
# Les fonctions ord() et chr() permettent de transformer un caractère en son code ASCII et vice-versa.

>>> ord('A')
65
>>> ord('C')
67
>>> chr(65)
'A'

# La fonction hex() permet de convertir un nombre entier en base 10 en un nombre en base 16 (hexadecimal). Elle renvoie une chaîne de caractères.
>>> hex(16)
'0x10'
>>> hex(42)
'0x2a'

# Pour retirer un nombre x de lettres au début d'un mot, on utilise [x:]
>>> s = "moustique"
>>> s[4:]
'tique'

#La fonction zfill() prend en paramètre un nombre entier. Elle permet de rajouter des 0 au début d'une chaîne de caractères si la longueur de celle-ci est inférieure au paramètre donné à la fonction. 
>>>'hello'.zfill(6)
'0hello'
```

### La fonction `msgXor(m, key)`

Cette fonction va se charger d'appliquer XOR entre le message et la clé (soit message ⊕ clé). Elle prend donc en paramètre `m` une chaîne de caractères correspondant au message que l'on désire chiffrer, et **qui a déjà été converti en hexadecimal**. Elle prend également `key` qui est également une chaîne de caractères en hexadecimal et qui est de la même longueur que `m`. `msgXor(m, key)` va renvoyer une chaîne de caractères en hexadecimal.

Pour appliquer XOR, voici les différentes étapes qu'il faudra implémenter:

- Sélectionner chaque caractère des chaînes de caractère 2 par 2
- Les convertir en nombre entier
- Appliquer XOR !

**Quelques fonctions utiles...**

```py
# La fonction int() va convertir un caractère ou une chaîne de caractère en un entier. Dans notre cas, nous allons renseigner deux paramètres : une chaîne de caractères en hexadécimal et la base de notre chaîne de caractères (ici, 16 car on utilise de l'hexadecimal). 
>>> int('10', 16)
 16
>>> int('FA', 16)
250

# L'opérateur logique XOR est symbolisé par ^ en Python. Il peut être utilisé avec des nombres entiers.
>>> 42^56
18

# Les fonctions et opérateurs hex(), [x:], zfill(), expliqués plus haut.
```

### La fonction `hexaToString(hexa)`

Cette fonction va se charger de convertir une chaîne de caractères en hexadecimal, en une chaîne de caractères de lettres, que l'on pourra lire et comprendre. Elle va donc renvoyer une chaîne de caractères. `hexaToString(hexa)` prend en paramètre `hexa`, une chaîne de caractères en hexadecimal.

Les fonctions dont vous aurez besoin pour implémenter votre solution ont déjà été expliquées plus haut. Les étapes ne sont pas données mais vous pouvez les déduire des étapes de `stringToHexa()`.

À vous de jouer !

## Sources

---

- [Table ASCII](https://computersciencewiki.org/images/3/3d/Ascii_table.png)

- [Infos sur la table ASCII](http://www.table-ascii.com/)
