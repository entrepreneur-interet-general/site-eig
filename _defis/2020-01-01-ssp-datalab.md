---
layout: defi
title: "SSP Datalab"
---

L’Insee en tant que coordinateur du service statistique public (SSP) souhaite développer une plateforme ergonomique de traitement des données statistiques afin de rendre les techniques modernes plus accessibles et de mutualiser les efforts pour répondre aux défis actuels de la statistique publique.

## La problématique : des outils et techniques de traitement de données difficiles d’accès et dépourvus d’environnements de test

Le service statistique public est composé de 16 services statistiques ministériels et de l’Insee (Institut national de la statistique et des études économiques) qui en assure la coordination.

Dans le contexte informationnel actuel, l’Insee est confronté à de multiples enjeux : Comment continuer à exercer la mission d’éclairage du débat public en étant plus précis, plus réactif, sur les thématiques actuelles et émergentes ? Comment être efficace dans la coordination de 16 services de statistique sans disposer d’infrastructure mutualisée ?

L’enjeu est donc d’innover dans les méthodes de traitement et d’exploitation des données à travers une plateforme mutualisée, ergonomique, sécurisée et accessible à distance.

## Le défi : créer un cloud spécialisé dans les outils et techniques de traitement de données, à l’état de l’art et accessible à un public varié

Le défi consiste à créer une plateforme de centralisation d’outils de traitement de données et une communauté d’échange de bonnes pratiques à destination des services statistiques publics. 

Une [version provisoire de la plateforme](https://spyrales.sspcloud.fr/accueil) a été mise en production en mars en soutien d’une communauté de statisticiens de l’État. Cette ouverture a permis de lancer une dynamique d’amélioration fondée sur la mise à l’épreuve rapide par les utilisateurs pour proposer des modifications pertinentes. 

La plateforme repose sur l’assemblage de technologies open source et cloud native : un stockage objet pour le datalake (minIO), des services déployables à la demande (Rstudio, Jupyter) avec un orchestrateur de conteneurs (marathon et kubernetes), et des outils de gestion de la sécurité (Vault, Keycloak).

Le défi se focalisera sur l’amélioration : 
- du **design de l’offre** pour faciliter l’expérience utilisateur ; 
- des **services de stockage et de traitement** de données ;
- de **l’accompagnement** des utilisateurs dans leurs démarches d’appropriation et d’amélioration de la plateforme. 

La création d’une communauté de pratiques est un axe essentiel du défi. L’ambition de cette offre de service est d’améliorer  la qualité des traitements de données grâce à un partage des bonnes pratiques au sein du service statistique public.
