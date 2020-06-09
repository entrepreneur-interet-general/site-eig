---
author: Bastien Guerry, EIG Link
description: Qu'est-ce que le logiciel libre ?  Les EIG en ont-ils utilisé ?  En ont-ils
  publiés ?  Comment aller plus loin ?  Quelques réflexions à l'issue de cette deuxième
  année du programme EIG.
image: https://upload.wikimedia.org/wikipedia/commons/e/ee/GNU%2BLinux.png
layout: post
tags:
- méthode
- outil
- open
title: What about open source software in all this?
lang-ref: logiciel-libre
permalink: /en/blog/:year/:month/:day/:title.html
twitter: bzg2
---

## Open source software and public administrations

Open source software is software that guarantees four freedoms for everyone: that of running the software as they see fit; that of analysing the program&#39;s operation (in particular by accessing its source code) and customizing it to their needs (by changing the source code); that of redistributing copies of the program; that of improving the program and redistributing copies of improved versions.

These &quot;four freedoms&quot; of open source software are the pillars of the movement with the same name, launched in the 1980s by Richard Stallman, then a computer scientist at MIT, who mobilized the hacker community to write an open source operating system called GNU (&quot;GNU is Not Unix&quot;). The movement gained momentum with the arrival of the Linux kernel in the early 1990s, which allowed the GNU open source system to run on ordinary computers.

<a title="Kazoza404 [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], from Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:GNU%2BLinux.png"><img alt="GNU+Linux" src="https://upload.wikimedia.org/wikipedia/commons/e/ee/GNU%2BLinux.png"></a>
<center><p><em>You knew about the penguin, the mascot of the Linux kernel, but did you know about the wildebeest, the symbol of the GNU is Not Unix project?</em></p></center>

In the 2000s, this movement spread in two ways: on the one hand with the emergence of &quot;open source&quot; products, which sought to emphasize the practical and economic value of open source, while at the same time avoiding the movement&#39;s political aspects; on the other with the spreading of open source ideas to fields other than information technology alone: this involved the launching of the Creative Commons licenses by Lawrence Lessig and the Wikipedia free encyclopedia by Jimmy Wales and Larry Sanger. The next two decades would see &quot;open&quot; initiatives in other areas, in particular _open access_ (for the open access publication of research articles) and _open data_ (for the opening up of public data).

Today, open source software is represented by standards well known to the general public such as the GNU/Linux system, the Firefox web browser, the VLC reader - and many others.

What&#39;s this got to do with administrations? They are large _consumers_ of software: efforts are regularly made to encourage the use of open source software, at least since [the Ayrault circular of 2012](http://www.cnll.fr/news/le-cnll-se-rejouit-de-la-circulaire-ayrault-sur-les-logiciels-libres/), with varying degrees of success. Administrations are also _producers_ of open source software. The Law for a Digital Republic of 7 October 2016 clearly states that the source codes of software used by a public body are administrative documents coming under the open data regime. As such, any citizen may ask to be provided with the /source code / of software ordered by administrations.

A recent example of a government-led open source project is the [Clip OS](https://www.ssi.gouv.fr/administration/services-securises/clip/) distribution recently released by the ANSSI (National agency for information systems security).

<a title="© Nextimpact"
href="https://www.nextinpact.com/news/107048-clip-os-anssi-ouvre-son-systeme-securise-a-tous-contributeurs.htm"><img
src="https://cdn2.nextinpact.com/images/bd/news/171736.jpeg"/></a>
<center><p><em>Overview of the security-oriented Clip OS distribution published under free license by ANSSI - © NextINpact</em></p></center>

These outreach efforts are just beginning: many administrations are not familiar with open source software; many projects are still developed without proper knowledge of the issues, constraints and potential benefits of the open source code approach.

The &quot;Public interest entrepreneur&quot; program assigns an important role to open source software. Follow me to see this in detail.

## You can learn how to use open source software!

Administrations produce open source software either by ordering it from a service provider or by developing it themselves. Few administrations are able to mobilize resources to develop products in-house. **The interest of the EIG program is to make technical skills the focus of services** and we have seen the benefits of this approach: public servants are involved in the statement of requirements and in improving products on a daily basis, EIGs have the satisfaction of testing their products at an early stage, and public servants and EIGs form complementary teams dialoguing constantly.

We started from the idea that EIGs, whether designers, developers or data scientists, have heard of open source but don&#39;t necessarily know what it actually means: &quot;open source&quot; often means that a software library can be used free of charge.

To go further, we carried out some collective teaching. First, by organizing two workshops open to EIGs and mentors, [one in March](https://entrepreneur-interet-general.etalab.gouv.fr/blog/2018/04/16/atelier-ouverture-logiciel-libre.html) during a coaching session and the other at DINSIC a few weeks later, with people from other administrations, to go further into _licensing_ issues and to take ownership of the government&#39;s [policy for contributing to open source software](https://disic.github.io/politique-de-contribution-open-source/), published last May.

<a
href="https://www.numerique.gouv.fr/publications/politique-logiciel-libre/"><img
src="/img/pocos.png" /></a>
<center><p><em>The Government&#39;s open source software contribution policy, published in May 2018, which provides the framework within which government agencies can contribute to the open source software ecosystem.</em></p></center>

I also wrote and shared an [introductory document about open source software](https://github.com/entrepreneur-interet-general/eig-link/blob/master/opensource.org), maintained a [Frequently Asked Questions section](https://github.com/entrepreneur-interet-general/eig-link/blob/master/opensource-faq.org), published [a one-page mini-guide in PDF format](https://entrepreneur-interet-general.etalab.gouv.fr/docs/mini-guide-logiciel-libre.pdf) and occasionally answered questions and help requests.

What are the first observations after ten months of progress in the subject?

1. Yes, EIGs may not know what open source software is and may believe that they have the right to copy code found on Github without looking into licensing issues…
2. Yes, open source licenses are complicated, but in fact, with a little clarification at the right time, it is _never_ a sticking point.
3. The approach seems natural for all EIGs: none of them complained about having to follow it.
4. There is still a lot to be done to make mentors feel comfortable with the subject, a lot of concepts to be explained and a lot of doubts to be removed about the real interest of all this.

## EIGs use mainly open source software

What are the open source tools/software/frameworks used by EIGs?

Loosely speaking: angular.js, antizer, apache airflow, apache hive, atom, babel, bootstrap, bulma, chart.js, cider, clojure, clojurescript, d3.js, elasticsearch, emacs, embulk, flask, git, jupyter, laravel, leaflet, mongodb, neo4j, postgresql, pyspark, python, r, react.js, redash, rstudio, sass, scala, scikit-learn, tensorflow, tornado, vim, visual studio code, vue.js, webpack.

That&#39;s a _lot_! It&#39;s the reflection of a de facto situation: it is nowadays impossible to develop a software project without using one or more open source products, either as a development tool or in the product&#39;s software &quot;stack&quot;.

<a title="© Github vient de passer la barre des 100 millions de dépôts" href="https://blog.github.com/2018-11-08-100M-repos/"><img src="https://user-images.githubusercontent.com/7321362/48171817-66b51680-e2b2-11e8-99f2-3467c803a7b1.png"/></a>
<center><p><em>The most popular products included on Github - © Github</em></p></center>

On the proprietary software side, there are only three: the Sublime Text editor, the Adobe suite and the Vertica database. The other proprietary tools EIGs have to use are the ones already available in their administrations (in particular Oracle databases).

## EIGs have produced open source software

But EIGs do not only consume open source software programs, they also produce them! Several categories: complete applications, software libraries, generic tools, scripts and other _ad hoc_ tools.

Applications include:

- [Open Scraper](https://github.com/entrepreneur-interet-general/OpenScraper): an open source tool for retrieving data from several websites at the same time and structuring the resulting data.
- [Gobelins](https://github.com/entrepreneur-interet-general/gobelins): a distribution and search tool for Mobilier national&#39;s collections.
- [Stalactite](https://github.com/jeanbaptisteassouad/cheapExp): a tool for viewing, classifying and processing a tree structure containing all types of documents (e-mails, images, documents, presentations, etc.).
- [Graph Explorer](https://github.com/entrepreneur-interet-general/graph-explorer): a tool for viewing and exploring a large graph of financial transactions.

<a href="https://github.com/entrepreneur-interet-general/graph-explorer"><img
src="https://raw.githubusercontent.com/entrepreneur-interet-general/graph-explorer/master/docs/img/home.png"
/></a>
<center><p><em>An overview of the Graph-Explorer interface</em></p></center>

Note the efforts made to _communicate well_ regarding these projects: writing a good README is an essential step in producing open source software. [Graph-Explorer](https://github.com/entrepreneur-interet-general/graph-explorer/blob/master/README.md), for example, guides the user step by step through the application&#39;s installation and testing, increasing the potential for reuse.

Generic tools include [metadocs](https://github.com/entrepreneur-interet-general/metadocs) which is used to include several [Sphinx](http://www.sphinx-doc.org/) documentation projects, [Open API Schemas to Markdown](https://github.com/entrepreneur-interet-general/open_api_schemas_to_markdown) which allows Markdown documentation to be generated from schemas in accordance with [Open API](https://github.com/OAI/OpenAPI-Specification) specifications and [spacy-lefff](https://github.com/sammous/spacy-lefff), a package for lemmatization and detection of the nature of a word in French.

<a href="https://github.com/entrepreneur-interet-general/metadocs"><img src="https://camo.githubusercontent.com/8db03293ee7081124ad99c9ebc38ee88ccb12b93/687474703a2f2f672e7265636f726469742e636f2f65674638627a783771632e676966" /></a>
<center><p><em>Animated gif presenting the metadocs tool, used to include several Sphinx documentation projects.</em></p></center>

Libraries include [H3.Standard](https://github.com/entrepreneur-interet-general/H3.Standard) to provide _binding_ between C Sharp and [the C library](https://uber.github.io/h3) developed by Uber for geospatial indexing based on hexagonal breakdown.

And finally, a few tools: a small [Twitter bot in Clojure](https://github.com/bzg/eigforever-twitter-bot), an [Org-mode export module](https://github.com/entrepreneur-interet-general/ox-html-timeline) to an HTML rendering in the form of a frieze, a [familiarization tool](https://github.com/entrepreneur-interet-general/vue-python-starter-kit) a python application for the _backend_ and vue.js for the _frontend_, a [csv2html](https://github.com/entrepreneur-interet-general/csv2html) mini application to publish csven [datatables](https://www.datatables.net/), a library for [locating public holidays in France](https://github.com/AntoineAugusti/jours-feries-france) and [another one for school holidays](https://github.com/AntoineAugusti/vacances-scolaires-france) ... there is something for everyone! All this just needs to be tested, debugged, used... and to receive your contributions: it&#39;s open source!

## EIG and the open source ecosystem: learn and/or share

Being &quot;open source&quot; also means participating in communities that discuss, share and learn together.

Those EIGs who wanted to do so [published](https://medium.com/@BGuigal/janusgraph-python-9e8d6988c36c)[several](https://bl.ocks.org/benoitguigal/e11a791079318b7ff6ecde9a6464801d) technicalblog entries, others asked their [questions](https://stackoverflow.com/questions/52624102/local-mathjax-with-mkdocs) on Stackoverflow, and others still [contributed](https://github.com/Attendize/Attendize/pull/486) to existing open source software. And above all, we have [sometimes](https://github.com/entrepreneur-interet-general/metadocs/pull/1)[received](https://github.com/entrepreneur-interet-general/H3.Standard/issues/1) help from people outside EIGs, and that&#39;s great!

These exchanges of knowledge take EIGs beyond their field of competence and their comfort zone. Some of them thus participated in the [day organized with the Framasoft association](https://framablog.org/2018/05/03/storify-est-mort-longue-vie-a/) around the writing of a Storify clone; while others dabbled with the free database [Wikidata](https://www.wikidata.org/) during a workshop in Etalab around the publication of [data.gouv.fr](https://www.data.gouv.fr/) data; while others finally discovered Wikimedia projects during a [day&#39;s visit to Mobilier National&#39;s workshops](https://entrepreneur-interet-general.etalab.gouv.fr/blog/2018/10/12/retour-sur-atelier-wikipedia-au-mobilier-national.html) and to the [Wikimedia commons](https://commons.wikimedia.org/wiki/Category:Atelier_Mobilier_national_du_21_septembre_2018). All opportunities to meet and cooperate with important &quot;open source&quot; actors.

<a href="https://framablog.org/2018/05/03/storify-est-mort-longue-vie-a/"><img src="https://framablog.org/wp-content/uploads/2018/05/Storia_-_Cr%C3%A9ation_liste-1024x648.png"/></a>
<center><p><em>EIG designers helped design a clone for Storify during the workshop undertaken with Framasoft.</em></p></center>

The aim was to move beyond the strictly utilitarian standpoint sometimes observed with reference to &quot;open source&quot; and meet communities that are involved in various aspects of this open source culture.

## How can projects be kept open source?

Known open source software are [common digital assets](https://fr.wikipedia.org/wiki/Biens_communs_num%C3%A9riques). &quot;Common assets&quot; suppose three aspects: a shared _resource_ (in this case the source code), a _community_ to maintain it, and the _governance_ rules that this community establishes.

Open source software programs produced by EIGs are not yet such common assets, as they are maintained by a small team and external contributions are not large enough for the question of governance to have arisen. But that leaves two problems unsolved: how to maintain them over time? why and how to turn them into digital common assets?

The first problem already arises for administrations. The EIG program has seen two ways of approaching this: the first is to _increase the skills_ of the in-house technical teams to allow them to become _power users_ of the application, or even be able to debug and upgrade it; the second is to invest in the creation of a collective body whose task is to _fund the future changes_ in the software. This is the case for the Open Scraper software, which is potentially useful for administrations other than the one that started its development within the EIG program.

It should be noted here that these issues go beyond the framework of EIGs and arise for all open source software. In 2017, Framasoft launched the [Contributopia](https://contributopia.org/fr/) campaign to draw users&#39; attention to the importance of contributing to and putting these common assets on a permanent footing.

Administrations are an interesting environment in this respect, as they are in a position to invest in the development of stable pooled resources. The required change of culture is twofold: move from being a simple consumer of open source software to a contributor, and from a contributor to a maintainer of a digital resource with its own governance, shared by a community extending beyond the boundaries of the contributing administration (the [OpenFisca](http://openfisca.org/) project is a good example of this). These changes have a cost and they will not happen spontaneously. The EIG program shows one way of looking at them: by putting the energy of committed developers at the heart of administration departments.

If the question of how to produce and maintain open source software in administrations interests you, meet in Paris on 6 December at the [Paris Open Source Summit](http://www.opensourcesummit.paris/) where DINSIC is organizing the **first meetings of open source software in administrations**.

We&#39;ll keep you posted!
