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
title: 'Bulletins: our open source weekly review tool'
lang-ref: bulletins-form
permalink: /en/blog/:year/:month/:day/:title.html
twitter: AntoineAugusti
---

Back about thirty digital professionals in 15 challenges in as many administrations in various places: this is the task that the team of the Entrepreneurs d&#39;Intérêt Général (EIG) program carries out on a daily basis. The multidisciplinary team backs Public Interest Entrepreneurs and mentors in various aspects of their challenges: strategy, technical, project management, assessment, communication, etc.

We would like to share with you one of the means of communication that we have set up to carry through our coaching task: **the weekly review**.

## Our problem: share progress in various challenges

The EIG team is able to monitor progress in each challenge on a weekly basis through advisors, but not other challenges. To overcome this information asymmetry, we needed a tool that will allow us to:

- share its weekly review asynchronously;
- archive its reviews;
- make it easier to read other reviews (as other challenges are taking place in other administrations, this only leaves a short period of attention).

## Alternatives considered

To meet this need for information between teams, weekly follow-up meetings, also known as &quot;stand-up meetings&quot;, are often held. Stand-up meetings are meetings where several people meet in the same place at the same time to take turns in talking about what they are working on. These are recurring milestones, which are used to circulate information within a team.

Problem: stand-up meetings call for several people to interrupt their respective work at the same time to absorb information that may not be useful to them at the same time. In addition, our teams are in different workplaces and have no crucial need to know the progress of other challenges in order to carry out their tasks. Finally, holding a review via an online communication tool (video or instant conversation) does not provide for true asynchrony or efficient archiving.

It was therefore crucial for the tool to be **asynchronous, quick to use and to provide for quick consultation of colleagues&#39; reviews**.

## Solution adopted

We did not find a tool that met our needs on the market and we considered that the development of such a tool would take a few days. I thus created [Bulletins](https://bulletins.eig-forever.org/), our weekly review tool, available as open source software.

Instead of interrupting everyone&#39;s work, our tool allows each team to provide a written assessment of the past week. Retrospectives are entered into a form, which each team fills out whenever they want to - as long as they fill it out in time. Once filled in, the reviews are then aggregated in an e-mail that is sent to everyone, and that everyone can read whenever they want to. Information can thus be circulated with no need for meetings.

![Formulaire web permettant de remplir sa rétrospective hebdomadaire](/img/blog/bulletins-form.png)
_Screenshot of the weekly review form_

![Interface web permettant la consultation des précédentes rétrospectives](/img/blog/bulletins-history.png)
_Screenshot of the consultation of a project&#39;s previous reviews_

Having thought long and hard about what questions to ask, we came up with the following questions:

- what is your state of mind?
- what was your priority for the week?
- what worked and what was more difficult?
- do you need help to overcome a difficulty?

These questions get straight to the point and provide for effective information sharing while leaving room for cooperation opportunities.

## Operation

Its operation is as follows:

- Each team fills in its review of the week by completing the follow-up form, on the basis of one review per team;
- The reviews entered are aggregated in an e-mail that is sent automatically every Friday at 3 p.m.

The answers entered in the application form are not public. However, this information is useful for each team: for this reason, it is possible to access a history of reviews, share reviews through a single link and export data.

## A generic, open source tool

The problem of sharing information between teams or projects is recurrent. [Bulletins](https://bulletins.eig-forever.org/) provides us with a simple, efficient weekly monitoring tool that is in line with our vision.

Through Bulletins, we have managed to involve around thirty people on a weekly basis. The coordination team now has a valuable tool to monitor everyone&#39;s progress. We use it in conjunction with other tools, such as instant discussion, where we regularly comment on reviews.

Colleagues at DINSIC are currently considering the use of this tool; we would be happy for you to do the same. Bulletins is open source and available in French or English to increase its potential for use. You can consult [its documentation online](https://bulletins.eig-forever.org/). If you have any questions, we will gladly discuss them with you on [GitHub](https://github.com/entrepreneur-interet-general/bulletins) or by e-mail sent to [entrepreneur-interet-general@data.gouv.fr](mailto:entrepreneur-interet-general@data.gouv.fr).
