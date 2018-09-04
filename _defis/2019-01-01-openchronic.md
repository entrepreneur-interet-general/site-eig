---
layout: defi2019
titre: Open Chronic
site: https://entrepreneur-interet-general.etalab.gouv.fr
annees: 2019
mission: "Améliorer la prise en charge des malades chroniques avec une nouvelle base de données de santé"
administration: Ministère de la santé, Direction de la recherche, des études, de l’évaluation et des statistiques
administration-website: http://drees.solidarites-sante.gouv.fr/etudes-et-statistiques/la-drees/
type: Data science
eigs:
  - nom: Un·e data engineer
  - nom: Un·e expert·e en data anonymisation
mentors: 
  - nom: Philéas Condemine
    site: /communaute/2018/phileas-condemine.html
  - nom: Stéphanie Combes
    site: /communaute/2018/stephanie-combes.html
images: 
  - /img/logo-open-chronic.png
---

La [Direction de la recherche, des études, de l’évaluation et des
statistiques (DREES)](http://drees.solidarites-sante.gouv.fr/etudes-et-statistiques/la-drees/) 
du Ministère des Solidarités et de la Santé 
souhaite construire une base de données des parcours de soin des 
malades chroniques et faciliter, pour les agences et établissements
de santé, le développement d’une variété d’outils, notamment pour 
mieux comprendre les variabilités de prise en charge des malades et 
mieux coordonner les différents professionnels de santé (ville/hôpital).

<br/>

## Open Chronic : améliorer la prise en charge des maladies chroniques et grâce à une nouvelle base de données de santé

### La problématique

Le vieillissement de la population et les évolutions de comportement notamment autour de l'activité et de l'alimentation conduisent à une transformation épidémiologique majeure : une forte croissance des pathologies chroniques telles que les maladies cardio-vasculaires, le diabète ou le cancer. 
En France, près de 10 millions de personnes souffrent d'une affection de longue durée (ALD), soit 15% de la population et le taux pourrait grimper à 20% en 2025. 

 **Améliorer la détection précoce, la prise en charge et les parcours de soins des patients concernés constitue un défi majeur des années à venir pour le système de santé** sachant que la prise en charge de ces patients représente plus de 70% des dépenses de l'assurance maladie. Constituer une base de données dédiée à la question est un axe particulièrement prometteur pour y parvenir puisque cela permettra d'effectuer des analyses très ciblées.

### Le défi : constituer une base de données sur les affections de longue durée, complète et exploitable

La loi du 26 janvier 2016 de modernisation du système de santé français a créé et permis l'accès au Système national des données de santé (SNDS). Il regroupe la base de données des feuilles de soin, les données hospitalières et la base des causes médicales de décès. 

A partir des données exhaustives du SNDS sur un an et en profondeur sur un échantillon de 4 millions de patients, les EIG devront :

* **créer la base Open Chronic pour permettre l'analyse des parcours de malades souffrant d'ALD**. L'extraction des parcours de soins demandera des compétences poussées en data engineering pour parvenir à traiter la volumétrie (plusieurs centaines de To) et la complexité (structuration variable) des données du SNDS. 

* **développer des outils permettant le traitement simplifié des données par l'Etat et les agences sanitaires dans le cadre de leur misison de service public**. Plusieurs pistes pourront être explorées :
   - la mise en place de modèles prédictifs de détection de patients présentant un fort risque de développer une ALD ;
   - l'analyse de la coordination des professionnels de santé ville/hôpital ;
   - l'analyse de la variabilité de la prise en charge tout au long du parcours de soins...

<br/>

## Les EIG recherché•e•s 

### EIG 1 - Un·e data engineer

**Missions principales** : Optimmiser l'exploitation du serveur, produire des scripts d'industrialisation et la documentation des procédures d'extraction des parcours de soins anonymisés pour générer Open Chronic.

**Compétences nécessaires** : maîtrise des librairies adaptées à l'exploitation de données volumineuses (plusieurs To), administration système. Des compétences en machine learning seraient un plus (GLM, Recurrent Neural Network, random forests).

### EIG 2 – Un·e expert·e en data anonymisation

**Missions principales** : mise en place d'un algorithme d'anonymisation, mesure du risque de ré-identification et calibrage de la base Open Chronic en consééquence.

**Compétences nécessaires** : algorithmique et en particulier algorithmique d’anonymisation, maîtrise des méthodes état de l'art -k-anonymisation, l-diversité, confidentialité différentielle.
Des compétences en machine learning seraient un plus (GLM, Recurrent Neural Network, random forests).

_L’environnement de travail des EIG : serveur centOS, 2To de RAM, GPU Tesla K80, R/Python/TensorFlow_

_Lieu de travail : 75014 métro Pasteur/Gaité/Montparnasse._

<br/>

## L'équipe autour des EIG

### Philéas Condemine, mentor opérationnel

![Philéas Condemine](/img/communaute/phileas-condemine.png)

Actuaire, data scientist chez AXA pendant 3 ans, Philéas Condemine a rejoint le programme EIG 2018 et a décidé de poursuivre l'aventure au LabSanté du ministère de la santé.

_"En data science la majorité des projets dans le privé sont du marketing ou de la tarification. On est parfois déçu par le manque de sens de nos projets ; au LabSanté du ministère de la Santé je peux travailler sur des sujets concrets, utiles avec comme objectif : améliorer la santé de tous. En plus, il s'agit d'une des bases de données (de santé) les plus riches au monde !"_ 

### Stéphanie Combes, mentor de haut niveau

![Stéphanie Combes](/img/communaute/photostephaniecombes.png)

_« Je travaille la donnée depuis 7 ans, données structurées, données
géolocalisées, données textuelles. Python, R, Rshiny sont mes amis.
Data-scientist à l'Insee ces dernières années, je suis arrivée à la
DREES avec l'envie d'exploiter le potentiel de ces données de santé
avec un nouveau regard. »_ 
