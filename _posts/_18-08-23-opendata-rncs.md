---
layout: post
title: Open Data + Logiciel Libre = Démocratie de l'Information
author: Pierre Camilleri, Christophe Ninucci
twitter: ChrisNinucci
description: Pour tous ceux qui manipulent des données financières, sachez que les bilans annuels déposés après le 1er janvier 2017 sont offerts en open data par l'INPI. Le format des données n'est aujourd'hui pas le plus attrayant, mais nous avons décidé dans le cadre de notre défi EIG de développer des outils open source pour permettre leur exploitation par le plus grand nombre.
---


# Signaux Faibles et l'Open Data

Le défi [Signaux Faibles](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/signauxfaibles/) a comme ligne de fond la mise en œuvre d'un protocol de prévention des difficultés des entreprises. Il est en effet d'autant plus efficace d'intervenir auprès des entreprises que leurs difficultés sont mieux anticipées car les leviers d'action seront plus nombreux, plus efficaces et plus faciles à mettre en oeuvre, évitant ainsi nombre de situations délicates ou désespérées. Par ailleurs, de la même façon qu'il est plus simple de soigner un rhume qu'une pneumonie, cette démarche s'inscrit dans une économie de moyens qui tombe sous le sens, aussi propice à la multiplication des effets positifs de l'action publique qu'à la prévention des dérives budgétaires de l'aide aux entreprises.

À cette fin, il existe en France une très grande richesse de dispositifs à l'efficacité reconnue pour intervenir à tous les niveaux, qu'ils soient d'ordre financier, organisationnels ou productifs. La démarche Signaux Faibles s'articule donc entre un dispositif opérationnel mettant en mouvement les acteurs de terrain qui cotoient les entreprises (URSSAF, DIRECCTE, Régions, et nous en oublions...) et une coordination orchestrée grâce à l'analyse algorithmique des données dont disposent les administrations avec pour cible de détection les entreprises fragilisées et comme leitmotiv le décloisonnement des administrations et la collaboration transversale sur fond de démarche bottom-up. Ce type d'organisation démontre ici son efficacité par le volontariat des participants et le foisonnement d'idées et améliorations qu'il favorise généreusement.

Pour ce qui est de la partie algorithmique, le projet fait feu de toute donnée sociale, économique ou financière et à ce titre le RNCS est une source de choix. En effet le Registre National du Commerce et des Sociétés (parfois appelé Infogreffe) est une base de données qui recèle tous les comptes annuels déposés par les entreprises auprès des greffes de tribunaux de commerces et ne faisant pas l'objet d'une demande de confidentialité ou d'une exemption accordée par principe aux petites entreprises. En fait de comptes annuels, on y trouve les bilans et comptes de résultats ainsi que les immatriculations, modifications et radiations des entreprises (RNCS IMR). Ce registre de données publiques constitue un véritable bilan de santé de l'économie française et a été ouvert en open data par décret en 2015.

L'institut national de la propriété intellectuelle (INPI) fournit donc depuis le premier trimestre 2017 gratuitement l'accès à l'ensemble des données économiques publiques des entreprises déposées depuis le premier janvier 2017. Ces données sont [disponibles sur simple demande] 
(https://www.inpi.fr/fr/nationales/l-inpi-lance-l-ouverture-des-donnees-du-registre-du-commerce-et-des-societes). Il est d'ailleurs à noter que l'open data de l'INPI ne se limite d'ailleurs pas au RNCS mais distribue également toutes les données en rapport avec son métier premier, à savoir [les marques](https://www.inpi.fr/fr/open-data-marques-francaises) et les brevets français](https://www.inpi.fr/fr/open-data-brevets-francais) qui constituent des vivier de données aussi vastes que riches.

Pour l'anecdote, la mise en open data du RNCS fait suite au [décret n° 2015-1905 du 30 décembre 2015](https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000031741407) qui précise des modalités de transmission et de mise à disposition de ces données publiques. Ce texte a donné lieu à une bataille juridique avec les greffes qui [n'aura pas suffi à empêcher la confirmation de l'INPI dans son rôle de diffuseur](https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000005634379&idArticle=LEGIARTI000031821154&dateTexte=) mais qui explique les deux ans de délais qu'il aura fallu pour ouvrir ces données.

# Un accès aux données facile mais...
L'accès aux comptes annuels est entièrement gratuit, sous réserve d'acceptation d'une [licence à compléter](https://www.inpi.fr/sites/default/files/licence_rncs_comptes_annuels_mars_2017_0.pdf) et à renvoyer par mail à licences@inpi.fr. Suite à l'acceptation de la licence par l'INPI sont fournis des identifiants par retour de mail qui ouvrent l'accès à un serveur FTPS dont la structure est expliquée dans la [documentation](https://www.inpi.fr/fr/sites/default/files/doc_tech_comptes_annuels_decembre_2017_v1.4.pdf) qui est parfaitement à jour et fonctionnelle.

![Aperçu du dépot](/img/blog/filezillaRncs.png)

Toutefois un [article Décodex du Monde](https://www.lemonde.fr/les-decodeurs/article/2018/06/22/comment-infogreffe-a-garde-la-main-sur-les-donnees-legales-des-entreprises_5319408_4355770.html) souligne que « les échantillons présentés [...] sont incompréhensibles pour un citoyen non averti, et relativement inexploitables sans un important retraitement pour une entreprise qui déciderait de les proposer à la consultation ». En effet, les fichiers, au [format XML](https://fr.wikipedia.org/wiki/Extensible_Markup_Language), ressemblent à l'échantillon présenté ci-dessous: 

![screenshot XML](/img/blog/screenXML.png)

Ces fichiers pourront effectivement faire obstacle à plus d'un aficionado du célèbre tableur, toutefois il faut noter qu'il s'agit d'un format standardisé depuis plus de 20 ans et que de nombreux outils permettent d'en tirer parti dans tous les langages de programmation. Par ailleurs la richesse des informations stockées dans ces fichiers se prête assez mal à des structures tabulaires plus classiques et à ce titre le choix du XML se révèle judicieux, la faute allant à la complexité naturelle des données véhiculées.

L'autre écueil à affronter pour exploiter ce format est l'utilisation d'une codification plutôt riche qu'il convient d'analyser avec la [documentation](https://www.inpi.fr/sites/default/files/doc_tech_comptes_annuels_decembre_2017_v1.4.pdf) fournie, conférant à une tentative d'exploitation manuelle une pénibilité qui ne s'oublie pas. Là encore, on ne peut que blâmer la nature des informations transportées.

Également, on pourra regretter cette maladresse qui consiste en la nécessité d'obtenir une license et des identifiants personnalisés, car même si la démarche est traitée très efficacement par l'INPI, elle condamne la réutilisation publique des données pour produire un format plus digeste.

Et pour en finir avec les mauvaises nouvelles, un quota de téléchargement de 1Go par jour est imposé aux utilisateurs, ce qui porte à quelques jours le temps minimum pour télécharger le dépot, condition nécessaire pour être certain de ne rien rater…

# Faciliter l'accès à l'information
Même si tout n'est pas parfait; et il s'en faut en fait de quelques détails; l'enjeu qui entoure ces données est tel qu'il vaut bien que nous nous accommodions de quelques inconvénients car l'essentiel est sauf. Le RNCS offre en effet de précieuses informations d'intelligence économique, et la précision de sa structure, la pertinence des chiffres qu'il délivre et le haut niveau de fiabilité des données qui le caractérise permettent d'envisager des traitements statistiques à grande valeur ajoutée.


Par ailleurs, on peut également se consoler en soulignant que l'accès à de ces informations était jusque là totalement payant. Ce partage d'information a un fort potentiel d'impact sur la transparence financière des entreprises françaises, et permet aussi d'envisager des traitements big data sur l'intégralité des données là où les services à péage facturaient souvent au nombre d'entreprises consultées, et limitaient de fait l'exploitation de la base complète à un public restreint de clients aussi fortunés que motivés dans cette démarche par leurs propres intérêts privés.


Même si aujourd'hui, l'historique des comptes annuels est absent de la base ouverte, cet alternative se pose comme concurrente directe des offres dispendieuses que sont par exemple l'application Diane (Bureau Van Dijk, aujourd'hui filiale de Moody's Corporation), Ellisphère ou societe.com; offres auxquelles souscrivent même les administrations françaises faute de pouvoir accéder autrement à leurs propres données.

Il nous semble nécessaire de permettre un meilleur accès à l'information que ces données contiennent, et cela pour favoriser leur réutilisation par le plus grand nombre et participer à libérer leur potentiel.

# Open Data + Open Source = Démocratie de l'information

Le mot d'ordre de l'open data (mouvement initié par Tim Berner-Lee) est « Raw Data Now » (données brutes maintenant) et même si il n'est nullement ici question de remettre en question ce slogan qui a su provoquer en quelques années un véritable tsunami, force est de constater que l'open data comme unique ingrédient n'arrive pas toujours à maximiser son rôle libérateur car l'investissement à consacrer à une réutilisation place parfois la barre très haute sur le plan technique. Le logiciel libre apporte ici une réponse en mirroir à cette problématique en offrant le véhicule idéal au savoir faire inhérent à l'exploitation des données complexes.

Par ailleurs, il nous semble tout à fait opportun de maximiser l'impact de notre développement en dégageant la brique dédiée au RNCS que nous développons dans le contexte du projet Signaux Faibles pour en faire un logiciel à part entière. En effet nous sommes avec le programme EIG au croisement entre l'open source, l'open data et l'intérêt général, ce qui fait de nous des acteurs privilégiés pour répondre à ces problématiques.

[gorncs](https://github.com/chrnin/gorncs) est donc une première brique libre, développée en première intention pour fournir ses fonctionnalités dans la plateforme [OpenSignauxFaibles](https://github.com/entrepreneur-interet-general/opensignauxfaibles). Comme nous pensons que ce premier module n'est pas suffisant pour atteindre l'idéal d'ouverture auquel nous aspirons; sa réutilisation demandant elle même quelques compétences propres aux informaticiens; il paraît essentiel d'embarquer cette brique dans une solution libre, simple à déployer et permettant l'accès aux compte annuels depuis un simple navigateur. C'est précisément l'objectif de la suite logicielle que nous avons commencé à développer et qui sera mise à jour à mesure que les fonctionnalités de consultation des comptes annuels feront leur entrée dans la plateforme [OpenSignauxFaibles](https://github.com/entrepreneur-interet-general/opensignauxfaibles).

Il existe de nombreuses données ouvertes qui souffrent de limites contextuelles et pour lesquelles le même type de solutions sont à envisager, parmi lesquelles nous avons déjà identifié le BODACC qui contraint à un retraitement d'une complexité bien supérieure à celle du RNCS et sur lequel nous investiguons actuellement. Ce dernier pourrait également faire l'objet du même genre de développement… À suivre !
