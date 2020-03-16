---
author: Jean-Baptiste Le Dévéhat, EIG Link
description: "Les experts en accessibilité numérique, Jamshid Kohandel et Fernando Pinto da Silva vous montrent comment un aveugle navigue depuis son ordinateur et depuis son smartphone sur des sites internet et applications. Ce que vous découvrirez : les outils et les gestes de navigation, les erreurs de conception les plus fréquentes, l'importance de concevoir des services numériques réellement accessibles à tous."
image: /img/blog/demo-a11y-20190404.jpeg
layout: post
tags:
- design
- écosystème
title: "Démonstrations : comment un aveugle navigue sur le web ?"
twitter: jbledevehat
---

## Qu'est-ce que l'accessibilité ?
 
L'accessibilité est un droit, défini par la possibilité pour un citoyen d'avoir accès à ce dont il a besoin. Cette notion d'accessibilité est généralement utilisée pour les personnes en situation de handicap et concerne de nombreux domaines, comme par exemple l'accessibilité physique ou l'accessibilité éducative... L'accessibilité numérique est l'adaptation des systèmes numériques, notamment des sites web, aux différents types de handicap et aux outils utilisés par les personnes en situation de handicap tels que le lecteur d'écran et l'afficheur braille. 

> D'après une [enquête de l'INSEE de 2007](https://www.insee.fr/fr/statistiques/1373648?sommaire=1373710), les personnes en situation de handicap en France représentent 9,6 millions de citoyens.


## L'État français s'engage pour l'accessibilité

Depuis 20 ans, l'État pousse les sujets d'accessibilité :
- [en 1999, il publie une circulaire qui recommande que les sites publics soient accessibles à tous](https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000000213936&categorieLien=id), en particulier aux personnes en situation de handicap grâce au respect des recommandations de la [« Web Accessibility Initiative »](https://www.w3.org/WAI/) (WAI) du World Wide Web Consortium (W3C) ;
- en 2009, il introduit le [Référentiel général d'accessibilité pour les administrations (RGAA)](https://references.modernisation.gouv.fr/rgaa-accessibilite/) qui présente les modalités techniques de mise en œuvre de l'accessibilité numérique devenue obligatoire avec [la loi handicap de 2005](https://www.legifrance.gouv.fr/affichTexteArticle.do?idArticle=LEGIARTI000037388867&cidTexte=LEGITEXT000006051257) ; 
- en 2016, il demande aux administrations, dans la [loi pour une République numérique](https://www.legifrance.gouv.fr/eli/loi/2016/10/7/ECFI1524250L/jo/texte), de rendre compte de leurs actions d'amélioration de l'accessibilité numérique avec des plans d'actions annuels qui incluent les actions de sensibilisation et de formation.

L'accessibilité n'est plus une option, elle est un fil conducteur à intégrer dans chaque projet. 

Au sein de la DINSIC, l'équipe Qualité des services en ligne produit de nombreuses ressources comme les [10 principes d'une démarche exemplaire](https://www.numerique.gouv.fr/publications/dix-principes/) ou les labels [e-accessible](http://references.modernisation.gouv.fr/e-accessible) et [cerfa numérique](http://references.modernisation.gouv.fr/cerfa-numerique). C'est pourquoi l'équipe Qualité des services a été présentée aux entrepreneurs d'intérêt général (EIG) lors de [leur bootcamp](https://entrepreneur-interet-general.etalab.gouv.fr/blog/2019/03/12/bootcamp-eig3.html). Les EIG sont des data scientists, designers, développeuses et développeurs qui travaillent pendant 10 mois en équipes pluridisciplinaires de 2 ou 3 pour relever des défis d'amélioration du service public à l'aide du numérique et des données. L'objectif était de sensibiliser au maximum ces professionnels du numérique aux enjeux de l'accessibilité. 


## Deux démonstrations pour comprendre les enjeux de l'accessibilité

Avec le département Qualité des services en ligne, nous avons organisé deux démonstrations qui avaient une finalité pédagogique : comprendre comment un non-voyant utilise son ordinateur et son smartphone pour naviguer sur un site web.

Initialement destinées aux EIG, ces démonstrations ont suscité beaucoup d'intérêt et ont donc été ouvertes aux membres de la [communauté UX](https://www.numerique.gouv.fr/actualites/rejoignez-la-communaute-ux-services-publics-en-ligne/) et de la [communauté Qualité web](https://www.modernisation.gouv.fr/le-hub-des-communautes/qualite-des-demarches-en-ligne-et-accessibilite-numerique). Chaque démonstration a été filmée et _livetwittée_, vous pouvez donc les regarder ou les revoir. Elles durent environ 30 min et sont suivies d'un temps de questions-réponses qui témoignent des étonnements du public.

![Un homme est assis face à une assemblée de 30 personnes. Derrière lui, la plateforme data.gouv.fr est projetée sur le mur.](/img/blog/demo-a11y-20190404.jpeg) _Jamshid Kohandel navigue sur la plateforme [data.gouv.fr](https://data.gouv.fr)_


### 1. Démonstration sur ordinateur - plateforme data.gouv.fr 

La première démonstration a été réalisée par Jamshid Kohandel, expert accessibilité et non-voyant. 

Pour commencer, il faut comprendre que **les aveugles travaillent sur un ordinateur grâce à un logiciel que l'on nomme un lecteur d'écran**. Le logiciel restitue les informations visibles à l'écran à travers une synthèse vocale et/ou un lecteur braille. Le lecteur d'écran retranscrit également la nature de l'élément en cours de consultation. Par exemple, il indique s'il s'agit d'un lien, d'un bouton ou d'une case à cocher. Le lecteur d'écran lit donc dans le code source et intéprète les types de composants. Par conséquent, si un titre est visible uniquement par l'augmentation de la taille de ses caractères, il ne sera pas accessible facilement. Alors que s'il est borné par les balise `<h2>` et `</h2>`il sera repéré rapidement et facilitera la compréhension du contenu.

Autre point important, pour naviguer sur un ordinateur, **un aveugle n'utilise pas sa souris**. La navigation passe alors exclusivement par des commandes du clavier, comme par exemple les flèches ou la tabulation. Cela conditionne les stratégies de navigation et de recherche de contenus, comme nous avons pu le voir en naviguant sur la plateforme [data.gouv.fr](https://www.data.gouv.fr/). 
Par exemple, la recherche plein texte sur l'ensemble du contenu de la page est un mode de navigation exhaustif mais long et fastidieux. Le mode de navigation par titres permet de découvrir tous les titres et de comprendre la hiérarchisation de l'information. Il existe aussi d'autres stratégies de navigation comme la recherche par liens, par boutons ou par champs de saisie de la page. Ce dernier permet bien souvent d'obtenir un accès au moteur de recherche du site.

<blockquote class="twitter-tweet"><p lang="fr" dir="ltr">🔴 Démo <a href="https://twitter.com/hashtag/accessibilit%C3%A9?src=hash&amp;ref_src=twsrc%5Etfw">#accessibilité</a> web à la DINSIC par notre expert Jamshid Kohandel#a11y <a href="https://t.co/D3YNk6IyZo">https://t.co/D3YNk6IyZo</a></p>&mdash; _DINSIC (@_DINSIC) <a href="https://twitter.com/_DINSIC/status/1113729821161295872?ref_src=twsrc%5Etfw">April 4, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
 _Cliquez sur le tweet pour revoir la démonstration de Jamshid_

Nous avons ensuite cherché un jeu de donnée, un fichier Excel que nous avons pu télécharger et analyser. A la fin de cette première démonstration, une nouvelle question a émergé : comment un non-voyant navigue en ligne sur son mobile ?

### 2. Démonstration sur mobile - Ameli, Tchap... 

Lors de la seconde démonstration, Jamshid était accompagné de Fernando Pinto da Silva également expert en accessibilité numérique et non-voyant. 

Pour la démonstration, ils ont utilisés un iPhone et le lecteur d'écran VoiceOver intégré au système d'exploitation MacOs (pour Android, il y a le lecteur d'écran TalkBack). Un utilisateur lambda qui navigue sur son smartphone déclenche une action à chaque fois qu'il touche un élément sur son écran. **Un aveugle utilise le lecteur d'écran pour décrire tout ce qu'il touche.** Il utilise ensuite des gestes supplémentaires pour déclencher une action. Il s'agit là du premier enseignement de la démonstration.

<iframe frameborder="0" width="100%" height="480" src="https://www.dailymotion.com/embed/video/x7h7en4" allowfullscreen="" allow="autoplay"></iframe>
_(Re)regardez la démonstration de navigation sur mobile grâce à la vidéo ci-dessus_

Deuxième enseignement : **il existe entre 50 et 60 gestuelles de navigation avec le lecteur d'écran sur mobile**. La démonstration a permis d'en découvrir quelques unes comme par exemple : 
- le balayage horizontal vers la droite ou la gauche pour aller respectivement vers l'élément suivant ou précédent ;
- la double tape sur l'écran pour ouvrir un dossier ou une application ;
- le mouvement circulaire avec deux doigts sur l’écran, comme si l'on souhaitait remonter une vieille horloge, pour sélectionner une option.

Enfin, **il est également possible de connecter un lecteur en braille nommé "plage braille"** (en bluetooth) afin de naviguer sur son mobile. Fernando a ainsi pu ouvrir l'application Ameli à travers sa plage braille, en désactivant la voix. Ce dispositif est utile par exemple pour les personnes sourdes-aveugles.

**Application Ameli**

Dans le cadre de la démonstration nous avons pu ouvrir l'[application Ameli](https://apps.apple.com/fr/app/ameli-lassurance-maladie/id620447173) afin de comprendre ce qui était accessible et ce qui ne l'était pas. Nous avons pu observer un bouton sans label, nous questionnant sur l'utilité de celui-ci. Nous avons aussi visualisé un champ de texte décrit comme étant à saisir (malheureusement il ne l'était). Enfin, le lecteur d'écran a détecté un bouton "Dashboard menu BTN white", ne nous offrant ainsi aucune aide à la navigation.

**Application Tchap**

Jamshid nous a ensuite présenté l'[application Tchap](https://www.tchap.gouv.fr/). Dans la navigation, nous avons observé quelques éléments mal décrits ou même non définis, laissant planer rapidement un doute sur les actions à réaliser. Ensuite nous avons pu échanger des messages sur l'application Tchap, nous permettant de comprendre comment les aveugles utilisent le clavier virtuel du smartphone (cf. vidéo ci-dessus).

### Au-delà de l'accessibilité numérique, le numérique comme outil d'accessibilité

Jamshid nous a également présenté l'application [Scanner](https://apps.apple.com/us/app/scanner/id1291962681https://apps.apple.com/us/app/scanner/id1291962681). Celle-ci permet de prendre en photo une page contenant du texte. Le texte est ensuite lu par la synthèse vocale ce qui permet, par exemple, de lire l'addition d'un restaurant ou un courrier administratif.

Enfin, Jamshid nous a présenté l'application [BlindSquare](https://apps.apple.com/fr/app/blindsquare/id500557255). Cette application a été conçue pour les aveugles afin de connaître tout ce qui se situe dans leur environnement immédiat (restaurant, parc, musée, boutique...). Couplée à une application de navigation (Maps ou Plan), elle permet à Jamshid de se déplacer au quotidien.

## Voir l'inaccessible

L'observation de l'utilisateur, afin de comprendre son expérience particulière et ses usages, est riche d'enseignement ; pour nous concepteur, ces démonstrations ont permis d'appréhender les difficultés et les bonnes pratiques d'accessibilité, mais aussi d'utilisabilité, de nos interfaces. Nous vérifions trop souvent nos sites dans notre propre contexte : il est indispensable de se décentrer !

Par ailleurs, l'accessibilité numérique semble être un domaine chargé de normes et de règles techniques. En réalité, elle définit uniquement ce qui doit être produit par les concepteurs et les développeurs web selon un standard et demande de la rigueur.

En un mot, nous vous recommandons fortement d'organiser cette démonstration pour sensibiliser vos concepteurs et  vos développeurs aux enjeux des normes d'accessibilité ! 

Pour organiser une démonstration dans votre administration, vous pouvez prendre contact avec l'équipe [Qualité des services en ligne](http://references.modernisation.gouv.fr/contact-rgaa).
