---
layout: defi2019
titre: LexImpact
site: /defis/2019/leximpact.html
annees: 2019
description: "Simuler l'impact de réformes socio-fiscales sur les citoyen·ne·s"
administration: Direction interministérielle et du système d’information et de communication de l'Etat
administration-website: https://www.etalab.gouv.fr/qui-sommes-nous
type: Design & Développement
eigs:
  - nom: Un·e designeur·se lean UX avec un goût prononcé pour le code
  - nom: Un·e développeur·se Python/JavaScript avec un goût prononcé pour les données
mentors:
  - nom: Mauko Quiroga
    site: /communaute/2019/mauko-quiroga.html
  - nom: Sandra Chakroun
    site: /communaute/2019/sandra-chakroun.html
images:
  - /img/logo-lex-impact.png
---

La Direction Interministérielle du Numérique et du Système d’Information et de Communication de l’État ([DINSIC](https://www.numerique.gouv.fr/)) souhaite développer, avec la collaboration du Parlement, de la Cour de Comptes, et de la société civile, une application permettant de simuler, de façon simple, rapide et ouverte, l’impact de réformes socio-fiscales sur les citoyen·ne·s.

Voir le [défi LexImpact](https://speakerdeck.com/eig2018/pitch-leximpact-defi-eig3) en quelques slides.

<br/>

## LexImpact : Évaluer l’impact de réformes socio-fiscales en développant des interfaces de simulation utilisables par tous

### La problématique

Connaissez-vous l'impact de la prochaine réforme sur votre situation
personnelle ? Probablement pas et vous n'êtes pas seul. Assemblée
Nationale, Sénat et Cour des Comptes expriment régulièrement le besoin
de disposer d'un outil leur permettant de se positionner sur les
projets de loi grâce à une information indépendante sur l'effet des
textes de loi.

L'étude d’impact des réformes reste particulièrement difficile à
réaliser, en particulier lorsque les délais sont courts. Dans le
domaine fiscal, des modèles ont été développés par plusieurs
administrations (DGFiP, INSEE, DINSIC, etc.), mais leur usage est
limité, soit parce que les données ou logiciels ne sont pas ouverts,
soit parce qu'ils sont difficiles à prendre en main.

Pourtant, cette capacité à réaliser plus facilement et rapidement des
analyses d’impact apparaît comme un enjeu primordial de notre
démocratie, tant pour améliorer le processus législatif que pour des
questions de transparence et d’engagement de la société civile.

### Le défi : développer un outil accessible aux parlementaires, agents publics et à la société civile permettant d'évaluer l'impact de réformes socio-fiscales

[OpenFisca](http://openfisca.org) est un logiciel open source qui
comprend des règles de la législation socio-fiscale et permet de
réaliser des simulations sur des situations de personnes ou une
population entière. Il est en particulier utilisé par
[Etalab](https://etalab.gouv.fr), l'Incubateur
[beta.gouv.fr](https://beta.gouv.fr), l'[IPP](https://www.ipp.eu), la
[MSA](http://www.msa.fr) et l'[IDEP](https://www.idep-fr.org) mais ce
commun contributif n'est pas directement accessible à tous les types
d'utilisateurs puisqu'il requiert des compétences en code
informatique.

**LexImpact a pour ambition de rendre l'évaluation socio-fiscale permise par OpenFisca accessible à tous**.

Plusieurs axes :

* Construire une application open source permettant de réaliser de
  façon simple et rapide des simulations de réformes socio-fiscales,
  en particulier : les analyses de réformes paramétriques (changements
  d'assiettes et de taux) et d'impacts sur le revenu disponible, les
  transferts de charges, le budget de l'État et des collectivités ;
* Recueillir des données représentatives pour alimenter l'outil :
  situations de personnes, données budgétaires et financières, etc. ;
* Systématiser les tests utilisateurs avec les parlementaires,
  services administratifs et membres de la société civile ;
* Réaliser des modules pédagogiques à destination de différents types
  d'utilisateurs et développer l'usage de l'outil au sein
  d'administrations partenaires ;
* Imaginer une généralisation de l'outil à l'ensemble des réformes
  législatives.

Une grande partie des règles et des paramètres socio-fiscaux est
d'ores et déjà développée dans le modèle
[OpenFisca-France](https://fr.openfisca.org/legislation/). Des données
du budget de l'État ainsi que des données démographiques sont en accès
libre. Il reste à élaborer une base représentative de situations de
personnes et à étendre la connaissance des structures de réformes
usuelles.

Avant l'arrivée des EIG, des rencontres avec les principales
institutions partenaires - DINSIC, Assemblée Nationale, Cour des
Comptes, Sénat- permettront d'identifier les conditions d'accès aux
modèles de populations existants ou à co-construire. En parallèle, un
ensemble de cas types décrivant des situations de personnes et de
groupes de personnes sera rassemblé pour servir de base aux travaux
des EIG. Les types de réformes que l'application serait amenée à
traiter seront affinés par des entretiens utilisateurs.

<br/>

## Les EIG recherché.e.s

### EIG 1 - Un·e designeur·se / Lean UX avec un goût prononcé pour le code

**Missions principales** : prototyper l’outil, mener des tests
utilisateurs, améliorer constamment l'expérience utilisateur, assurer
la médiation avec la société civile et les partenaires du défi
(Assemblée nationale, Cour des comptes, Sénat et d'éventuels nouveaux
partenaires).

**Compétences nécessaires** : design UX, gestion de projet,
communication. Une connaissance de la fiscalité sera un plus.

### EIG 2 - Un·e développeur·se Python/JavaScript avec un goût prononcé pour les données

**Missions principales** : développer l'outil (interface utilisateur,
backend...), déployer l'outil, compiler/éditorialiser/mettre à
disposition des cas types, faire évoluer l'API Réforme d'OpenFisca
Core.

**Compétences nécessaires** : Python, JavaScript. Une connaissance de la fiscalité sera un plus.

<br/>

## L'équipe autour des EIG

### Mauko Quiroga, mentor opérationnel

![Mauko Quiroga](/img/communaute/mauko-quiroga.png)

Mauko Quiroga est un Product Manager spécialisé dans le déploiement de
services publics numériques. Depuis 2016, il s'engage dans la
construction d’un État au XXI<sup>e</sup> siècle, en tant que membre
permanent de [beta.gouv.fr](http://beta.gouv.fr). Aujourd’hui, Mauko
travaille avec l’équipe [OpenFisca](https://openfisca.org/fr/), pour
faciliter la collaboration entre le Parlement, le gouvernement et la
société civile, lors de la création de la loi. Issu d’une formation à
l'entrecroisement des sciences politiques, du génie industriel, et du
commerce, Mauko se donne avec abnégation à sa mission, d’après lui,
prométhéenne. Il est sur
[LinkedIn](https://www.linkedin.com/in/maukoquiroga/),
[Twitter](https://twitter.com/maukoquiroga) et
[Github](https://github.com/maukoquiroga).

<br/>

### Sandra Chakroun, mentor opérationnelle

![Sandra Chakroun](/img/communaute/sandra-chakroun.jpg)

Développeuse informaticienne, Sandra Chakroun est actuellement membre
de l'équipe [OpenFisca](https://openfisca.org/fr/) à la DINSIC.
Diplômée d'un Master 2 d'Informatique de l'Université Pierre & Marie
Curie ([Sorbonne Université](https://www.sorbonne-universite.fr)),
elle s'adapte aux différentes technologies de programmation
logicielle.  Elle assurera un accompagnement technique et humain pour
l'intégration des EIG dans la communauté de contributeurs à [OpenFisca
France](https://github.com/openfisca/openfisca-france/graphs/contributors).
