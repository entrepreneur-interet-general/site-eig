---
layout: post
modal-id: Un point technique après deux mois du programme EIG
author: Bastien Guerry, EIG Link
author_link: https://entrepreneur-interet-general.etalab.gouv.fr/
twitter: bzg2
description: "Quelles sont les « stacks » des défis EIG ?  Font-ils de « l'agile » ?  Comment sont leurs outils de gestion de projet ?  Où est publié leur code ?  Quels rituels collectifs se mettent en place ?  Quel est le rôle de l'EIG Link ?  Un point technique après deux mois de cette deuxième année EIG."
---

Les 28 « entrepreneur·es d'intérêt général » ne sont pas isolés les
uns des autres : ils échangent et font progresser la cohérence
technique du programme en mettant en place des outils mutualisés et
des rituels.  Mon défi [EIG
Link](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/eiglink/)
a pour mission d'encourager et de pérenniser cette cohésion de groupe
et cette cohérence technique.  **On avance et ça se voit** !

![Thérapie de groupe pour les EIG !  On parle de nos expériences
tech.](/img/LLL_ZoeJung_IMG_4987.jpg) _Thérapie de groupe pour les
EIG !  On parle de nos expériences tech lors du bootcamp © Zoe Jung._

# Le bootcamp : un moment de forte cohésion

Soizic Pénicaud (Etalab) l'a très bien raconté dans [cette entrée de
blog](https://entrepreneur-interet-general.etalab.gouv.fr/posts/2018/02/27/bootcamp-comment-souder-un-collectif-de-talents/),
le bootcamp EIG fut un moment important pour la cohésion du groupe :
nous avons sympathisé et nous avons beaucoup échangé sur tous nos
défis.

La « [bulloterie](https://twitter.com/la_bulloterie) » (un format de
découverte des compétences d'un groupe, imaginé par [Sébastien
Kurt](https://twitter.com/Anachitect)) a donné lieu à un premier
protoype développé par Philéas Condemine, du défi [Lab
Santé](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/labsante/).
Paul Schmite d'Etalab a ensuite saisi l'ensemble de ces données et
j'ai dans ma TODO liste de proposer une interface web pour les
explorer de façon interactive.  En attendant, les défis présentent
leurs outils dans un fichier
[stack.org](https://github.com/entrepreneur-interet-general/eig-link/blob/master/stack.org)
qui continue d'évoluer.

![Un aperçu de l'exercice de « bulloterie » lors du
bootcamp](/img/bulloterie_apercu.jpg) _Un aperçu de l'exercice de
« bulloterie » lors du bootcamp_

![Le prototype pour visualiser la
bulloterie](/img/bulloterie_proto.png) _Le prototype pour visualiser
la bulloterie, développé par Philéas en shinyapps.io_

Le bootcamp a aussi été l'occasion de proposer quelques premiers
projets collaboratifs, dont un dépôt pour partager des
[tutoriels](https://github.com/entrepreneur-interet-general/tutos-2018)
et une liste
d'[outils](https://github.com/entrepreneur-interet-general/eig-link/blob/master/boite-a-outils.org
" ") : voyez par exemple le tutoriel publié par Julien Naour, du défi
[Lab
Santé](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/labsante/),
sur une [introduction à
Gitlab](https://gitlab.com/jnaour/tutoriel-gitlab/wikis/tutoriel-gitlab) :
typiquement ce qu'on essaie de faire quand on parle de
« transformation numérique » des administrations !

# La gestion de projet : subsidiarité et dénominateur commun

Le programme EIG est l'occasion d'introduire un peu d'« agilité » dans
la façon dont les administrations gèrent les projets.  Les principes
de cette « agilité » sont bien résumés dans [ce
document](https://www.gov.uk/service-manual/agile-delivery/core-principles-agile)
du gouvernement britannique :

- se concentrer sur les besoins des utilisateurs ;
- publier les livrables de manière itérative ;
- améliorer constamment la manière dont l'équipe travaille ;
- échouer tôt et apprendre rapidement ;
- planifier constamment.

En dehors de ces grandes directions, pas question d'imposer une
méthode agile particulière (SCRUM ou autre) ni d'outil spécifique pour
la mettre en oeuvre.  Les EIG sont force de proposition, mais par
principe de subsidiarité, ils définissent leurs méthodes et leurs
outils en fonctions des contraintes locales, avec leurs mentors et
leurs équipes d'accueil.

Certains défis
([Archifiltre](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/archemse/
" "),
[b@liseNAV](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/balisenav/),
[SocialConnect](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/socialconnect/))
sont donc déjà lancés dans des *sprints* avec des *user stories* bien
définies, mais ce modèle n'est pas commun. Pour le défi
[BrigadeNumérique](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/brigadenumerique/),
Dora et Jean-Baptiste utilisent l'outil de kanboard que j'ai installé
sur notre serveur, mais d'autres équipes utilisent des outils locaux.

![L'utilisation du "kanboard" par le défi BridageNumérique](/img/brigadenumerique-board.png)
_L'utilisation du "kanboard" par le défi BridageNumérique_

En revanche, pour continuer de multiplier les points de contact entre
défis, il nous faut un **un outil de suivi collectif**.  Pour
l'instant, nous stockons les retours hebdomadaires de chaque défi dans
ce [gros fichier
partagé](https://github.com/entrepreneur-interet-general/eig-link/blob/master/suivi.org). Ce
n'est pas le plus pratique, mais c'est un premier test avant d'avoir
un outil web plus adapté.

# Les outils : adaptation et mutualisation

Le dépôt
[eig-link](https://github.com/entrepreneur-interet-general/eig-link)
présente l'ensemble des outils mis à disposition des EIG :

- un serveur [Proxmox](https://www.proxmox.com) de 32GO ;
- un espace de fichiers partagés avec [Nextcloud](http://nextcloud.com/) ;
- un [agenda commun public](https://cloud.eig-forever.org/index.php/apps/calendar/p/5S4DP594PDIVTARU/EIG2018) (via notre instance Nextcloud) ;
- un [agenda des événements annexes](https://cloud.eig-forever.org/index.php/apps/calendar/p/C1YPGSGZ1JZPVDDU/EIG2018-Open) qui nous intéressent ;
- une instance de [gogs](http://gogs.io) pour des dépôts privés ;
- une instance de [kanboard](http://kanboard.org/) ;
- une instance de [Matomo](https://matomo.org) pour des statistiques.
- un client web [Kiwirc](https://kiwiirc.com) pour nous connecter à notre canal IRC.

Cela va sans dire (mais cela va mieux en le disant) : ces outils
mutualisés s'appuient tous sur des [logiciels
libres](https://fr.wikipedia.org/wiki/Logiciel_libre) !

La question qui se pose souvent est celle-ci : si un EIG a besoin
d'une machine virtuelle pour son défi, doit-il la demander à son
administration ou doit-il utiliser celle que nous mettons à sa
disposition via notre panoplie d'outils ? Les deux, mon capitaine !
Les outils EIG n'ont pas vocation à remplacer ceux que les
administrations mettront en place pour pérenniser les projets, mais à
dépanner et à montrer comment ces solutions se mettent en oeuvre.  Si
ces outils aident à assurer la transition, c'est bien ; s'ils sont
l'occasion d'une discussion avec des DSI pour voir comment faire
évoluer leurs systèmes, c'est encore mieux !

# Les rituels : « less is more »

Les « rituels » sont les habitudes de travail que nous prenons en tant
que groupe.  Nous essayons de les rendre [peu
invasifs](http://www.paulgraham.com/makersschedule.html) et de les
garder les plus collectifs possible.

- Nous communiquons au quotidien via le service slack et via une liste
  de discussion de [framalistes.org](https://framalistes.org).

- Entre le jeudi soir et le vendredi midi, une personne de chaque défi
  envoie un message sur la liste avec un point hebdomadaire sur ce qui
  a été fait et ce qui va être fait.

- Nous discutons de cela sur slack entre 11h30 et 12h30 le vendredi.

- Nous nous retrouvons en présentiel au [Liberté Living
  Lab](https://www.liberte.paris/liberte-living-lab) un jeudi tous les
  quinze jours pour le programme d'accompagnement, soit entre EIG soit
  avec les mentors.
  
- Nous nous retrouvons les mercredi après-midi pour simplement être
  assis dans la même salle du LLL et travailler ensemble.
  
Ce qui se met en place doucement :

- Des sessions de « revue de code » avec Quentin Decock, du Liberté
  Living Lab. La première a eu lieu le 14 mars autour du logiciel
  [OpenScraper](http://github.com/entrepreneur-interet-general/OpenScraper)
  et du défi
  [Prédisauvetage](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/donneesauvetagemaritime/).
  Nous allons en reprogrammer une bientôt.
  
- Des sessions d'échanges techniques libres le mercredi avec des
  « invités », des ressources du réseau des EIG (merci à Tiphaine
  Phe-Neau du défi
  [Prévisecours](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/previsecours/)
  d'avoir lancé cette idée !)

Ce qui est intéressant, c'est que tout cela évolue : l'idée de se
retrouver le mercredi après-midi pour travailler a été proposée par
les EIG ; certains s'impliquent dans la conception des séances du
programme d'accompagnement ; et nous réfléchissons à la manière de
rendre le point hebdomadaire du vendredi midi plus efficace.  Nous
envisageons notamment de le faire sur IRC plutôt que sur slack pour
l'ouvrir à toute personne désireuse d'en apprendre plus sur les défis
et le programme.

![Rencontre avec Quentin Decock lors du bootcamp, le référent technique du LLL](/img/LLL_ZoeJung_IMG_5169.jpg)
_Rencontre avec Quentin Decock lors du bootcamp, le référent technique du LLL_

# L'écosystème : *No EIG is an island*

En plus de l'entraide naturelle au sein des équipes d'EIG par défi,
l'entraide *entre* défis se développe.

Cette entraide s'exprime dans la création de canaux techniques dédiés
sur le slack, en présentiel le mercredi ou lors des sessions de revue
de code.

Au-delà, les EIG de cette deuxième promotion interragissent avec ceux
de la première et avec les développeurs et les datascientistes
d'Etalab. C'est par exemple Victor Schmidt du défi
[Hopkins](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/hopkins/)
qui fait remonter un souci avec le logo du [site
EIG](https://entrepreneur-interet-general.etalab.gouv.fr), souci
auquel répond [Frédéric Bardolle](https://twitter.com/seiteta) de la
première promotion... ou bien Christophe Ninucci du défi [Signaux
Faibles](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/signauxfaibles/)
qui pose une question à Christian Quest d'Etalab, et leur échange qui
aboutit à la publication d'un [nouveau jeu de
données](https://www.data.gouv.fr/fr/datasets/historique-des-changements-de-codes-siret/)
sur https://data.gouv.fr.  Ce sont aussi les EIG qui participent au
forum « Open d'État » - voir ce tweet de [Jean-Baptiste Le
Dévéhat](https://twitter.com/jbledevehat), du défi
[BrigadeNumérique](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/brigadenumerique/) :

<blockquote class="twitter-tweet" data-lang="fr"><p lang="fr" dir="ltr">Première rencontre du forum &quot;Open d’Etat&quot; <a href="https://twitter.com/hashtag/OpenGov?src=hash&amp;ref_src=twsrc%5Etfw">#OpenGov</a> <a href="https://twitter.com/hashtag/OpendEtat?src=hash&amp;ref_src=twsrc%5Etfw">#OpendEtat</a> <a href="https://twitter.com/Etalab?ref_src=twsrc%5Etfw">@Etalab</a> <a href="https://twitter.com/datactivi_st?ref_src=twsrc%5Etfw">@datactivi_st</a> <a href="https://twitter.com/vrmtvrmt?ref_src=twsrc%5Etfw">@vrmtvrmt</a> <a href="https://t.co/gdn5MZzJDz">pic.twitter.com/gdn5MZzJDz</a></p>&mdash; Jean-Baptiste Le Dévéhat (@jbledevehat) <a href="https://twitter.com/jbledevehat/status/973256889051045888?ref_src=twsrc%5Etfw">12 mars 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

C'est ce qu'on pourrait appeler le niveau « **EIG²** », quand on
croise nos ancêtres les EIG 1, nos cousins d'Etalab ou les acteurs de
la transformation numérique... comme lorsqu'Emmanuel Gautier, du défi
[Archifiltre](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/archemse/),
passe un coup de balai après avoir passé la nuit à coder pour [la nuit
du code citoyen](http://nuitcodecitoyen.org).

<blockquote class="twitter-tweet" data-lang="fr"><p lang="fr" dir="ltr">Manu, le <a href="https://twitter.com/hashtag/DataScientist?src=hash&amp;ref_src=twsrc%5Etfw">#DataScientist</a> parfait : il passe la serpillière <a href="https://twitter.com/LaPaillasse?ref_src=twsrc%5Etfw">@LaPaillasse</a> après avoir aidé des projets de <a href="https://twitter.com/hashtag/NuitCodeCitoyen?src=hash&amp;ref_src=twsrc%5Etfw">#NuitCodeCitoyen</a> pendant 24h non-stop à la <a href="https://twitter.com/hashtag/SocialGoodWeek?src=hash&amp;ref_src=twsrc%5Etfw">#SocialGoodWeek</a> ! <a href="https://t.co/Pt5aGNvbCh">pic.twitter.com/Pt5aGNvbCh</a></p>&mdash; Latitudes (@LatitudesTfG) <a href="https://twitter.com/LatitudesTfG/status/972570281901481985?ref_src=twsrc%5Etfw">10 mars 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

![Emmanuel, encore debout après une nuit de code citoyen](/img/nuitducodecitoyen.jpg)
_Emmanuel, encore debout après une nuit de code citoyen_

... enfin, plus loin encore, il y a le niveau « **EIG³** » ! C'est
quand on se jette carrément dans le grand bain et qu'on publie des
propositions d'améliorations de logiciels libres, le bien commun de
l'écosystème auquel on contribue ! C'est Christophe ouvrant [une
*issue*](https://github.com/tidyverse/dplyr/issues/3355) dans le
Tidyverse ; Tiphaine qui sollicite une *pull request* pour le code
d'[open-moulinette](https://github.com/anthill/open-moulinette/pull/61) ;
ou Victor qui partage la librairie python
[mkinx](https://pypi.org/project/mkinx/).

Vous l'avez compris : **on met les mains dans le cambouis, on avance,
on aime ça et ça se voit** !

# Le défi EIG Link, c'est quoi ?

Je ne suis ni « animateur », ni « manager », mais agent de **liaison**
et de **valorisation**.

J'essaie de détecter des *besoins communs* aux défis et de mettre en
oeuvre des solutions : celles-ci peuvent se trouver soit du côté des
outils (par ex. aider à la prise en main des machines virtuelles),
soit du côté de la communication (par ex. aider un défi à avancer sur
les aspects de *product research*).

Pour la valorisation, je n'ai qu'à me baisser et ramasser tellement
cela foisonne -- mais c'est justement un problème délicat à résoudre :
quelle interface mettre en place pour rendre accessible tout ce qui se
fait ?  À suivre...

# Use The Source, Luke.

Assez parlé, retrouvez **tout le code** que nous développons dans
notre [organisation sur
github.com](https://github.com/entrepreneur-interet-general/).

Si vous avez des questions, n'hésitez pas : `bastien.guerry @ data.gouv.fr`

À bientôt pour d'autres nouvelles de nos avancées techniques !
