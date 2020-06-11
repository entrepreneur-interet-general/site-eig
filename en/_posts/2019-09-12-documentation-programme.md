---
author: Antoine Augusti, EIG Link
description: As the program coordination team, our main duties are to set up cohorts, coach entrepreneurs throughout the year and promote and develop the EIG program. In this context, a knowledge base including our events, processes, explanations and good practices has to be set up. In this article, we describe the aims of our documentation, the construction process followed and how we update it.
image: /img/blog/doc-site.png
layout: post
tags:
- open
- méthode
- collectif
- outil
title: "Opening up the program's resources: our online documentation"
permalink: /en/blog/:year/:month/:day/:title.html
lang-ref: documentation-programme
twitter: AntoineAugusti
---

The Public Interest Entrepreneurs program aims to bring together people from outside administrations with advanced digital skills and public servants committed to innovation. Public Interest Entrepreneurs are divided into multidisciplinary twosomes or threesomes. They work in the fields of development, design and data science. Together with public officials of their host administrations, they have 10 months to meet the challenge of improving public services using digital technology and data. These challenges follow an open, transparent working approach, in particular through the publication of open source and open data productions.

The program currently has around thirty entrepreneurs per promotion, working in various administrations such as the Ministry of Ecological and Solidarity Transition, the Court of Auditors or the Bio agency.

As the program coordination team, our main duties are to set up promotions, coach entrepreneurs throughout the year and promote and develop the EIG program. **In this context, a knowledge base including our events, processes, explanations and good practices has to be set up.**

In this article, we describe the aims of our documentation, the construction process followed and how we change it.

**Aims of our documentation**

Our program has more than 30 people working in administrations in several geographic locations. Each promotion has a short lifespan (ten months), which means that the processes and resources available during the induction phase need to be explained clearly and memories need to be refreshed later.

The target users of our documentation are Public Interest Entrepreneurs, their mentors and the Etalab coordination team. Entrepreneurs need to understand how the program works and be able to access resources to meet their challenges in their administrations.

To meet these needs, our documentation has been divided into three main parts. A few examples of the content to be found are given below:

- **The program flow** : project coaching, planning of promotional events, tools used;
- **The resources available to EIGs in the promotion context** : the digital ecosystem of administrations, access to a third location, the possibility of obtaining infrastructure;
- **Good practices, organised by topic** : understanding free licenses, publishing and reusing data, writing strategy notes, and how to practice design in administrations.

**Cooperative, open source work**

Our documentation was not established in a day and will continue to progress. This work was started under the impetus of [Bastien Guerry](https://entrepreneur-interet-general.etalab.gouv.fr/communaute/2018/bastien-guerry.html) at the start of 2018. Bastien then had the [EIG Link](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2018/eiglink.html) role, the person assisting the program coordination team, responsible for the technical and methodological coaching of the challenges. It is he who wrote the first pages of our documentation based on the needs and resources identified progressively. We did not start from a blank page but were inspired by many available resources, which are also open source: [beta.gouv.fr](https://beta.gouv.fr/), [GDS](https://www.gov.uk/government/organisations/government-digital-service), [Code for Canada](https://medium.com/code-for-canada) blog and many others.

In accordance with the program&#39;s transparency and openness values and aims, this documentation is published under a free license [in a Gitrepository](https://github.com/entrepreneur-interet-general/eig-link). In concrete terms, our documentation comprises several text files written in [Markdown](https://fr.wikipedia.org/wiki/Markdown), a light markup language for writing text documents.

Our documentation is cooperative: it is maintained mainly by the program coordination team but entrepreneurs are invited to provide feedback and input. We are thus delighted to note that the documentation already contains more than 1,000 amendments made by 27 contributors.

It was important to start the documentation work from the start of 2018. I then advanced as and when needed according to questions of EIGs or the needs that I anticipated. With a vibrant community where mutual assistance is the norm, it was a real pleasure.

**Bastien Guerry,** [**EIG Link 2018**](https://entrepreneur-interet-general.etalab.gouv.fr/defis/2018/eiglink.html)

This documentation will never be finalized as it is established iteratively. It is written as and when needed, based on the questions we receive, the changes in our processes and our ambitions. It is our preferred means of sharing information and establishing an open knowledge base.

![Interface web de GitHub montrant plusieurs fichiers.](/img/blog/doc-github.png)
_Screenshot of our documentation [on GitHub](https://github.com/entrepreneur-interet-general/eig-link)._

**Making documentation pleasant to consult for everyone**

Our documentation comprises several Markdown files. Easy for cooperation: Contributors can submit changes directly to GitHub and have their changes approved in _pull-requests_. More annoying to browse through documentation: with about 20 Markdown files at the root, it&#39;s not easy to know where to start, even if a README file explains the documentation layout. What was not a problem initially, as the community was primarily technical and used to the GitHub interface, proved to be one over time.

For this reason, we chose to publish our documentation on a specific website, in addition to the Markdown source files already available on GitHub. We are used to using static websites: [the program&#39;s website](https://entrepreneur-interet-general.etalab.gouv.fr/) is based on [Jekyll](https://jekyllrb.com/), for example. For documentation, we turned to [VuePress](https://vuepress.vuejs.org/), a static website generator ideal for documentation needs that call for a minimum configuration. We took the opportunity to create [an open source VuePress theme](https://vuepress-gouv-fr-demo.eig-forever.org/) using the French administration&#39;s graphic codes.

![Site web de la documentation du programme faisant apparaitre une page sur la sécurité et un menu.](/img/blog/doc-site.png)
_Documentation screenshot, accessible at [doc.eig-forever.org](https://doc.eig-forever.org/)_

We thus now have documentation that is accessible online, pleasant to use, and on an interface appropriate for the various screens. In doing so, we have made a point of not introducing too much unnecessary technical complexity in terms of code or infrastructure. Most importantly, we have retained the ability to cooperate quickly on documentation: in the end, our documentation is just a set of basic text files.

**Avenues for development**

We are generally satisfied with our documentation, which has developed well over time. Entrepreneurs or other teams within Etalab have told us how useful Etalab is in fulfilling their assignments. Furthermore, this documentation could be an incubation mechanism for more extensive guides subsequently published by Etalab or DINSIC, in particular around the issues of open source publications, algorithms or data.

For the coming months, we want to continue working on the existing content, reorganize our sections and publish content for those who want to replicate a program similar to the Public Interest Entrepreneurs program in another structure or context.

We look forward to continuing to develop this documentation. We would be glad to see it be of benefit to others. If you would like to discuss this initiative with us, we would be delighted [to hear from you](https://entrepreneur-interet-general.etalab.gouv.fr/contact.html).
