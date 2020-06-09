---
author: Antoine Augusti, EIG Link
description: Afin de partager et de suivre l'avancement des différents défis relevés
  par une trentaine de personnes au sein du programme Entrepreneurs d'Intérêt Général,
  nous avons développé un outil de rétrospective hebdomadaire, Bulletins, que nous
  présentons dans cet article.
image: /img/blog/bulletins-form.png
layout: post
tags:
- réalisation
- open
- accompagnement
title: 'Bulletins : notre outil open source de rétrospective hebdomadaire'
lang-ref: bulletins-form
twitter: AntoineAugusti
---

Accompagner une trentaine de professionnels du numérique au sein de 15 défis dans autant d'administrations réparties dans différents lieux : c'est la mission que relève au quotidien l'équipe du programme Entrepreneurs d'Intérêt Général (EIG). Pluridisciplinaire, l'équipe appuie entrepreneurs d'intérêt général et mentors sur des aspects variés de leurs défis : stratégie, technique, gestion de projet, évaluation, communication, etc.

Nous vous partageons un des moyens de communication que nous avons mis en place pour mener à bien notre mission d'accompagnement : **la rétrospective hebdomadaire**.

## Notre problématique : partager l'avancement de plusieurs défis

L'équipe du programme EIG est en capacité de suivre l'avancement de chaque défi de manière hebdomadaire par le biais de personnes référentes, mais les autres défis non. Pour pallier cette asymétrie d'informations, nous avions besoin d'un outil qui permette de :

- partager sa rétrospective hebdomadaire de manière asynchrone ;
- archiver les rétrospectives ;
- faciliter la lecture des autres rétrospectives (les autres défis se déroulant dans d'autres administrations, ceci ne laisse la place qu'à un court temps d'attention).

## Alternatives envisagées

Pour répondre à ce besoin de circulation de l'information entre équipes, on organise souvent des réunions de suivi hebdomadaires, aussi appelées « stand-up meetings ». Les stand-up sont des réunions durant lesquels plusieurs personnes se réunissent au même endroit, au même moment, pour dire à tour de rôle ce sur quoi elles travaillent. Ce sont des points d’étapes récurrents, qui servent à faire circuler des informations au sein d’une équipe.

Problème : les stand-up demandent à plusieurs personnes d’interrompre leur travail respectif au même moment pour absorber des informations qui ne leur seront sans doute pas utiles au même moment. Par ailleurs, nos équipes sont dans des lieux de travail différents et n'ont pas un besoin crucial de connaître l’avancement des autres défis pour mener à bien leurs tâches. Enfin, la tenue d'une rétrospective via un outil de communication en ligne (vidéo ou conversation instantanée) ne permet pas de véritablement être asynchrone ni de proposer un archivage efficace.

Il était donc crucial que l'outil soit **asynchrone, rapide à utiliser et qu'il propose une consultation rapide des rétrospectives des collègues**.

## Solution retenue

Nous n'avons pas trouvé d'outil se rapprochant de notre besoin sur le marché et nous avons évalué que le développement d'un tel outil prendrait quelques jours. C'est ainsi que j'ai créé [Bulletins](https://bulletins.eig-forever.org), notre outil de rétrospective hebdomadaire, disponible en tant que logiciel open source.

Au lieu d’interrompre le travail de tout le monde, notre outil permet à chaque équipe de faire un bilan écrit de la semaine écoulée. Les rétrospectives sont saisies dans un formulaire, que chaque équipe remplit quand bon lui semble — du moment qu’elle le remplit à temps. Une fois renseignées, les rétrospectives sont ensuite agrégées dans un e-mail qui est envoyé à tout le monde, et que chacun peut lire quand bon lui semble. Les informations circulent ainsi sans nécessiter de réunion.

![Formulaire web permettant de remplir sa rétrospective hebdomadaire](/img/blog/bulletins-form.png)_Capture d'écran du formulaire de la rétrospective hebdomadaire_

![Interface web permettant la consultation des précédentes rétrospectives](/img/blog/bulletins-history.png)_Capture d'écran de la consultation des précédentes rétrospectives d'un projet_

Nous avons longuement réfléchi aux questions à poser et nous nous sommes arrêtés sur les questions suivantes :
- quel est votre état d'esprit ?
- quelle a été votre priorité de la semaine ?
- qu'est-ce qui a fonctionné et qu'est-ce qui était plus difficile ?
- avez-vous besoin d'aide pour surmonter une difficulté ?

Ces questions vont droit au but et permettent un partage efficace d'informations tout en laissant la place aux opportunités de collaborations.

## Fonctionnement

Son fonctionnement est le suivant :

- Chaque équipe renseigne sa rétrospective de la semaine en complétant le formulaire de suivi, à raison d’une rétrospective par équipe ;
- Les rétrospectives saisies sont agrégées dans un e-mail qui est envoyé automatiquement chaque vendredi à 15 heures.

Les réponses saisies dans le formulaire de l'application ne sont pas publiques. Toutefois, ces informations sont utiles pour chaque équipe : c'est pourquoi il est possible d'accéder à un historique des rétrospectives, partager les rétrospectives à l'aide d'un lien unique et d'exporter les données.

## Un outil générique et open source

La problématique de partage d'informations entre équipes ou projets est récurrente. Avec [Bulletins](https://bulletins.eig-forever.org), nous sommes heureux d'avoir à notre disposition un outil simple, efficace de suivi hebdomadaire et qui correspond à notre vision.

Grâce à Bulletins, nous avons réussi à impliquer une trentaine de personnes de manière hebdomadaire. L'équipe de coordination dispose désormais d'un outil précieux pour suivre l'avancement de chacun. Nous l'utilisons en complément d'autres outils, comme la discussion instantanée, où nous commentons régulièrement les rétrospectives.

Des collègues de la DINSIC sont en train d'envisager l'utilisation de cet outil ; nous serions heureux que vous en fassiez de même. Bulletins est open source et disponible en français ou en anglais pour démultiplier le potentiel d'utilisation. Vous pouvez consulter [sa documentation en ligne](https://bulletins.eig-forever.org). Si vous avez des questions, nous serons ravis d'échanger avec vous [sur GitHub](https://github.com/entrepreneur-interet-general/bulletins) ou par e-mail à l'adresse <entrepreneur-interet-general@data.gouv.fr>.
