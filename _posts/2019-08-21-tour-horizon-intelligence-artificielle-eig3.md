---
author: Antoine Augusti, EIG Link
description: "Le programme Entrepreneurs d’Intérêt Général fait la part belle à la circulation des données et à leur exploitation. Pour la troisième promotion, 11 défis sur 15, portés par plusieurs administrations et portant sur des thématiques variées, expérimentent des techniques de pointe en intelligence artificielle. Nous vous présentons ici quelques cas d’usage de ces méthodes au sein de l’administration."
image: /img/blog/seminaire-2019/moteurs-regles.jpg
layout: post
tags:
- datascience
- open
- collectif
title: "Tour d’horizon des méthodes d’intelligence artificielle utilisées dans les défis EIG 3"
twitter: AntoineAugusti
---

Le programme Entrepreneurs d’Intérêt Général fait la part belle à la circulation des données et à leur exploitation. Pour la troisième promotion, 11 défis sur 15, portés par plusieurs administrations et portant sur des thématiques variées, expérimentent des techniques de pointe en intelligence artificielle. Nous vous présentons ici quelques cas d’usage de ces méthodes au sein de l’administration.


## Le programme EIG : une opportunité d'expérimentation pour l'administration


### Qu’est-ce que le programme EIG ? 

Le programme Entrepreneurs d'Intérêt Général est porté par Etalab, service du premier ministre qui ouvre et valorise les données publiques. Il a pour objectif de faire travailler ensemble des personnes extérieures à l'administration aux compétences numériques pointues et des agents publics engagés dans une démarche d'innovation. Les entrepreneurs d'intérêt général sont répartis en binômes ou trinômes pluridisciplinaires. Avec leurs mentors, ils ont 10 mois pour relever un défi d’amélioration du service public à l’aide du numérique et des données.


### Faire de l’intelligence artificielle dans l’administration 

Dans la quasi totalité des administrations, [les défis data science du programme EIG](https://entrepreneur-interet-general.etalab.gouv.fr/defis.html) sont une opportunité pour les administrations d'expérimenter des projets reposant sur l'exploitation de données. C’est pourquoi les entrepreneurs ont rencontré plusieurs difficultés : devoir expliquer leur métier, devoir exposer les limites et les prérequis pour appliquer des méthodes d'intelligence artificielle, travailler avec peu de données ou des données difficilement exploitables, ne pas disposer tout de suite d’un environnement de travail propice à la pratique de la data science (développement local et serveurs). Pour surmonter ces difficultés, les entrepreneurs ont organisé plusieurs [présentations de vulgarisation](https://speakerdeck.com/eig2018/vulgarisation-data-science) et mené des formations à destination des agents. Ils ont également rédigé plusieurs notes à destination de leur hiérarchie pour lever des freins ou saisir des opportunités. Grâce à cela ils ont pu implémenter des méthodes d’intelligence artificielle dont voici quelques cas d’usage.

![3 hommes travaillent ensemble autour d'un ordinateur.](/img/blog/seminaire-2019/moteurs-regles.jpg) _[Gabriel Bastard](/communaute/2019/gabriel-bastard.html), [Quentin Loridant](/communaute/2019/quentin-loridant.html) et [Antoine Augusti](/communaute/2018/antoine-augusti.html) échangent sur les moteurs de règles_

## Le traitement automatique du langage au service de la justice et du code du travail

Deux défis sont liés à la justice : [Open Justice](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/openjustice.html) et [DataJust](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/datajust.html). Le premier oeuvre pour ouvrir la jurisprudence par la pseudonymisation des données et le second vise à construire un référentiel d'indemnisation des préjudices corporels. [ExploCode](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/explocode.html) s'attache à rendre le droit du travail lisible, accessible et compréhensible. Ces défis utilisent des algorithmes de traitement automatique du langage (_natural language processing_). Les deux premiers s’appuient sur les décisions de justice tandis que le défi ExploCode traite des documents législatifs, des conventions, des accords de branches et des questions/réponses concernant le droit du travail.

Un enjeu pour ces défis est de reconnaître des entités nommées (_named-entity recognition_) afin de pseudonymiser les données ou de réaliser des tâches de classification (regrouper des préjudices corporels ou des thématiques du droit du travail). Pour accomplir ces tâches, les EIG utilisent des avancées récentes du domaine, notamment les méthodes de [Flair embeddings](https://github.com/zalandoresearch/flair), [ELMo](https://allennlp.org/elmo)(_Embeddings from Language_) ainsi que des réseaux de neurones bi-LSTM (_bidirectional Long Short-Term Memory_) couplés à un CRF (_Conditional Random Fields_), une approche robuste et fiable. L'utilisation de Flair se justifie par le fait que les vecteurs contextuels permettent de rendre compte des différents sens que peuvent prendre les mots selon le contexte. En complément de ces techniques, les EIG utilisent des techniques habituelles de traitement automatique du langage : règles déterministes à bases d'expressions régulières, tf-idf (_term frequency - inverse document frequency_), _word embedding_.

Notons que le défi OpenJustice bénéficie d'un corpus de décisions de justice conséquent : près de 3 millions de décisions de justice en base, une partie étant déjà pseudonymisée (les éléments identifiants à caractère personnel ont été retirés) et une plus petite partie annotée. Dans ce dernier cas, une classe (nom, prénom, adresse) est attribuée aux entités identifiantes de la décision afin d'entraîner des algorithmes. Ceci a été rendu possible par l'utilisation de logiciels de pseudonymisation en place depuis plusieurs années et par le travail de 10 annotateurs à temps plein au sein de la Cour de cassation.


## Assister les juridictions financières avec des techniques de recherche d'information et de fouilles de textes

Le défi [Plume](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/plume.html) assiste les juridictions financières au sein de la Cour des comptes. Entre autres, ce défi porte sur l'analyse de corpus documentaires, l'extraction d'entités nommées et l'utilisation de moteurs de recommandation. Les données sont composées de rapports, de recommandations, de comptes-rendus. Les techniques de traitement du langage utilisées sont le basique tf-idf, TextRank, LSA (_latent semantic analysis_) et les réseaux de neurones récurrents RNN. La recherche et la recommandation se fait à l'aide de bases de données orientées recherche, en l'occurrence ElasticSearch.


## Classifier des millions d'images pour fiabiliser le constat des infractions

Le défi [IA Flash](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/iaflash.html) fiabilise la constatation des infractions au sein du Ministère de l'Intérieur et de l’Agence nationale de traitement automatisé des infractions (ANTAI). Ce défi se concentre sur le traitement et la classification d'images. Il traite des millions d'images de radars automatiques en charge de relever les infractions routières. Les EIG ont recours à des techniques de traitement d'images et réalisent des classifications pour reconnaître automatiquement la marque et le modèle de véhicules en infraction. L’implémentation d’un réseau de neurone convolutif résiduel, entraîné parallèlement sur plusieurs processeurs graphiques (GPU) compte tenu du volume important de données d’apprentissage, donne déjà de bons résultats. Vous pouvez [tester leur modèle de classification en ligne](https://iaflash.fr).

> J'ai été agréablement surpris de découvrir un patrimoine de données riche : images (radars, vidéoprotection), structurés et référencées (données de titres, visa, carte d'identité, permis de conduire), textes.

**[Cristian Perez Brokate](/communaute/2019/cristian-perez.html), datascientist au sein du projet IA Flash**

## Assurer une navigation maritime sûre à l'aide d'algorithmes

Le défi [CibNav](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/cibnav.html) aide au contrôle des navires professionnels à la Direction des affaires maritimes. Il met en oeuvre des techniques de régression et de classification pour répondre à la question : est-il critique de procéder au contrôle de tel navire professionnel ? Le but est d'assurer la sécurité du navire et de l'équipage. Ils utilisent des techniques éprouvées d'apprentissage automatique telles que des arbres de décisions, des SVM (_Support Vector Machine_), des méthodes des k plus proches voisins ou encore des _Generalized Additive Models_. Ces algorithmes ont été choisis en raison de leur interprétabilité, condition nécessaire à l’adoption de l'outil par les agents en charge des contrôles.

## Endiguer la fraude à l'aide de graphes

Le défi [Adler](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/adler.html) lutte contre les comportements financiers illicites au Ministère de l’Action et des comptes publics, tandis que [Polygraphe](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2019/polygraphe.html) améliore la confiance des consommateurs en détectant des faux avis sur Internet à la Direction générale de la concurrence, de la consommation et de la répression des fraudes (DGCCRF). Ils utilisent les données pour prévenir et lutter contre des comportements illicites. Ils se reposent sur des données structurées ou semi-structurées et mettent en oeuvre diverses techniques de traitement du langage naturel, de détection d'anomalies et d'analyses de graphes. Les outils de fouilles de données mis en oeuvre grâce à ces techniques permettent à des agents de cibler plus finement les contrôles.


## Une communauté data science au cœur de l'administration

Pour promouvoir une culture de l’expérimentation dans l’administration, le programme EIG encourage les data scientists à entretenir des liens avec le monde de la recherche, à utiliser des logiciels libres et à s’intégrer à la communauté des data scientists dans l’Etat.

![Deux hommes et une femme sont assis autour d'une table avec deux ordinateurs. Ils discutent et échangent.](/img/blog/datajust-pac.jpg)
_[Kim Montalibet](https://entrepreneur-interet-general.etalab.gouv.fr/communaute/2019/kim-montalibet.html) et [Cédric Malherbe](https://entrepreneur-interet-general.etalab.gouv.fr/communaute/2019/cedric-malherbe.html), les EIG du défi DataJust, présentent leurs outils à Paul-Antoine Chevalier, data scientist à Etalab, lors du demo day interne organisé en juin 2019._

### Les administrations s’inspirent de la recherche

Les EIG ont des carrières variées : ils étaient auparavant indépendants, en contrat dans le secteur privé, dans le monde associatif ou en doctorat. Plusieurs data scientists sont proches de la recherche : certains sont titulaires d'un doctorat en apprentissage automatique, d'autres souhaitent commencer une thèse après le programme EIG tandis que certains rédigent des articles qu'ils ont soumis à des conférences. Par ailleurs, tous les défis s'inspirent d'articles de recherche ou de logiciels libres émanant d'articles de recherche disponibles librement en ligne sur des sites tels que [arXiv](https://arxiv.org/) ou [HAL](https://hal.archives-ouvertes.fr/) grâce à leur publication en open access.


### Les défis data science reposent sur des logiciels libres

Les défis data science EIG utilisent tous le langage Python et reposent sur des logiciels libres bien connus de la communauté : [Jupyter](https://jupyter.org/), [scikit-learn](https://scikit-learn.org/), [spaCy](https://spacy.io/), [PyTorch](https://pytorch.org/), [NLTK](https://www.nltk.org/), [Kepler Mapper](https://kepler-mapper.scikit-tda.org/), [NumPy](https://www.numpy.org/), [TextRank](https://github.com/summanlp/textrank), [Gensim](https://radimrehurek.com/gensim/) et bien d'autres. Les projets EIG ont des objectifs d'ouverture de leurs outils et de librairies, on peut donc s'attendre à des contributions et des publications de logiciels libres d'ici la fin de l'année de leur part. L’équipe d’accompagnement des EIG les [aide](https://doc.eig-forever.org/opensource.html) dans cette ouverture. Dans la continuité, plusieurs défis réfléchissent aux meilleures façons de publier leurs données d'entraînement en open data ou de mettre à disposition des modèles déjà entraînés.


### Etalab au coeur de la politique de la donnée

Le programme Entrepreneurs d'Intérêt Général est coordonné par Etalab. Grâce au portefeuille important de défis data science, des collaborations entre EIG et administrations se nouent. Par ailleurs, les EIG interagissent avec et enrichissent les écosystèmes animés par Etalab tels que le Lab IA, le [pôle data science d'Etalab](https://www.etalab.gouv.fr/datasciences-et-intelligence-artificielle) ou les [appels à manifestation d'intérêts intelligence artificielle](https://www.etalab.gouv.fr/intelligence-artificielle-decouvrez-les-15-nouveaux-projets-selectionnes). Toutes ces interactions structurent une communauté _open data science_ d'acteurs publics engagés pour mettre en oeuvre des méthodes de data science au service des politiques publiques.

*PS : cet article est rédigé conjointement avec les datascientists de la promotion 3 du programme EIG. Merci à toutes et tous.*
