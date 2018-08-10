---
layout: post
modal-id: "« L’ouverture » d’un logiciel libre : retour sur les ateliers du 22 mars (1/3)"
author: Paul Schmite, équipe EIG
author_link: https://entrepreneur-interet-general.etalab.gouv.fr/
twitter: schmitologie
description: "Le 22 mars s’est tenue la deuxième session d’accompagnement des EIG.  Elle était organisée autour de trois ateliers : l’un sur les questions à se poser pour définir son produit ; l’autre sur la façon d’impliquer les utilisateurs dans sa conception ; le dernier sur l’ouverture du code source &#x2013; l’un des enjeux majeurs du programme EIG étant de permettre le développement, au sein de l’administration, de logiciels libres, ouverts aux contributions extérieures."
---
Voici un petit retour d’expérience sur ma participation à cet atelier,
animé par Bastien, qui nous a aidé à nous frayer un chemin au milieu
de ces questions : pourquoi ouvrir ?  pour quelles contributions ?
quelles craintes à surmonter ?  comment choisir sa licence libre ?

![Le paperboard de préparation de l'atelier du 22 mars.](/img/eig-atelier-utilisateurs.jpg)
_En pleine préparation de l'atelier du 22 mars ! © Bastien Guerry [CC-by-sa](https://creativecommons.org/licenses/by-sa/3.0/)_

# Faire de l’open source, ça veut dire quoi  ?

La discussion a commencé par la description d’un projet open source
typique, en distinguant les aspects techniques (pour lesquels nous
avons parcouru le [test de Joel](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code) sur les 12 étapes pour mieux coder) et
les aspects d’ouverture, parmi lesquels :

-   indiquer clairement la licence libre utilisée ;
-   avoir et animer une communauté d’utilisateurs et de testeurs ;
-   mettre à disposition un outil de remontée de bug ;
-   avoir une documentation claire et à jour ;
-   faire que les utilisateurs deviennent des contributeurs ;
-   avoir une feuille de route claire et à jour ;
-   permettre un développement itératif et journalier ;
-   indiquer clairement qui fait la maintenance, et comment.

La présentation, lors de l’atelier, d’[Open Scraper](https://github.com/entrepreneur-interet-general/OpenScraper), a permis de se
poser ces questions autour d’un cas précis.  Développé par Julien
Paris, EIG pour le défi [Social Connect](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/socialconnect/), l’outil permet de collecter
(*scraper*) les données d’une page web.  Cet outil ne faisait pas partie
des réalisations prévues par le projet, mais il constitue une brique
importante pour le défi&#x2026; et potentiellement pour d’autres, car ces
problématiques de *scraping* sont assez fréquentes.  Cette création *ad
hoc* d’un logiciel sous licence libre permet au projet de contribuer au
développement de nouveaux services tout en instillant au sein de
l’administration un intérêt pour le libre.

![La page d'accueil de l'outil Open Scraper, développé par Julien Paris pour le défi SocialConnect](/img/openscraper.jpg)
_La page d'accueil de l'outil [Open Scraper](http://www.cis-openscraper.com/), développé par Julien Paris pour le défi SocialConnect_

# Respecter les valeurs d’une communauté de pratiques

Nous avons aussi eu l’exemple d’un EIG qui a forké un logiciel libre
existant en oubliant de conserver la mention de la licence d’origine.
Il s’est fait tomber dessus par un contributeur, a corrigé le tir, et
a reçu ensuite un mot gentil de l’auteur original, qui a bien compris
qu’il n’y avait aucune intention de nuir.

L’anecdote est instructive : dès qu’on fait du logiciel libre, on
entre en relation avec de *Vraies Personnes™*, tout une communauté de
pratiques qui veille, parfois sermonne, souvent conseille.  Toute
personne ou institution qui se met au libre, doit se préparer à ce
processus d’apprentissage.

# Quelle licence libre pour quel produit ?

La discussion a ensuite naturellement porté sur le choix de la licence
libre.

Nous avons d’abord évoqué le fait qu’en pratique, certaines licences
visent des types de contenu particuliers : la Licence Ouverte 2.0 est
adaptée aux données en open data, les licences [Creative
Commons](https://creativecommons.org/) aux contenus médias (images,
vidéos, etc.) et les autres licences libres comme la [GNU
GPLv3+](https://www.gnu.org/licenses/gpl-3.0.fr.html) ou la licence
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) pour du
code.

## Licences Copyleft et « permissives »

Bastien a ensuite présenté les deux grandes familles de licences
libres : les licences dites « *copyleft* », ou « à réciprocité »,
inventées par Richard Stallman, le père du logiciel libre ; et les
licences dites « permissives », utilisées surtout dans le monde de
l'entreprise.

Quelle est la différence ?  Si un logiciel intègre du code placé sous
GNU GPL, il doit lui-même être publié sous licence GPL ou équivalente.
Si un logiciel intègre du code publié sous licence Apache 2.0 (l'une
des licences « permissive »), il n'y a pas d'obligation particulière
à ce que le nouveau logiciel soit publié sous la même licence.

![Les débats sur les licences, source de plaisir infini !](/img/xkcd-open-source.jpg)
_Les débats sur les licences, source de plaisir infini ! © XKCD, [CC-by-nc](https://www.xkcd.com/license.html)_

Si on limite la question au code source des logiciels, c’est une
approche au cas par cas qui convient, mais en pratique, on se trouvera
souvent dans l’une de ces situations : soit le code qu’on produit est
dérivé d’un logiciel libre *existant*, auquel cas la pratique commune
est d’utiliser la même licence libre que celui-ci ; soit on produit du
*nouveau code*, auquel cas on a tendance à se caler sur les pratiques
de logiciels similaires (ayant les mêmes fonctions et/ou écrits dans
le même langage informatique).  Par exemple : si vous forkez un
logiciel qui est publié sous licence GPLv3+ ou Apache 2.0, vous
placerez votre logiciel sous GPLv3+ ou Apache 2.0 aussi ; si vous
écrivez un nouveau logiciel en Ruby, vous placerez votre logiciel sous
licence MIT, qui est la plus utilisée dans l’écosystème Ruby ; etc.

# Pour ne pas finir

Ces questions juridiques sont souvent stressantes pour les personnes
qui les découvrent, notamment parce qu’elles sont l’objet de débats
passionnés entre « libristes ».  Peut-on publier du code source sans
licence libre ?  Que faire alors si la licence choisie ne correspond
pas aux finalités du projet ?  Est-ce que je peux modifier du code
libre sur mon serveur sans partager mes modifications ?  Est-ce que je
peux utiliser deux licences ?  Pour simplifier et encourager une
approche pragmatique, nous avons convenu de commencer [une FAQ](https://github.com/entrepreneur-interet-general/eig-link/blob/master/ouverture-faq.org) sur ces
questions de licence et d’ouverture&#x2026; c’est ouvert, n’hésitez pas à
[ouvrir un ticket](https://github.com/entrepreneur-interet-general/eig-link/issues/new) pour poser une nouvelle question !

Au final, Bastien a insisté sur le fait que nous pouvions imaginer des
« dégrés » d’ouverture du code source, en allant du projet qui fait le
minimum (publier le code sous une licence libre) à un projet qui tente
de jouer à fond la carte de l’open source.  Ces degrés sont présentés
dans [cette page](https://github.com/entrepreneur-interet-general/eig-link/blob/master/ouverture.org#des-degr%25C3%25A9s-douverture-des-projets-libres) - là aussi, vos retours sont les bienvenus.

L’atelier s’est clos sur l’engagement d’ouvrir et de partager autant
que possible les outils développés dans le cadre du programme.  Les
codes seront progressivement mis à jour sur [le compte d’organisation
Github EIG](https://github.com/entrepreneur-interet-general/) - suivez-nous !


# Quelques lectures supplémentaires

-   La politique de contribution open source de l’État : version [en
    ligne](https://disic.github.io/politique-de-contribution-open-source/), version de travail sur [github](https://github.com/DISIC/politique-de-contribution-open-source)

-   La [liste des licences libres](https://www.data.gouv.fr/fr/licences) pour l’administration

-   La [Licence Ouverte 2.0](https://www.etalab.gouv.fr/licence-ouverte-open-licence)

-   Des [guides sur l’open source](https://opensource.guide) publiés par Github

-   Des guides [britanniques](https://www.gov.uk/government/publications/open-source-guidance) et [états-uniens](https://open-source-guide.18f.gov/) sur l’open source

-   Quelques recommandations pour la [gestion d’un projet libre au sein
    de l’administration](https://github.com/entrepreneur-interet-general/eig-link/blob/master/ouverture.org), accompagnées d’une [FAQ](https://github.com/entrepreneur-interet-general/eig-link/blob/master/ouverture-faq.org)

-   The Joel Test: [12 Steps to Better Code](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/)

