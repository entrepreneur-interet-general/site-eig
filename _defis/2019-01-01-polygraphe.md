---
layout: defi
title: PolyGraphe
---

[La Direction générale de la concurrence, de la consommation
et de la répression des fraudes (DGCCRF)](https://www.economie.gouv.fr/dgccrf)
souhaite développer des nouvelles méthodes de text mining, d’analyse de données et de
comportements pour aider les enquêteurs de sa direction à mieux
détecter et qualifier des faux avis sur les plateformes de
consommation en ligne.

Voir le [défi PolyGraphe](https://speakerdeck.com/eig2018/pitch-polygraphe-defi-eig3) en quelques slides.

<br/>

## PolyGraphe : Détecter les faux avis pour garantir la confiance sur Internet

### La problématique

Les informations disponibles sur Internet orientent considérablement
les choix des consommateurs. Selon une étude IFOP, 85% des
consommateurs sont influencés par les avis laissés en ligne sur les
produits ou les services en vente.

Les faux avis trompent les consommateurs qui tiennent compte des
commentaires laissés en ligne pour guider leur acte d’achat. Ils
nuisent également aux professionnels vertueux en empêchant une
concurrence loyale.

La [Direction Générale de la Concurrence, Consommation et Répression
des Fraudes (DGCCRF)](https://www.economie.gouv.fr/dgccrf) effectue chaque année des enquêtes sur cette
thématique. Afin de lutter plus efficacement contre cette pratique,
elle souhaite se doter d’un outil permettant de détecter les avis
suspects sur Internet. Cet outil a vocation à être utilisé par les
agents en charge des enquêtes sur ce sujet.

### Le défi : développer un outil permettant de détecter les avis suspects parmi les commentaires, notes ou autres évaluations disponibles publiquement sur Internet

Le défi se décompose en trois axes principaux :

* **La récupération des données pertinentes sur des plateformes web
  proposant des avis de consommateurs** : texte du commentaire,
  informations sur l’entreprise ou produit faisant l’objet de l’avis,
  note attribuée, informations sur l’utilisateur ayant posté l’avis,
  etc.

* **L’analyse des données extraites pour identifier les commentaires
  suspects** à l’aide de différents indicateurs de suspicion définis
  avec les enquêteurs expérimentés sur ce sujet.

* **La visualisation des résultats sous forme d’une interface à
  destination des enquêteurs.**

_La DGCCRF a réalisé une analyse préliminaire en interne, et une preuve
de concept est en cours auprès d’un prestataire externe et avec les équipes d'Etalab. Les EIG
auront donc une base de travail et des données disponibles dès leur
arrivée._

<br/>

## Les EIG

### [Gabriel Bastard](/communaute/2019/gabriel-bastard.html), data scientist

**Missions principales** : définition de métriques à partir des
indicateurs de suspicion, élaboration d’algorithmes pour l’agrégation
des indicateurs (apprentissage non supervisé), mise en place de
l’apprentissage supervisé dans un second temps si cela s’avère
pertinent, text mining pour l’analyse du texte des
commentaires. 

**Compétences** : text mining, techniques d'apprentissage, 
maîtrise de Python et R.

### [Luc Salommez](/communaute/2019/luc-salommez.html), développeur

**Missions principales** : développement d’une application pour
l’extraction et l’exploration des données web (en partenariat étroit
avec la·e datascientist·e), la visualisation des données (indicateurs…)
via un tableau de bord interactif, en partenariat avec le service
informatique de la DGCCRF et les futurs utilisateurs.

**Compétences nécessaires** : maîtrise de Python, HTML/CSS/JavaScript, et éventuellement C#.

<br/>

## L'équipe autour des EIG

### Audrey Istace, mentor opérationnelle

![Audrey Istace](/img/communaute/audrey-istace.png)

**Audrey Istace est inspecteur à la DGCCRF**. Elle
travaille au service national des enquêtes, au sein d’une équipe
dédiée aux techniques d’investigations numériques : développement
d’outils pour cibler des pratiques suspectes, analyse de bases de
données d’entreprise pour mettre en évidence des fraudes, etc.

_"L’objectif de ce défi est, d’une part, de lutter plus efficacement
contre les faux avis et leurs conséquences en orientant les contrôles
et, d’autre part, de permettre une plus grande responsabilisation des
acteurs. Détecter et mettre en lumière que les plateformes sont le
support de pratiques illicites doit les inciter à accroitre
l’efficacité de leurs politiques et actions de vérifications et ainsi
contribuer à y mettre fin._

_Accueillir des EIG représente pour nous l’occasion de monter en
compétence en travaillant à leur côté et d’approfondir la démarche
actuelle de développement de la data science à la DGCCRF._"
