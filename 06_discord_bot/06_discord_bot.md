---
title: Créer son premier Bot pour discord en python
date: 2020
author: Gabrielle Pauvert
---

Introduction
============

Dans ce TD, nous allons apprendre pas à pas comment créer un bot pour Discord en python et lui donner quelques premières commandes très simples, par exemple répondre à une commande par un “hello world”.

Création du Bot
===============

Tout d’abord, connectez vous sur le site de gestion des bots discord :
<https://discordapp.com/developers/docs/intro>.

Puis cliquez sur l’onglet `Applications` en haut à gauche.

![Onglet Application](ims/im1.png){width=10cm height=6cm}

Si vous ne possédez pas de compte discord, vous devez en créer un car cette action vous demandera de vous authentifier pour vous connecter à votre compte discord. Cliquez sur le bouton `New application` en haut à droite et entrez le nom de votre Bot pour le créer. Vous arrivez sur la page de votre bot, qui contient entre autres son identifiant (`ID`) dont vous aurez besoin pour la prochaine étape. Notez le quelque part, il servira !

![ID du bot](ims/im2.png){width=12cm height=5cm}

Cliquez ensuite sur l’onglet Bot à gauche puis sur `Add Bot`. Ici, vous
verrez les informations de votre Bot, dont son pseudo (`username`) et son avatar que vous pourrez modifier selon vos envies, et surtout son token qui **doit toujours rester secret !** [^1] (sauf pour vous). Si votre token fuite (sur
internet par exemple), changez le ! Gardez le dans un coin, on va aussi en
avoir besoin pour plus tard. Et ne vous inquiétez pas pour le token de mon bot sur l'image, je l'ai changé après avoir mis ça ici.

![Token du bot](ims/im9.png){width=12cm height=5cm}

Voilà, votre bot est créé. Il faut maintenant le connecter à discord et lui donner du code à lire et exécuter.

[^1]: Si quelqu'un connaît votre token, il pourra parler à la place de votre bot et lui faire faire ce qu'il veut.


Connecter son Bot
==============

Pour interagir avec votre bot, lui donner des instructions et le tester, vous allez avoir besoin d’y accéder via discord. Nous allons l’inviter dans un
serveur discord créé pour l'occasion. Vous pourrez supprimer ce serveur à la fin des tests si cela vous chante. Ouvrez discord (l'application que vous avez l'habitude d'utiliser) et créez un serveur de test en appuyant sur le `+` dans la barre de gauche en bas de vos serveurs.

Ensuite, dans votre navigateur de recherche (par exemple firefox ou google chrome), tapez le lien suivant en remplaçant \[votre ID\] par l’ID de votre bot, sans guillemet. Normalement, vous avez noté cet ID dans un coin lors de la partie "Création du Bot".

    https://discordapp.com/oauth2/authorize?client_id=[votreID]&scope=bot&
    permissions=0

Vous devriez voir apparaître une page comme celle ci.

![Page d'invitation du bot](ims/im3.png){width=6cm height=7cm}

Sélectionnez le serveur dans lequel vous voulez inviter votre Bot, c'est à dire le serveur Test que nous venons de créer, et cliquez sur le bouton
“Authorize”. Dans quelques instants, vous devriez voir votre Bot
apparaître en tant que membre de ce serveur. Pour l’instant,
il est hors-ligne. C’est tout à fait normal, car nous ne lui avons
pas encore donné de code à exécuter et nous ne l’avons pas lancé. C’est
ce que nous allons faire maintenant.

Coder son Bot
=============

Il est temps d’écrire le fichier python qui contiendra votre code.
Créez-en un où vous voulez à l’aide de votre éditeur de texte préféré.
Par défaut, si vous n’en connaissez aucun, vous pouvez utiliser gedit
sous linux. Nommez-le comme vous voulez avec l’extension `.py`, par
exemple `bot.py`, et remplissez le de la manière suivante :

``` python
import discord
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix='!', description="ce que vous voulez en"
+"description")
#vous pouvez changer la commande '!' en autre chose si vous le souhaitez

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)

#ici figureront les commandes et instructions pour votre bot

bot.run("token") #vous devez ici rentrer le token de votre bot,
#que vous avez noté plus haut.
```

Dans l’instruction `bot.run`, vous devez mettre entre guillemets `"` le vrai token de votre bot. Dans tout ce tuto, il figurera en clair sur votre fichier python, mais vous devrez le cacher si vous mettez votre code en ligne un jour
(rappelez-vous, il doit rester secret).

Les trois premières lignes de ce code indiquent les modules nécessaires, c'est à dire les fichiers dont python a besoin pour comprendre votre code. Par exemple, le module `discord` contient les fonctions créées pour faire le lien entre python et discord.
Ensuite, en ligne 4, on indique au bot qu'on fera appel à lui grâce au symbole `!` lorsqu'on lui donnera des commandes. Si je veux créer une commande que je veux appeler `coucou`, je lancerai cette commande dans discord en tapant `!coucou`.
Enfin, la dernière ligne permet de faire le lien entre le code écrit dans le fichier et le bot que vous venez de créer et connecter à discord.

Exécutez votre fichier python contenant le code du Bot. Par exemple si votre fichier s’appelle `Bot.py`, ouvrez un terminal linux, rendez vous dans le dossier contenant votre fichier et tapez `python3 Bot.py`. Vous aurez peut-être besoin de faire une étape intermédiaire si vous rencontrez une erreur. Il faut installer le module `discord` si celui ci n'est pas déjà installé. Pour cela, tapez `pip3 install discord.py`.

Si tout se passe correctement, vous devriez obtenir ce résultat :

![Connection du bot](ims/im4.png){width=9cm height=1.5cm}

Le terminal vous affiche `Logged in as ...` car dans le fichier que vous venez de lancer se trouve l'instruction

``` python
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
```

qui s’exécute au lancement du Bot (et uniquement à ce moment là).

Voilà, votre Bot apparaît désormais en ligne et connecté sur votre
serveur de test. Mais pour l’instant, il ne fait rien. Nous devons lui
donner des instructions.



Une première commande : Hello World
===================================

Nous allons coder une commande appelée `bonjour` qui demande à notre bot d'envoyer un message `Hello World !`. Dans votre fichier python, à l’endroit où doivent figurer les commandes et instructions (repérées par un commentaire dans votre fichier si vous ne l’avez pas effacé), ajoutez le code suivant :

``` python
@bot.command(pass_context=True)
async def bonjour(ctx):
    msg = ctx.message
    await msg.channel.send("Hello World !")
```

Sauvegardez, et relancez votre bot dans le terminal. Vous devrez d'abord reprendre le contrôle de votre terminal en arrêtant l'exécution précédente du Bot qui tourne en boucle. Pour cela, appuyez deux fois de suite sur `ctrl + C` avant de retaper `python3 Bot.py`.

Une fois votre bot relancé, retournez dans discord et tapez dans votre serveur de test la commande `!bonjour`. Votre Bot devrait vous répondre `hello world` comme ci-dessous.

![La commande "bonjour"](ims/im5.png){width=7cm height=2.5cm}


Réagir à un événement
=================

Laissez moi vous donner quelques explications. Le code que lit un bot discord est dit asynchrone, c’est à dire qu’au lieu de lire votre
code ligne par ligne et de l’exécuter au fur et à mesure comme
d’habitude, le code va s’exécuter en parallèle, un peu tout à la fois. Ce code particulier est repéré par les mots-clés `async` et `await` à ajouter avant les fonctions asynchrones, comme dans la ligne `await message.channel.send`. `async` est à mettre avant de définir une fonction asynchrone, et `await` avant d'en utiliser une. Les autres instructions sont exécutées comme vous en avez l’habitude.

De plus, chaque morceau de code asynchrone se déclenchera lorsque
certains événements arriveront. Nous en avons déjà vu deux exemples, l'affichage du `Logged in as ...` qui se déclenche quand vous lancez le bot (c'est un événement), et la commande "bonjour" qui se déclenche quand vous tapez `!bonjour` dans discord.

Il existe plein d'autres évènements. Une catégorie importante d'événements est constituée des commandes : le bot réagit à un mot devant lequel vous mettez un `!` (par exemple). Mais ce ne sont pas les seules, loin de là ! Vous pouvez lui demander de réagir à l’écriture d’un message, à l’ajout d’une réaction par quelqu’un, etc.

Voici un exemple d’instruction qui réagit à un message dans lequel quelqu’un à écrit “le jeu” en disant “J’ai perdu...” :

``` python
@bot.listen()
async def on_message(msg):
    if "le jeu" in msg.content:
        await msg.channel.send("J'ai perdu...")
```

![Bot réagissant à un message](ims/im6.png){width=6cm height=2.5cm}

Comme vous pouvez le voir, ici le bot n’attend pas qu’on s’adresse à lui
par une commande, il reste tout le temps à l’écoute et exécute son code
chaque fois qu’un message est posté. Si les conditions sont remplies,
il envoie alors lui-même un message.

Vous aurez peut-être remarqué les lignes étranges `@bot.event`, `@bot.command` ainsi que `@bot.listen()` qui commencent par des arobases. Il s'agit d'une notion compliquée de python qu'on appelle les décorateurs. Un décorateur sert à modifier le comportement d'une fonction qu'on définit juste en dessous. Ici les décorateurs servent comme boîte noire de discord, pour faire le lien entre le code et le bot.

Vous ne devez savoir que deux choses pour les utiliser correctement pour votre bot :

- Si vous voulez coder une commande pour votre bot, vous allez avoir besoin de mettre la ligne `@bot.command(pass_context=True)` avant de définir la fonction de la commande. Ceci lui indiquera qu'il doit exécuter cette partie du code lorsque qu'on fait appel à lui avec un `!` suivi du nom de la fonction.

- Si vous voulez que votre bot réagisse à un autre événement, vous devez mettre la ligne `@bot.listen()` avant de définir votre fonction. Ici, il saura qu'il doit rester à l'écoute. Mais de quoi ? De l'événement qui correspond au nom de votre fonction. Dans l'exemple ci-dessus, on lui a demandé d'exécuter son code à chaque fois que quelqu'un poste un message grâce à la fonction `on_message` qui prend en argument le message posté. Faites donc bien attention aux noms que vous donnez à vos fonctions et à leurs arguments, vous ne pouvez pas les choisir librement ici.

Exercices
=================

- Faites de votre bot un juge du "ni oui ni non". Si quelqu'un écrit "oui" ou "non" dans un message, le bot lui dit qu'il a perdu.

- [difficile !] Codez un jeu de devinette avec votre bot. Donnez un nombre à votre bot puis essayez de le trouver en proposant des nombres et en demandant à votre bot de vous indiquer si le nombre est plus ou moins grand.

![Jeu de devinette](ims/im10.png){width=4cm height=5.5cm}

(Indication : pour récupérer la chaîne de caractère (string) correspondant au message de la commande, vous pouvez utiliser `ctx.message.content`.)


## Quelques explications

Ne lisez cette partie que si vous êtes à l'aise sur le reste ! Nous allons aborder des notions très avancées.

Avant de vous laisser libre, détaillons un peu le fonctionnement de l'instruction particulière `msg.channel.send` que l'on a rencontré plusieurs fois. Lorsqu'on écrit `msg.channel.send`, on manipule l'objet `msg`, le message qui a été envoyé par quelqu'un. Puis on récupère le salon dans lequel ce message a été envoyé `msg.channel`. Enfin, dans ce salon là, on demande au Bot d'envoyer un message `.send`.

On dit alors que l'on fait de la programmation “orientée objet”, car l’on ne fait que manipuler des “objets” (ici le message `msg` ou encore son salon `msg.channel`) et leurs attributs. Les attributs sont repérés par des “.” et peuvent être des fonctions, des chaînes de caractères, d'autres objets etc. qui sont liés à l'objet. Par exemple, le `.channel` est encore un objet qui représente le salon et le `.send` est une fonction liée à l'objet salon, lui-même lié à l'objet message.

Autre exemple, le `ctx.message.content` de tout à l'heure. Ici `ctx` correspond au "contexte", un objet assez général que discord donne à ses fonctions de commandes. Puis `.message` correspond au message (auquel le bot réagit ici) et le `.content` correspond au contenu du message. C'est une chaîne de caractères.

Cette façon de programmer peut surprendre un peu et est assez particulière, ce tuto n’a pas pour but de vous faire un cours sur les objets python, qui mériteraient de traiter le sujet à part, mais de vous donner quelques pistes pour les utiliser sans
forcément bien les comprendre.


À vous de jouer !
=================

Pour voir les événements disponibles pour votre bot, vous pouvez vous référer à la documentation python de discord.py (en Anglais...):
<https://discordpy.readthedocs.io/en/latest/api.html>.

Pour celles qui savent lire l'Anglais, vous y trouverez dans l’onglet `Event reference` une liste exhaustive de tous les événements pour lesquels vous pouvez demander à votre bot de
faire quelque chose. Par exemple notre `on_message` est là :

![Instruction on_message](ims/im7.png){width=13cm height=8cm}

La doc renseigne aussi sur les actions que vous pouvez demander
à votre Bot. Par exemple, nous lui avons demandé d’envoyer
des messages dans des salons discord (channels en anglais) grâce à
l’instruction `msg.channel.send`. Pour plus d'information, allez voir les onglets correspondants. Ici, c'est dans l’onglet `TextChannel` (objet salon) que vous trouverez les explications pour l'instruction `send` qui envoie un message dans un salon.

![Instruction send](ims/im8.png){width=17cm height=10cm}

### Bon Courage !

Lire la doc et la comprendre peut être très difficile. N’hésitez pas à tester des choses par vous même et à demander autour de vous comment faire tel ou tel truc. Bonne programmation !
