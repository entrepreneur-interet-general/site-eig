---
author: Antoine Augusti, EIG Link
description: "En tant qu'équipe coordination du programme, nous avons comme missions principales la constitution de promotions, l'accompagnement des entrepreneurs au fil de l'année, faire rayonner et évoluer le programme EIG. Il s'est avéré nécessaire de mettre en place une base de connaissance comportant nos événements, nos processus, diverses explications et bonnes pratiques. Nous détaillons dans cet article quels sont les objectifs de notre documentation, la démarche de construction suivie et comment nous la faisons évoluer."
image: /img/blog/doc-site.png
layout: post
tags:
- open
- méthode
- collectif
- outil
title: "Ouvrir les ressources du programme : notre documentation en ligne"
lang-ref: documentation-programme
twitter: AntoineAugusti
---

Le programme Entrepreneurs d'Intérêt Général a pour objectif de faire travailler ensemble des personnes extérieures à l'administration aux compétences numériques pointues et des agents publics engagés dans une démarche d'innovation. Les entrepreneurs d'intérêt général sont répartis en binômes ou trinômes pluridisciplinaires. Ils interviennent dans les domaines du développement, du design et de la datascience. Avec les agents publics de leurs administrations d’accueil, ils ont 10 mois pour relever un défi d'amélioration du service public à l'aide du numérique et des données. Ces défis suivent une démarche de travail ouverte et transparente, notamment par la publication de productions en open source et en open data.

Le programme comporte actuellement une trentaine d'entrepreneurs par promotion, travaillant au sein de diverses administrations comme le ministère de la Transition écologique et solidaire, la Cour des comptes ou l'agence Bio.

En tant qu'équipe coordination du programme, nous avons comme missions principales la constitution de promotions, l'accompagnement des entrepreneurs au fil de l'année et faire rayonner et évoluer le programme EIG. **Dans ce cadre, il s'est avéré nécessaire de mettre en place une base de connaissance comportant nos événements, nos processus, diverses explications et bonnes pratiques.**

Nous détaillons dans cet article quels sont les objectifs de notre documentation, la démarche de construction suivie et comment nous la faisons évoluer.


## Objectifs de notre documentation

Notre programme comporte plus de trente personnes qui travaillent dans des administrations dans plusieurs lieux géographiques. Chaque promotion a une courte durée de vie (dix mois), ce qui implique qu'il est nécessaire d'expliquer clairement les processus et les ressources à disposition lors de la phase d'accueil et d'offrir un moyen de pouvoir se rafraîchir la mémoire plus tard.

Les utilisateurs cibles de notre documentation sont les entrepreneurs d'intérêt général, leurs mentors et l'équipe de coordination au sein d'Etalab. Les entrepreneurs ont besoin de comprendre comment fonctionne le programme et d'accéder à des ressources pour mener à bien leurs défis dans leurs administrations.

Pour répondre à ces besoins, notre documentation a été scindée en trois grandes parties. Voici quelques exemples de contenu que l'on peut retrouver :



* **Le déroulement du programme** : l'accompagnement des projets, le planning d'événements de la promotion, les outils utilisés ;
* **Les ressources à disposition des EIG dans le cadre de la promotion** : l'écosystème numérique de l'administration, l'accès à un tiers lieu, la possibilité d'obtenir de l'infrastructure ;
* **Les bonnes pratiques, organisées en thématiques** : comprendre les licences libres, publier et réutiliser des données, écrire des notes stratégiques, comment pratiquer le design dans l'administration.

## Un travail collaboratif et ouvert

Notre documentation ne s'est pas construite en un jour et elle continuera d'évoluer. Ce travail a été commencé sous l'impulsion de [Bastien Guerry](https://entrepreneur-interet-general.etalab.gouv.fr/communaute/2018/bastien-guerry.html), début 2018. Bastien avait alors le rôle d'[EIG Link](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2018/eiglink.html), la personne assistant l'équipe de coordination du programme, chargée de l’accompagnement technique et méthodologique des défis. C'est lui qui a rédigé les premières pages de notre documentation en fonction des besoins et ressources identifiés au fur et à mesure. Nous ne sommes pas partis d'une page blanche, nous avons été inspirés par de nombreuses ressources disponibles, elles aussi ouvertes : [beta.gouv.fr](https://beta.gouv.fr/), [GDS](https://www.gov.uk/government/organisations/government-digital-service), le blog de [Code for Canada](https://medium.com/code-for-canada) et bien d'autres.

Conformément aux valeurs et objectifs de transparence et d'ouverture du programme, cette documentation est publiée sous licence libre [sur un dépôt Git](https://github.com/entrepreneur-interet-general/eig-link). Concrètement, notre documentation se compose de plusieurs fichiers textes écrits en [Markdown](https://fr.wikipedia.org/wiki/Markdown), un langage de balisage léger permettant d'écrire des documents textes.

Notre documentation est collaborative : elle est maintenue principalement par l'équipe de coordination du programme mais les entrepreneurs sont invités à faire part de retours et contribuer. Ainsi, nous sommes ravis de constater que la documentation comporte déjà plus de 1000 modifications effectuées par 27 contributeurs.


> C'était important de commencer le travail de documentation dès le début de l'année 2018.  Ensuite, j'ai avancé au fil de l'eau en fonction des questions des EIG ou des besoins que j'anticipais. Avec une communauté dynamique où l'entraide est la norme, c'était un vrai plaisir.

**Bastien Guerry, [EIG Link 2018](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2018/eiglink.html)**

Cette documentation ne sera jamais finalisée car elle se construit de manière itérative. Elle est rédigée au fil de l'eau, des questions reçues, des évolutions de nos processus et de nos ambitions. C'est notre moyen privilégié pour partager des informations et constituer une base de connaissance ouverte.

![Interface web de GitHub montrant plusieurs fichiers.](/img/blog/doc-github.png)
_Capture d'écran de notre documentation [sur GitHub](https://github.com/entrepreneur-interet-general/eig-link)._


## Rendre la documentation agréable à consulter pour tous

Notre documentation est constituée de plusieurs fichiers Markdown. Facile pour collaborer : les contributeurs peuvent soumettre des changements directement sur GitHub et faire approuver leurs modifications dans des _pull-requests_. Plus embêtant pour naviguer dans une documentation : avec une petite vingtaine de fichiers Markdown à la racine, il n'est pas facile de savoir par où commencer, même si un fichier README explique l'agencement de la documentation. Ce qui n'était pas un problème initialement, la communauté était principalement technique et habituée à l'interface de GitHub, s'est révélé problématique au fil du temps.

C'est la raison pour laquelle nous avons choisi de publier notre documentation sur un site spécifique, en complément des fichiers sources Markdown déjà présents sur GitHub. Nous avons l'habitude d'utiliser des sites statiques, [le site web du programme](https://entrepreneur-interet-general.etalab.gouv.fr/) repose par exemple sur [Jekyll](https://jekyllrb.com). Pour la documentation, nous nous sommes orientés vers [VuePress](https://vuepress.vuejs.org), un générateur de sites statiques idéal pour des besoins de documentation qui requiert une configuration minimale. Nous en avons profité pour créer [un thème VuePress open source](https://vuepress-gouv-fr-demo.eig-forever.org) reprenant les codes graphiques de l'administration française.


![Site web de la documentation du programme faisant apparaitre une page sur la sécurité et un menu.](/img/blog/doc-site.png)
_Capture d'écran de la documentation, accessible à l'adresse [doc.eig-forever.org](https://doc.eig-forever.org)_

Ainsi, nous disposons dorénavant d'une documentation accessible en ligne, agréable à utiliser, sur une interface adaptée aux différents écrans. En faisant ceci, nous n'avons pas introduit inutilement trop de complexité technique en terme de code ou d'infrastructure. Le plus important est que nous avons conservé la possibilité de collaborer rapidement à la documentation : à la fin, notre documentation n'est qu'un ensemble de fichiers textes basiques.


## Pistes d'évolution

Nous sommes globalement satisfaits de notre documentation qui a bien évolué au fil du temps. Les entrepreneurs ou d'autres équipes au sein d'Etalab nous ont fait part de l'utilité de celle-ci pour remplir leurs missions. Par ailleurs, cette documentation a pu être un mécanisme d'incubation pour des guides plus étoffés ensuite publiés par Etalab ou la DINSIC, notamment autour des questions de publications de logiciels libres, d'algorithmes ou de données.

Pour les mois à venir, nous souhaitons continuer à travailler sur le contenu existant, réorganiser nos différentes sections et publier des contenus pour ceux souhaitant répliquer un programme similaire au programme Entrepreneurs d'Intérêt Général dans une autre structure ou un autre contexte.

Nous avons hâte de continuer à étoffer cette documentation. Nous serions heureux qu'elle profite à d'autres. Si vous souhaitez échanger sur cette initiative, nous serions ravis [d'en discuter avec vous](https://entrepreneur-interet-general.etalab.gouv.fr/contact.html).
