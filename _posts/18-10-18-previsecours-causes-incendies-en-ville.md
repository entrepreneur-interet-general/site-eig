---
author: Guillaume Lancrenon, EIG Prévisecours
description: Guillaume est développeur au Ministère de l'Intérieur pour le défi Prévisecours.
  Il nous explique comment son équipe a travaillé pour déterminer les facteurs les
  plus corrélés avec le volume d'incendies urbains dans les différentes communes d'Essonne.
image: /img/communaute/Guillaume-Lancrenon.png
layout: post
tags:
- témoignage
- réalisation
- datascience
title: Comment prédire les incendies en ville ?
twitter: etalab
---

## Incendies en ville : quelles causes probables ?

![Portrait de Guillaume](/img/communaute/Guillaume-Lancrenon.png)
_Guillaume Lancrenon, développeur, Entrepreneur d'intérêt général pour le défi Prévisecours_

Depuis janvier 2018, je travaille avec Tiphaine Phe-Neau sur le défi
[Prévisecours](https://previsecours.fr), au service des
sapeurs-pompiers.  Ce défi fait partie du programme d’Etalab
« Entrepreneur.e d'intérêt général » et il est porté par le ministère
de l'Intérieur.  L’objectif est simple : créer des algorithmes de
prédictions d’intervention pour aider les pompiers de l’Essonne à
mieux anticiper les ressources humaines et matérielles à mobiliser au
quotidien.

Nous travaillons sur tous les types d’interventions dont les
principaux sont : le secours aux personnes, les incendies et enfin les
accidents. Dans cet article, pour plus de concision, nous allons nous
concentrer sur les **incendies urbains**.

### Reconstituer l'iceberg des facteurs potentiels

Pour faire nos prédictions, nous devions déterminer les facteurs qui
sont les plus corrélés avec le volume d’intervention des
pompiers. Bonne nouvelle, nous disposions déjà de leur
historique. Mauvaise nouvelle : nous n'avons rien d’autre. La question
centrale était donc : **quelles données allions-nous associer à celles
des pompiers ? Autrement dit, quels facteurs pourraient être corrélés
avec le nombre d’interventions des sapeurs pompiers ?**

Pour répondre à cette question, nous avions nos intuitions : la pluie,
la pollution… Mais cela ne touchait que la partie émergée de
l’iceberg. Ce que j’appelle l’iceberg, c’est l’ensemble des facteurs
corrélés avec les interventions des pompiers. La partie émergée est
donc l’ensemble des facteurs intuitifs, ceux qui auxquels on pense
sans même être pompier.

La partie _immergée_ de cet iceberg est difficilement accessible, car
on n'y pense pas d'emblée. **Pour y accéder, et donc avoir l'idée que
tel ou tel facteur pourrait avoir un impact, nous avons dialogué avec
des pompiers de certaines casernes de l’Essonne (1)**. Suite à ça,
nous avions de nombreuses pistes à explorer. Il a fallu trouver des
sources, ces personnes qui produisent la donnée recherchée (merci !
(2)). Puis, nous avons intégré, travaillé et préparé ces
données. Finalement, après des mois de travail, nous avons constitué
**une base de données d’environ 200 facteurs : notre gros glaçon**.

**L’iceberg est dorénavant composé de données très variées :**

- données calendaires (jours féries, fêtes religieuses, vacances,
  soldes, phases de la lune...) ;
- données de pollution de l’air (NO2, O3, PM10) ;
- données allergènes type pollen (graminées, cumul de taxons, etc.) ;
- données météo (humidité, précipitation, pression atmosphérique,
  température, vent, durée moyenne du jour) ;
- données épidémiques (diarrhée, grippe, varicelle) ;
- données sur les incivilités (certains types d'infractions) ;
- données sur la population (tranches d'âge, constitution des foyers,
  scolarisation, diplôme, profession, idh2 – indice de développement
  humain, couverture RSA, etc.) ;
- données sur la commune (présence d’établissements sociaux, de soins,
  etc.) ;
- données sur le transport (gares, trafic cumulé, terminus de ligne).

### Les facteurs en lien avec les caractéristiques des communes sont très corrélés avec le volume d'incendies urbains

Nous avons ensuite confronté ces facteurs aux interventions des
pompiers.  Ceux qui sont les plus corrélés avec nos interventions sont
présentés ici :

![Liste des facteurs corrélés avec les incendies urbains, dans l'ordre décroissant : le nombre d'opérations des sapeurs-pompiers lors des dernières semaines et années, le nombre de naissances à l'année, le nombre d'infractions mensuelles, la population, le nombre de décès à l'année, la proportion des ménages à bas revenus, le taux de foyers allocataires dont les ressources sont constituées à 50% ou plus des prestations CAF, les gares ferroviaires avec plus de trafic que la médiane du département. Liste des facteurs anti-corrélés avec les incendies urbains, dans l'ordre croissant : la proportion de ménages dont la personne de référence est Artisan, Commerçant, Chef d'entreprise, la proportion de familles sans enfant, la proportion de la population dans la tranche d'âge 55-79 ans, l'indicateur idh2](/img/blog/facteurs-incendies.png)
_À noter : l'[IDH2 (indicateur de développement humain 2)](https://www.insee.fr/fr/statistiques/fichier/2114265/lm_ind_02_C-7.pdf) est un indicateur élaboré par l'INSEE, qui réunit les trois dimensions de l'IDH original (santé, éducation, revenu) et des données spécifiques à la situation française._

La première ligne représente le nombre d’interventions réalisées par
les pompiers lors des dernières semaines et années. C’est le facteur
le plus corrélé avec les interventions des pompiers… comme on pouvait
s’y attendre, l’historique des interventions est prédominant. Les sept
lignes suivantes représentent les facteurs les plus corrélés, et enfin
les quatre derniers facteurs représentent les plus anti-corrélés.

L’objectif ici n’est pas d'interpréter les raisons de ces
corrélations. On peut cependant remarquer que pour le département de
l’Essonne, les facteurs météorologiques ne sont pas les plus corrélés
aux incendies urbains. Les facteurs majeurs sont ceux qui décrivent
les communes et leurs populations, comme la natalité ou les
revenus. Or, ces facteurs restent relativement stables de semaine en
semaine. La connaissance d’une commune seule (peu importe la météo)
permet donc de savoir si c’est un foyer propice aux incendies urbains
ou non.

### Vous voulez en savoir plus ou participer à ce projet ?

Consultez notre site web : [Prévisecours](https://previsecours.fr).
Et puisque nous sommes toujours en train de travailler sur ce projet,
si vous avez des idées de données à intégrer, nous serions ravis que
vous nous en fassiez part à l'adresse suivante :
[guillaume.lancrenon@interieur.gouv.fr](mailto:guillaume.lancrenon@interieur.gouv.fr)

Nous espérons vous lire !

[Guillaume Lancrenon](https://entrepreneur-interet-general.etalab.gouv.fr/communaute/2018/guillaume-lancrenon.html), Développeur au Ministère de l’Intérieur pour le défi Prévisecours, Entrepreneur d’Intérêt Général

<hr/>

PS : Pour ceux qui souhaitent aller plus loin, la corrélation
statistique utilisée est celle de Pearson. La maille temporelle
utilisée est celle de la semaine. Écrivez-nous pour plus
d’information.

(1) Merci aux pompiers des casernes de Viry, Étampes, Corbeil-Essonnes
et d’Évry pour leur accueil.

(2) Merci à nos partenaires pour la mise à disposition de leurs
données : Météo France, Le réseau sentinelle, l’INSEE, La région île
de France, data.gouv.fr, Air Parif, la FINESS, Le RNSA, La SSMSI, la
CAF, La SNCF, Le STIFF, et le SDIS91.
