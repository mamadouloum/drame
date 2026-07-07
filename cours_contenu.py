# -*- coding: utf-8 -*-
"""
SOURCE UNIQUE DE CONTENU
========================
Cours de licence 3 (40 heures) : « Normes et méthodes de sécurité ».

Ce module décrit, pour CHAQUE diapositive, à la fois :
  - la description de la diapositive (pour le PowerPoint) ;
  - le discours de l'enseignant associé (pour le PDF/Markdown).

Les deux générateurs (`generate_cours_pptx.py` et `generate_cours_discours.py`)
importent la liste `SLIDES` construite ici, ce qui garantit un alignement
diapositive par diapositive parfait entre la présentation et le discours.

------------------------------------------------------------------------------
SCHÉMA D'UNE DIAPOSITIVE (dictionnaire)
------------------------------------------------------------------------------
Champs communs :
  kind    : type de gabarit (voir ci-dessous)
  title   : titre affiché
  module  : numéro de module (0 = ouverture / clôture / transversal)
  kicker  : sur-titre optionnel (petite étiquette au-dessus du titre)
  accent  : jeton couleur d'accent optionnel ("GOLD","TEAL","RED","BLUE",...)
  speech  : liste de blocs (tag, contenu) = discours de l'enseignant

Champs selon `kind` :
  title      : subtitle, meta
  module     : number, subtitle, topics(list[str])
  objectives : items(list[str])
  bullets    : items(list[str | (str,niveau)]), note(str?)
  cards      : cards(list[(titre,desc) | (titre,desc,couleur)]), cols(int)
  twocol     : left_head,left_items,right_head,right_items,left_color,right_color
  matrix     : headers(list[str]), rows(list[list[str]]), note(str?)
  process    : steps(list[(titre,desc)])
  stat       : big, caption, sub
  key        : text, attrib(str?)
  exercise   : brief, tasks(list[str]), deliverable(str), duration(str)
  checklist  : items(list[str]), cols(int), note(str?)
  quiz       : qa(list[(question,reponse)])
  closing    : subtitle

------------------------------------------------------------------------------
TAGS DE DISCOURS (blocs `speech`)
------------------------------------------------------------------------------
  ("p",   "…")            paragraphe à dire (texte courant)
  ("bul", ["…","…"])      liste à puces dite à l'oral
  ("obj", "…")            rappel d'objectif (encadré)
  ("def", "…")            définition à poser clairement (encadré)
  ("ex",  "…")            exemple concret (encadré)
  ("trans","…")           transition vers la suite (encadré)
  ("tip", "…")            conseil d'animation pour l'enseignant (encadré)
  ("inter","…")           activité / interaction avec les étudiants (encadré)
  ("warn","…")            piège fréquent / point de vigilance (encadré)
  ("key", "…")            message clé à faire retenir (encadré)
  ("sec", "…")            sous-titre interne (annexe FAQ)
"""


# --------------------------------------------------------------------------
# Petit constructeur pour écrire le contenu de façon concise et homogène.
# --------------------------------------------------------------------------
def S(kind, title, module=0, kicker=None, accent=None, speech=None, **deck):
    d = {"kind": kind, "title": title, "module": module,
         "kicker": kicker, "accent": accent, "speech": speech or []}
    d.update(deck)
    return d


# ==========================================================================
#  OUVERTURE
# ==========================================================================
FRONT = [
    S("title", "Normes et méthodes\nde sécurité", module=0,
      subtitle="Gouverner, normaliser et maîtriser le risque des systèmes d'information",
      meta="Licence 3 · Cours de 40 heures · 10 modules · Travaux dirigés et étude de cas fil rouge",
      speech=[
        ("p", "Bonjour à toutes et à tous, et bienvenue dans ce cours intitulé "
              "« Normes et méthodes de sécurité ». Pendant quarante heures, nous "
              "allons apprendre à protéger un système d'information non pas au "
              "hasard, mais de façon organisée, méthodique et reconnue par des "
              "référentiels internationaux."),
        ("p", "Ce cours ne demande aucun prérequis technique avancé. Nous allons "
              "construire ensemble, brique par brique, un vocabulaire commun, puis "
              "les grandes normes — la famille ISO 27000, le cadre du NIST — et "
              "enfin les méthodes concrètes comme la gestion des risques ou "
              "l'audit. L'objectif final : que vous sachiez comment une "
              "organisation sérieuse pilote sa sécurité."),
        ("tip", "Prendre deux minutes pour se présenter, présenter le fil rouge du "
                "cours (une étude de cas suivie tout du long) et rassurer : on part "
                "de zéro, on avance progressivement, et chaque notion sera illustrée."),
        ("key", "Message d'ouverture : la sécurité de l'information est d'abord une "
                "affaire de méthode et de gouvernance, pas seulement de technique."),
      ]),

    S("bullets", "De quoi parle ce cours ?", module=0, kicker="Positionnement",
      accent="GOLD",
      items=[
        "La sécurité de l'information : protéger la confidentialité, l'intégrité et la disponibilité des données",
        "Les NORMES : des référentiels communs (ISO/IEC 27001, 27002, NIST CSF…) qui définissent les bonnes pratiques",
        "Les MÉTHODES : des démarches outillées (gestion des risques EBIOS, audit, PDCA) pour agir concrètement",
        "Le fil conducteur : gouverner la sécurité, pas seulement empiler des outils",
      ],
      note="On parle d'organisation, de processus et de décisions — la technique vient servir cette démarche.",
      speech=[
        ("p", "Commençons par clarifier le titre. Trois mots comptent : sécurité, "
              "normes, méthodes. La sécurité de l'information, c'est l'ensemble des "
              "moyens qui préservent trois propriétés de nos données : leur "
              "confidentialité, leur intégrité et leur disponibilité. Nous y "
              "reviendrons en détail dès le module 1."),
        ("p", "Les normes sont des référentiels partagés : des documents, souvent "
              "internationaux, qui disent ce qu'il faut faire pour bien gérer la "
              "sécurité. Les méthodes, elles, disent comment le faire, étape par "
              "étape : comment analyser un risque, comment auditer, comment "
              "s'améliorer en continu."),
        ("def", "Une norme décrit le « quoi » (les exigences, les bonnes "
                "pratiques) ; une méthode décrit le « comment » (la démarche pour y "
                "parvenir). Le cours articule sans cesse ces deux dimensions."),
        ("trans", "Voyons maintenant ce que vous saurez faire à la fin de ces "
                  "quarante heures."),
      ]),

    S("objectives", "Objectifs pédagogiques", module=0, kicker="Compétences visées",
      accent="TEAL",
      items=[
        "Maîtriser le vocabulaire de la sécurité de l'information et du risque",
        "Situer et expliquer les grandes normes (famille ISO 27000, NIST CSF 2.0)",
        "Comprendre le fonctionnement d'un SMSI selon ISO/IEC 27001:2022",
        "Conduire une analyse de risque avec ISO 27005 et EBIOS Risk Manager",
        "Sélectionner et justifier des mesures de sécurité (ISO/IEC 27002:2022)",
        "Connaître le cadre légal : RGPD, NIS2, DORA, et le rôle de l'ANSSI",
        "Préparer et comprendre un audit de sécurité et un projet de certification",
      ],
      speech=[
        ("obj", "À l'issue du cours, vous devez être capables de tenir une "
                "conversation professionnelle sur la sécurité : comprendre un "
                "auditeur, lire une politique, participer à une analyse de risque."),
        ("p", "Regardez ces objectifs comme une progression. On commence par le "
              "vocabulaire, indispensable pour se comprendre. Puis on situe les "
              "grandes normes, on entre dans le détail du SMSI — le système de "
              "management de la sécurité de l'information — et on apprend à "
              "analyser les risques."),
        ("p", "Ensuite, on relie tout cela aux mesures concrètes et au cadre "
              "légal, de plus en plus présent avec des textes comme le RGPD ou la "
              "directive NIS2. Enfin, on met tout en pratique dans une étude de cas "
              "et on prépare un audit, comme dans la vraie vie professionnelle."),
        ("tip", "Inviter les étudiants à noter, dès aujourd'hui, l'objectif qui "
                "leur parle le plus : cela crée un fil personnel de motivation."),
      ]),

    S("cards", "Le programme en 10 modules", module=0, kicker="Plan du cours",
      cols=2,
      cards=[
        ("1 · Fondamentaux de la sécurité", "Concepts, critères DICP, risque, principes", "GOLD"),
        ("2 · Gouvernance & cadre normatif", "Normes, organismes, famille ISO 27000", "TEAL"),
        ("3 · ISO/IEC 27001:2022 — le SMSI", "Clauses 4 à 10, PDCA, certification", "BLUE"),
        ("4 · ISO/IEC 27002:2022 — les mesures", "93 mesures, 4 thèmes, attributs", "BLUE"),
        ("5 · Gestion des risques", "ISO 27005 & EBIOS Risk Manager v1.5", "GOLD"),
        ("6 · NIST CSF 2.0 & référentiels", "6 fonctions, CIS, COBIT, PCI DSS", "TEAL"),
        ("7 · Politiques & mesures concrètes", "PSSI, IAM, crypto, journalisation", "BLUE"),
        ("8 · Audit, conformité & droit", "Audit, RGPD, NIS2, DORA", "RED"),
        ("9 · SecOps, DevSecOps & Cloud", "SOC, incident, continuité, cloud", "TEAL"),
        ("10 · Étude de cas & examen", "Projet fil rouge : SMSI d'une PME", "GOLD"),
      ],
      speech=[
        ("p", "Voici notre feuille de route : dix modules de quatre heures chacun. "
              "Les trois premiers posent les fondations et le système de management. "
              "Les modules 4 à 6 couvrent les mesures et les grands référentiels."),
        ("p", "Les modules 7 à 9 descendent vers le concret : les politiques, les "
              "mesures techniques, l'audit, le droit, puis la sécurité "
              "opérationnelle et le cloud. Enfin, le module 10 est entièrement "
              "consacré à une étude de cas où vous jouerez le rôle d'une équipe "
              "sécurité qui construit le SMSI d'une PME."),
        ("trans", "Un mot maintenant sur l'organisation pratique et l'évaluation."),
      ]),

    S("matrix", "Organisation & évaluation", module=0, kicker="Modalités",
      headers=["Élément", "Détail"],
      rows=[
        ["Volume horaire", "40 h — 10 modules de 4 h (cours + TD)"],
        ["Pédagogie", "Cours, exemples, exercices dirigés, étude de cas fil rouge"],
        ["Étude de cas", "Construction du SMSI d'une PME fictive (module 10)"],
        ["Évaluation", "Contrôle continu (exercices) + projet + examen final écrit"],
        ["Supports", "Diapositives + discours de l'enseignant (ce document)"],
        ["Références", "Normes ISO/IEC, guides ANSSI, publications NIST"],
      ],
      note="Les exercices de fin de module préparent directement le projet et l'examen.",
      speech=[
        ("p", "Quelques repères pratiques. Le cours fait quarante heures, "
              "découpées en dix modules de quatre heures. Chaque module mélange des "
              "apports théoriques, des exemples et au moins un exercice dirigé."),
        ("p", "L'évaluation combine trois choses : le contrôle continu à travers "
              "les exercices, un projet qui est l'étude de cas fil rouge, et un "
              "examen final écrit. Autrement dit, si vous suivez les exercices au "
              "fur et à mesure, vous préparez déjà votre examen."),
        ("tip", "Adapter ce tableau aux modalités réelles de l'établissement : "
                "coefficients, dates, éventuel oral de soutenance du projet."),
        ("trans", "Nous avons le cadre. Entrons dans le vif du sujet avec les "
                  "fondamentaux."),
      ]),
]


# ==========================================================================
#  MODULE 1 — FONDAMENTAUX DE LA SÉCURITÉ DE L'INFORMATION
# ==========================================================================
M1 = [
    S("module", "Fondamentaux de la sécurité de l'information", module=1,
      number="01", subtitle="Concepts, vocabulaire et principes directeurs",
      topics=["Sécurité de l'information vs cybersécurité",
              "Les critères DICP et la triade CIA",
              "Actifs, menaces, vulnérabilités, risques",
              "Grands principes : défense en profondeur, moindre privilège"],
      speech=[
        ("p", "Nous ouvrons le premier module, consacré aux fondamentaux. C'est la "
              "brique sur laquelle tout le reste va s'appuyer. Sans ce vocabulaire "
              "commun, les normes et les méthodes resteraient abstraites."),
        ("obj", "À la fin de ce module, vous saurez définir la sécurité de "
                "l'information, distinguer menace, vulnérabilité et risque, et citer "
                "les grands principes de protection."),
      ]),

    S("objectives", "Objectifs du module 1", module=1, kicker="Ce que vous saurez faire",
      accent="GOLD",
      items=[
        "Définir la sécurité de l'information et la distinguer de la cybersécurité",
        "Expliquer les critères DICP (disponibilité, intégrité, confidentialité, preuve)",
        "Différencier actif, menace, vulnérabilité, risque et impact",
        "Décrire la défense en profondeur et le principe de moindre privilège",
        "Comprendre pourquoi le facteur humain est central",
      ],
      speech=[
        ("p", "Voici précisément ce que nous visons dans ce module. Cinq "
              "capacités, très concrètes, qui vont revenir en permanence dans la "
              "suite du cours. Prenez-les comme une grille de lecture."),
        ("tip", "Annoncer qu'un exercice de synthèse clôturera le module pour "
                "vérifier ces objectifs."),
      ]),

    S("bullets", "Qu'est-ce que la sécurité de l'information ?", module=1,
      kicker="Définition", accent="TEAL",
      items=[
        "La protection de l'information sous toutes ses formes : numérique, papier, orale",
        "Un objectif : préserver la valeur de l'information pour l'organisation",
        ("Trois périmètres souvent confondus :", 0),
        ("Sécurité de l'information : toute l'information, tous supports", 1),
        ("Cybersécurité : ce qui touche au cyberespace et aux systèmes numériques", 1),
        ("Sécurité des systèmes d'information (SSI) : les SI de l'organisation", 1),
      ],
      note="La sécurité de l'information est le concept le plus large ; la cybersécurité en est une composante.",
      speech=[
        ("p", "Posons la première définition. La sécurité de l'information, c'est "
              "protéger l'information sous toutes ses formes. Et j'insiste : toutes "
              "ses formes. Un document papier confidentiel oublié sur une "
              "imprimante, une conversation dans un train, un fichier sur un "
              "serveur : ce sont trois problèmes de sécurité de l'information."),
        ("def", "Sécurité de l'information : préservation de la confidentialité, de "
                "l'intégrité et de la disponibilité de l'information, quelle que soit "
                "sa forme."),
        ("p", "On confond souvent trois termes. La cybersécurité concerne le "
              "cyberespace et les systèmes numériques. La sécurité des systèmes "
              "d'information, ou SSI, concerne les SI d'une organisation. Et la "
              "sécurité de l'information englobe tout cela, y compris le non "
              "numérique. Retenez l'emboîtement : l'information est le concept le "
              "plus large."),
        ("warn", "Erreur fréquente chez les étudiants : réduire la sécurité à "
                 "l'informatique. Un post-it avec un mot de passe est déjà une "
                 "faille de sécurité de l'information."),
      ]),

    S("cards", "Les critères DICP", module=1, kicker="Les propriétés à protéger",
      cols=2,
      cards=[
        ("Disponibilité", "L'information est accessible quand on en a besoin", "TEAL"),
        ("Intégrité", "L'information n'est pas altérée sans autorisation", "BLUE"),
        ("Confidentialité", "Seules les personnes autorisées y accèdent", "GOLD"),
        ("Preuve / Traçabilité", "On peut prouver qui a fait quoi, et quand", "RED"),
      ],
      note="La triade anglo-saxonne « CIA » (Confidentiality, Integrity, Availability) ; l'ANSSI y ajoute la Preuve : D-I-C-P.",
      speech=[
        ("p", "Voici le cœur du réacteur : les critères de sécurité. Dans le monde "
              "anglo-saxon, on parle de la triade CIA — Confidentiality, Integrity, "
              "Availability. En France, l'ANSSI ajoute un quatrième critère, la "
              "preuve, ce qui donne l'acronyme DICP."),
        ("def", "Disponibilité : pouvoir accéder à l'information au bon moment. "
                "Intégrité : garantir qu'elle n'a pas été modifiée indûment. "
                "Confidentialité : réserver l'accès aux personnes autorisées. "
                "Preuve : pouvoir tracer et prouver les actions."),
        ("ex", "Un hôpital : la disponibilité du dossier patient peut sauver une "
               "vie ; l'intégrité d'une prescription évite une erreur de dose ; la "
               "confidentialité protège la vie privée ; la traçabilité permet de "
               "savoir qui a consulté quoi."),
        ("key", "Toute mesure de sécurité vise à protéger au moins un de ces "
                "critères. Se demander « quel critère je protège ? » est un réflexe "
                "d'expert."),
      ]),

    S("bullets", "Actif, valeur métier, bien support", module=1,
      kicker="Ce que l'on protège", accent="BLUE",
      items=[
        "Actif (ou bien) : tout ce qui a de la valeur pour l'organisation",
        ("Valeur métier : une information ou un processus essentiel (ex. le fichier clients, la paie)", 0),
        ("Bien support : ce sur quoi repose la valeur métier (serveur, logiciel, personne, local)", 0),
        "Identifier ses actifs est le point de départ de toute démarche de sécurité",
        "On ne peut pas protéger ce que l'on n'a pas recensé",
      ],
      note="Vocabulaire repris par la méthode EBIOS Risk Manager (module 5).",
      speech=[
        ("p", "Avant de protéger, il faut savoir quoi protéger. On parle d'actifs, "
              "ou de biens. Un actif, c'est tout ce qui a de la valeur : une "
              "donnée, un logiciel, un équipement, mais aussi une personne ou une "
              "réputation."),
        ("def", "La méthode française EBIOS distingue la valeur métier — "
                "l'information ou le processus essentiel à la mission — et le bien "
                "support — le serveur, le logiciel, la personne ou le local sur "
                "lequel repose cette valeur métier."),
        ("ex", "Pour une école : la valeur métier, ce sont les notes des étudiants ; "
               "les biens supports, ce sont le logiciel de scolarité, le serveur qui "
               "l'héberge, et l'agent qui le gère."),
        ("key", "On ne peut pas protéger ce que l'on n'a pas recensé. La cartographie "
                "des actifs est la toute première étape, et souvent la plus négligée."),
      ]),

    S("process", "Menace, vulnérabilité, risque", module=1,
      kicker="La chaîne du risque", accent="RED",
      steps=[
        ("Menace", "Un danger potentiel (attaquant, panne, erreur, incendie)"),
        ("Vulnérabilité", "Une faiblesse exploitable (faille, absence de sauvegarde)"),
        ("Risque", "La menace exploite la vulnérabilité → un scénario probable"),
        ("Impact", "Les conséquences si le risque se réalise"),
      ],
      speech=[
        ("p", "Voici quatre mots que l'on mélange tout le temps, et qu'il faut "
              "absolument distinguer. Une menace, c'est un danger potentiel : un "
              "attaquant, mais aussi une panne, une erreur humaine, un incendie. "
              "Une vulnérabilité, c'est une faiblesse : une faille logicielle, "
              "l'absence de sauvegarde, une porte non verrouillée."),
        ("def", "Le risque naît de la rencontre entre une menace et une "
                "vulnérabilité : c'est un scénario probable, associé à un impact — "
                "les conséquences si le scénario se réalise."),
        ("ex", "La pluie est une menace. Un trou dans le toit est une "
               "vulnérabilité. Le risque, c'est « la pluie entre par le trou ». "
               "L'impact, c'est le parquet abîmé. Réparer le toit supprime la "
               "vulnérabilité ; on ne peut pas empêcher la pluie."),
        ("key", "On agit rarement sur la menace (on ne contrôle pas les "
                "attaquants) ; on agit surtout sur les vulnérabilités et sur "
                "l'impact. C'est toute la logique des mesures de sécurité."),
      ]),

    S("cards", "Qui sont les sources de menace ?", module=1,
      kicker="Panorama des attaquants", cols=3,
      cards=[
        ("Cybercriminels", "Motivés par l'argent (rançongiciels, fraude)", "RED"),
        ("États / espionnage", "Attaques ciblées, sophistiquées, discrètes", "RED"),
        ("Hacktivistes", "Défense d'une cause, atteinte à l'image", "ORANGE"),
        ("Interne malveillant", "Salarié, prestataire mécontent", "ORANGE"),
        ("Erreur humaine", "Non malveillante mais très fréquente", "GREY"),
        ("Panne / accident", "Défaillance technique, catastrophe", "GREY"),
      ],
      note="Menaces intentionnelles ET accidentelles : les deux comptent en sécurité de l'information.",
      speech=[
        ("p", "Les menaces ne sont pas toutes des pirates encapuchonnés. "
              "Distinguons les sources. Les cybercriminels, d'abord, motivés par "
              "l'argent : c'est la grande majorité. Les États et l'espionnage "
              "industriel, plus rares mais très sophistiqués. Les hacktivistes, qui "
              "défendent une cause."),
        ("p", "Mais n'oubliez jamais les menaces internes et accidentelles : le "
              "salarié mécontent, et surtout l'erreur humaine, qui est l'une des "
              "premières causes d'incident. Enfin, les pannes et catastrophes — un "
              "incendie de datacenter menace la disponibilité tout autant qu'un "
              "attaquant."),
        ("warn", "Ne pas se focaliser uniquement sur l'attaquant externe. Beaucoup "
                 "d'incidents majeurs viennent d'erreurs internes ou de pannes."),
      ]),

    S("bullets", "Surface d'attaque & défense en profondeur", module=1,
      kicker="Deux notions clés", accent="TEAL",
      items=[
        "Surface d'attaque : l'ensemble des points par lesquels on peut être attaqué",
        "Plus on a de services exposés, plus la surface est grande",
        ("Défense en profondeur : empiler plusieurs lignes de défense indépendantes", 0),
        ("Si une barrière cède, la suivante protège encore", 1),
        ("Inspirée des châteaux forts : douves, murailles, donjon", 1),
        "Aucune mesure n'est parfaite : on combine des couches complémentaires",
      ],
      note="Réduire la surface d'attaque + multiplier les couches = deux réflexes fondateurs.",
      speech=[
        ("p", "Deux notions structurantes. D'abord la surface d'attaque : c'est "
              "l'ensemble des points par lesquels quelqu'un pourrait entrer. Chaque "
              "service exposé sur Internet, chaque compte, chaque logiciel installé "
              "agrandit cette surface. Réduire la surface d'attaque — fermer ce qui "
              "est inutile — est un réflexe de base."),
        ("def", "Défense en profondeur : ne jamais compter sur une seule barrière, "
                "mais empiler plusieurs lignes de défense indépendantes, pour que la "
                "défaillance de l'une soit rattrapée par la suivante."),
        ("ex", "Le château fort : les douves, puis la muraille, puis le donjon. "
               "En informatique : le pare-feu, puis l'authentification, puis le "
               "chiffrement des données, puis les sauvegardes."),
        ("key", "Réduire la surface d'attaque et multiplier les couches de "
                "protection : deux réflexes que l'on retrouvera dans toutes les "
                "normes."),
      ]),

    S("cards", "Les grands principes de sécurité", module=1,
      kicker="Des règles d'or", cols=3,
      cards=[
        ("Moindre privilège", "Chacun n'a que les droits strictement nécessaires", "GOLD"),
        ("Besoin d'en connaître", "Accès à une info seulement si nécessaire", "GOLD"),
        ("Défense en profondeur", "Plusieurs couches indépendantes", "TEAL"),
        ("Sécurité par conception", "Penser sécurité dès la conception (by design)", "TEAL"),
        ("Séparation des tâches", "Aucune personne seule ne maîtrise tout", "BLUE"),
        ("Zero Trust", "Ne jamais faire confiance par défaut, toujours vérifier", "BLUE"),
      ],
      note="Ces principes irriguent les normes ISO et NIST que nous verrons ensuite.",
      speech=[
        ("p", "Terminons les concepts par les grands principes, les règles d'or "
              "que tout professionnel connaît. Le moindre privilège : chacun ne "
              "reçoit que les droits strictement nécessaires à son travail, ni "
              "plus. Le besoin d'en connaître : on n'accède à une information que "
              "si on en a réellement besoin."),
        ("p", "La sécurité par conception, ou security by design : on ne rajoute "
              "pas la sécurité à la fin, on la pense dès le départ. La séparation "
              "des tâches : aucune personne seule ne doit pouvoir mener une action "
              "sensible de bout en bout, pour éviter la fraude. Et le Zero Trust, "
              "très en vogue : ne jamais faire confiance par défaut, toujours "
              "vérifier, même à l'intérieur du réseau."),
        ("key", "Ces principes ne sont pas théoriques : on les retrouvera, presque "
                "mot pour mot, dans les mesures des normes ISO 27002 et du NIST."),
      ]),

    S("stat", "≈ 80 %", module=1,
      caption="des incidents de sécurité impliquent, à un moment, un facteur humain",
      sub="Ordre de grandeur couramment cité : erreur, négligence, manipulation. La technique seule ne suffit jamais.",
      accent="RED",
      speech=[
        ("p", "Je veux insister sur un point avant de clore les concepts : "
              "l'humain. On cite souvent que la grande majorité des incidents "
              "impliquent, à un moment ou à un autre, un facteur humain — une "
              "erreur, une négligence, ou une manipulation par ingénierie sociale. "
              "Prenez ce chiffre comme un ordre de grandeur, pas comme une mesure "
              "exacte."),
        ("p", "La conséquence est fondamentale pour tout notre cours : la sécurité "
              "ne peut pas être seulement technique. Elle est aussi une affaire "
              "d'organisation, de règles, de sensibilisation et de culture. C'est "
              "exactement pour cela que les normes insistent autant sur la "
              "gouvernance et sur les personnes."),
        ("key", "La meilleure technologie ne protège pas une organisation où "
                "personne n'est sensibilisé ni responsabilisé."),
      ]),

    S("exercise", "Exercice — Cartographier un risque", module=1,
      kicker="Travaux dirigés", duration="30 min",
      brief="En binôme, choisissez une organisation simple (une bibliothèque municipale, "
            "une petite boutique en ligne) et appliquez le vocabulaire du module.",
      tasks=[
        "Lister 3 valeurs métier et leurs biens supports",
        "Pour chaque valeur, indiquer le critère DICP le plus important",
        "Identifier 2 menaces et 2 vulnérabilités plausibles",
        "Formuler 1 risque sous la forme « menace + vulnérabilité → impact »",
      ],
      deliverable="Un tableau d'une page présenté oralement en 3 minutes.",
      speech=[
        ("inter", "Constituer les binômes, laisser 20 minutes de travail puis "
                  "10 minutes de restitution. Circuler pour aider à distinguer "
                  "valeur métier et bien support, confusion la plus fréquente."),
        ("p", "À vous de jouer. L'objectif n'est pas d'être exhaustif, mais de "
              "manipuler le vocabulaire : valeur métier, bien support, critère "
              "DICP, menace, vulnérabilité, risque. Choisissez une organisation "
              "simple que vous connaissez, et déroulez la chaîne."),
        ("tip", "Faire ressortir, lors de la restitution, qu'un même actif peut "
                "relever de plusieurs critères DICP, et que les binômes formulent "
                "souvent une vulnérabilité comme une menace : corriger ensemble."),
      ]),

    S("key", "L'essentiel du module 1", module=1, kicker="À retenir",
      text="La sécurité de l'information protège quatre critères — Disponibilité, "
           "Intégrité, Confidentialité, Preuve — sur des actifs qu'il faut d'abord "
           "recenser. Le risque naît d'une menace exploitant une vulnérabilité. "
           "On s'en protège par des principes simples et par des couches successives.",
      attrib="Synthèse — Fondamentaux",
      speech=[
        ("p", "Récapitulons ce premier module. La sécurité de l'information "
              "protège quatre critères : disponibilité, intégrité, confidentialité "
              "et preuve. Elle s'applique à des actifs, qu'il faut d'abord "
              "recenser."),
        ("p", "Le risque naît d'une menace qui exploite une vulnérabilité, avec un "
              "impact à la clé. On s'en protège par des principes — moindre "
              "privilège, défense en profondeur — et en gardant à l'esprit que "
              "l'humain est central. Ce vocabulaire va nous servir dans tout le "
              "reste du cours."),
        ("trans", "Maintenant que nous partageons un langage commun, montons d'un "
                  "cran : qui organise la sécurité, et avec quels référentiels ? "
                  "C'est l'objet du module 2, la gouvernance et le cadre normatif."),
      ]),
]


# Liste finale (les autres modules sont ajoutés par la suite).
# --------------------------------------------------------------------------
# Helpers pour les modules 2 à 10.
# Ils permettent de garder un contenu riche sans dupliquer manuellement les
# mêmes consignes de discours sur chaque diapositive.
# --------------------------------------------------------------------------
def _plain_items(items):
    out = []
    for it in items or []:
        out.append(it[0] if isinstance(it, tuple) else it)
    return out


def _speech_auto(kind, title, deck):
    """Produit un discours enseignant accessible pour une diapositive.
    Les générateurs PDF/Markdown affichent ces blocs sous forme de texte
    pédagogique : explication simple, exemple, point de vigilance, conclusion.
    """
    intro = deck.get("teacher") or (
        "Cette diapositive sert à installer la notion « %s ». "
        "L'idée est de partir du sens courant des mots, puis de les relier "
        "progressivement à un usage professionnel." % title
    )
    sp = [("p", intro)]

    if kind in ("objectives", "bullets", "checklist"):
        pts = _plain_items(deck.get("items"))
        if pts:
            sp.append(("bul", pts))
    elif kind == "cards":
        cards = deck.get("cards", [])
        pts = []
        for c in cards:
            if len(c) >= 2:
                pts.append("%s : %s" % (c[0], c[1]))
        if pts:
            sp.append(("bul", pts))
    elif kind == "matrix":
        rows = deck.get("rows", [])
        pts = ["%s → %s" % (r[0], " ; ".join(r[1:])) for r in rows]
        if pts:
            sp.append(("bul", pts))
    elif kind == "process":
        steps = deck.get("steps", [])
        pts = ["Étape %d — %s : %s" % (i + 1, s[0], s[1])
               for i, s in enumerate(steps)]
        if pts:
            sp.append(("bul", pts))
    elif kind == "twocol":
        sp.append(("p", "Faire comparer les deux colonnes : la première montre "
                        "un point de vue, la seconde montre le complément ou la "
                        "bonne pratique attendue. L'intérêt est de faire verbaliser "
                        "les différences, pas seulement de les lire."))
        sp.append(("bul", ["Côté gauche : " + ", ".join(_plain_items(deck.get("left_items"))),
                           "Côté droit : " + ", ".join(_plain_items(deck.get("right_items")))]))
    elif kind == "exercise":
        sp.append(("inter", "Lancer l'activité en reformulant la consigne, puis "
                            "laisser les étudiants produire avant de corriger. "
                            "L'enseignant circule pour repérer les confusions."))
        sp.append(("bul", deck.get("tasks", [])))

    if deck.get("definition"):
        sp.append(("def", deck["definition"]))
    if deck.get("example"):
        sp.append(("ex", deck["example"]))
    if deck.get("warning"):
        sp.append(("warn", deck["warning"]))
    if deck.get("activity"):
        sp.append(("inter", deck["activity"]))
    if deck.get("note"):
        sp.append(("key", deck["note"]))
    if deck.get("takeaway"):
        sp.append(("key", deck["takeaway"]))
    else:
        sp.append(("key", "À retenir : la notion doit toujours être reliée à "
                          "un risque réel, à une décision de gouvernance ou à une "
                          "preuve attendue lors d'un audit."))
    if deck.get("transition"):
        sp.append(("trans", deck["transition"]))
    return sp


def A(kind, title, module, **deck):
    speech = deck.pop("speech", None)
    if speech is None:
        speech = _speech_auto(kind, title, deck)
    return S(kind, title, module=module, speech=speech, **deck)


def MODULE(number, title, subtitle, topics, objectives, lessons, exercise, summary):
    slides = [
        S("module", title, module=number, number="%02d" % number,
          subtitle=subtitle, topics=topics,
          speech=[
            ("p", "Nous ouvrons le module %d : %s. Ce module représente environ "
                  "quatre heures de cours et de travaux dirigés." % (number, title)),
            ("obj", "Le but est de transformer les notions du module en décisions "
                    "concrètes : quoi documenter, quoi justifier, quoi vérifier."),
          ]),
        A("objectives", "Objectifs du module %d" % number, module=number,
          kicker="Ce que vous saurez faire", accent="GOLD", items=objectives,
          teacher="Présenter les objectifs comme une feuille de route. Les étudiants "
                  "doivent comprendre que chaque objectif correspond à une compétence "
                  "réutilisable dans l'étude de cas fil rouge."),
    ]
    for lesson in lessons:
        lesson = dict(lesson)
        kind = lesson.pop("kind")
        title_ = lesson.pop("title")
        slides.append(A(kind, title_, module=number, **lesson))
    if exercise:
        slides.append(A("exercise", exercise["title"], module=number, **{
            k: v for k, v in exercise.items() if k != "title"
        }))
    slides.append(S("key", "L'essentiel du module %d" % number, module=number,
                    kicker="Synthèse", text=summary, attrib="Module %d" % number,
                    speech=[
                      ("p", "Cette diapositive clôt le module. L'enseignant la lit "
                            "lentement et relie chaque phrase à un exemple vu pendant "
                            "les quatre heures."),
                      ("key", summary),
                      ("trans", "On peut maintenant passer au module suivant, qui "
                                "réutilisera ce socle dans un contexte plus appliqué."),
                    ]))
    return slides


M2 = MODULE(
    2, "Gouvernance et cadre normatif",
    "Pourquoi les organisations ont besoin de règles, de rôles et de référentiels",
    ["Gouvernance SSI", "Norme, standard, règlement, référentiel", "Acteurs : ISO, NIST, ANSSI, CNIL, ENISA", "Famille ISO/IEC 27000", "Cycle PDCA"],
    [
        "Expliquer pourquoi la sécurité doit être gouvernée par la direction",
        "Distinguer norme, standard, règlement, guide et référentiel",
        "Identifier les principaux organismes de référence",
        "Situer la famille ISO/IEC 27000 dans un programme de sécurité",
        "Comprendre le cycle d'amélioration continue PDCA",
    ],
    [
      dict(kind="bullets", title="Pourquoi gouverner la sécurité ?", kicker="Enjeu",
           accent="TEAL",
           items=[
             "La sécurité est un risque d'entreprise : financier, juridique, opérationnel et d'image",
             "Elle nécessite des arbitrages : budget, priorités, acceptation du risque",
             "La direction fixe l'appétence au risque et les responsabilités",
             "Les équipes techniques appliquent une stratégie, elles ne la remplacent pas",
           ],
           example="Une équipe IT peut proposer d'acheter un EDR ; seule la direction peut arbitrer le budget, le périmètre et le risque résiduel accepté.",
           takeaway="La gouvernance transforme la sécurité d'un ensemble d'outils en système de décisions maîtrisées."),
      dict(kind="matrix", title="Norme, standard, règlement, référentiel", kicker="Vocabulaire",
           headers=["Terme", "Sens pratique"],
           rows=[
             ["Norme", "Document reconnu, souvent international, issu d'un organisme de normalisation"],
             ["Standard", "Pratique largement adoptée, parfois industrielle ou communautaire"],
             ["Règlement / loi", "Obligation juridique contraignante : non-respect = sanctions"],
             ["Guide", "Recommandations opérationnelles, souvent non obligatoires"],
             ["Référentiel", "Ensemble structuré d'exigences, contrôles ou critères d'évaluation"],
           ],
           definition="Une norme peut être volontaire, mais devenir obligatoire par contrat, règlement sectoriel ou exigence client.",
           warning="Ne pas confondre conformité à une norme et sécurité absolue : une organisation certifiée reste exposée aux risques."),
      dict(kind="cards", title="Les organismes à connaître", kicker="Écosystème",
           cols=3,
           cards=[
             ("ISO/IEC", "Normes internationales, dont la famille 27000", "GOLD"),
             ("NIST", "Référentiels américains très utilisés : CSF, SP 800", "TEAL"),
             ("ANSSI", "Autorité nationale française en cybersécurité", "BLUE"),
             ("CNIL", "Protection des données personnelles et RGPD", "RED"),
             ("ENISA", "Agence européenne de cybersécurité", "TEAL"),
             ("CIS / OWASP", "Bonnes pratiques opérationnelles et applicatives", "BLUE"),
           ],
           takeaway="Un professionnel ne connaît pas toutes les normes par cœur ; il sait où chercher la bonne référence."),
      dict(kind="cards", title="La famille ISO/IEC 27000", kicker="Cartographie",
           cols=2,
           cards=[
             ("ISO/IEC 27000", "Vocabulaire et vue d'ensemble des SMSI", "GREY"),
             ("ISO/IEC 27001", "Exigences certifiables du SMSI", "GOLD"),
             ("ISO/IEC 27002", "Mesures de sécurité et guide de bonnes pratiques", "TEAL"),
             ("ISO/IEC 27005", "Gestion des risques de sécurité de l'information", "BLUE"),
             ("ISO/IEC 27017 / 27018", "Sécurité cloud et données personnelles dans le cloud", "BLUE"),
             ("ISO/IEC 27701", "Extension management de la vie privée", "RED"),
           ],
           note="27001 dit ce qui est exigé ; 27002 aide à choisir et mettre en œuvre les mesures."),
      dict(kind="twocol", title="Exigences vs mesures de sécurité", kicker="Lire correctement une norme",
           left_head="Exigence",
           left_items=[
             "Ce qui doit être démontré",
             "Souvent formulé en « l'organisation doit… »",
             "Vérifiable lors d'un audit",
             "Exemple : réaliser des audits internes planifiés",
           ],
           right_head="Mesure / contrôle",
           right_items=[
             "Ce qui traite concrètement un risque",
             "Peut être organisationnel, humain, physique ou technique",
             "Doit être justifié par l'analyse de risque",
             "Exemple : MFA, sauvegardes, classification",
           ],
           left_color="GOLD", right_color="TEAL",
           takeaway="Un audit vérifie des exigences ; un plan de sécurité met en œuvre des mesures."),
      dict(kind="process", title="Le cycle PDCA", kicker="Amélioration continue",
           steps=[
             ("Plan", "Comprendre le contexte, fixer objectifs, évaluer les risques"),
             ("Do", "Mettre en œuvre politiques, processus et mesures"),
             ("Check", "Mesurer, auditer, analyser les incidents et indicateurs"),
             ("Act", "Corriger, améliorer, réviser le plan et les priorités"),
           ],
           example="Une campagne de sensibilisation n'est pas terminée quand elle est diffusée : on mesure les résultats, on corrige le contenu et on recommence."),
      dict(kind="matrix", title="Rôles de gouvernance SSI", kicker="Qui décide ?",
           headers=["Rôle", "Responsabilité typique"],
           rows=[
             ["Direction", "Fixe l'appétence au risque, approuve les moyens et arbitre"],
             ["RSSI / CISO", "Anime la stratégie, conseille, coordonne et rend compte"],
             ["DSI", "Met en œuvre les moyens techniques et l'exploitation"],
             ["Métiers", "Expriment les besoins, possèdent les risques métier"],
             ["Juridique / DPO", "Traite obligations contractuelles, RGPD et preuves"],
             ["Auditeur", "Évalue objectivement la conformité et l'efficacité"],
           ],
           note="Un risque appartient au métier qui porte l'activité, pas uniquement à l'IT."),
      dict(kind="bullets", title="La documentation : preuve et mémoire", kicker="Gouvernance",
           accent="BLUE",
           items=[
             "Politique de sécurité : intention et engagements de haut niveau",
             "Procédures : comment réaliser une activité de façon répétable",
             "Enregistrements : preuves qu'une activité a bien été faite",
             "Versioning, approbation, diffusion et revue périodique sont essentiels",
             "Sans preuve, l'auditeur considère souvent que l'action n'est pas démontrée",
           ],
           warning="Documenter ne veut pas dire produire du papier inutile : chaque document doit soutenir une décision, une pratique ou une preuve."),
    ],
    dict(title="TD — Cartographier l'écosystème normatif", kicker="Travaux dirigés",
         duration="35 min",
         brief="À partir d'une organisation fictive (PME e-commerce, clinique, université), identifier les référentiels utiles.",
         tasks=[
           "Lister 5 parties prenantes : clients, régulateurs, fournisseurs, direction, utilisateurs",
           "Associer à chacune au moins une attente de sécurité",
           "Choisir les référentiels pertinents : ISO 27001, RGPD, guide ANSSI, NIST CSF, CIS",
           "Justifier ce qui relève de l'obligation, de la bonne pratique ou de l'exigence contractuelle",
         ],
         deliverable="Une carte parties prenantes → exigences → référentiels."),
    "La gouvernance donne un cadre aux décisions de sécurité. Les normes et référentiels ne remplacent pas le jugement : ils structurent les responsabilités, les preuves et l'amélioration continue."
)


M3 = MODULE(
    3, "ISO/IEC 27001:2022 — construire un SMSI",
    "Le système de management de la sécurité de l'information, ses clauses et son audit",
    ["SMSI", "Clauses 4 à 10", "Périmètre", "SoA", "Certification", "Amélioration continue"],
    [
        "Définir ce qu'est un SMSI et ce qu'il n'est pas",
        "Expliquer les clauses 4 à 10 d'ISO/IEC 27001:2022",
        "Rédiger les éléments clés d'un périmètre SMSI",
        "Comprendre le rôle central de la déclaration d'applicabilité",
        "Décrire le cycle de certification et de surveillance",
    ],
    [
      dict(kind="bullets", title="Un SMSI, ce n'est pas un logiciel", kicker="Définition",
           accent="TEAL",
           items=[
             "SMSI = système de management de la sécurité de l'information",
             "Ensemble coordonné : politiques, processus, rôles, mesures, preuves",
             "Objectif : gérer durablement les risques liés à l'information",
             "Il s'intègre aux processus de l'organisation et s'améliore en continu",
           ],
           definition="Un SMSI est un système de pilotage. Il organise les décisions de sécurité, leur mise en œuvre, leur contrôle et leur amélioration."),
      dict(kind="matrix", title="Les clauses 4 à 10", kicker="Structure ISO 27001",
           headers=["Clause", "Question à laquelle elle répond"],
           rows=[
             ["4 · Contexte", "Qui sommes-nous, quelles attentes, quel périmètre ?"],
             ["5 · Leadership", "Qui porte la sécurité et avec quelle politique ?"],
             ["6 · Planification", "Quels risques, objectifs et plans de traitement ?"],
             ["7 · Support", "Quelles ressources, compétences, communications, preuves ?"],
             ["8 · Opération", "Comment exécute-t-on les processus du SMSI ?"],
             ["9 · Évaluation", "Comment mesure-t-on, audite-t-on, révise-t-on ?"],
             ["10 · Amélioration", "Comment corriger et améliorer en continu ?"],
           ],
           note="Ces clauses sont les exigences certifiables : l'auditeur les vérifie systématiquement."),
      dict(kind="bullets", title="Définir le périmètre du SMSI", kicker="Clause 4",
           accent="GOLD",
           items=[
             "Inclure : entités, sites, processus, systèmes, données, interfaces",
             "Justifier les exclusions : elles doivent être cohérentes et défendables",
             "Identifier les parties intéressées et leurs exigences",
             "Relier le périmètre aux risques et aux objectifs métier",
           ],
           example="Une startup SaaS peut définir un SMSI limité à la plateforme cloud de production et aux processus support, sans inclure tous les postes personnels hors périmètre."),
      dict(kind="twocol", title="Leadership : engagements attendus", kicker="Clause 5",
           left_head="Ce que l'auditeur cherche",
           left_items=[
             "Une politique approuvée par la direction",
             "Des responsabilités attribuées et connues",
             "Des ressources effectivement allouées",
             "Des preuves de revues et décisions",
           ],
           right_head="Signes de faiblesse",
           right_items=[
             "Politique copiée-collée non connue",
             "RSSI isolé sans pouvoir d'arbitrage",
             "Objectifs sécurité non suivis",
             "Aucune trace de décision de direction",
           ],
           left_color="TEAL", right_color="RED"),
      dict(kind="process", title="Planification : risques → objectifs", kicker="Clause 6",
           steps=[
             ("Critères de risque", "Définir échelles, seuils d'acceptation et responsabilités"),
             ("Appréciation", "Identifier, analyser et évaluer les risques"),
             ("Traitement", "Choisir mesures, acceptation, transfert ou évitement"),
             ("Objectifs", "Fixer des objectifs mesurables et un plan pour les atteindre"),
           ],
           takeaway="La clause 6 relie directement analyse de risque, choix des mesures et objectifs du SMSI."),
      dict(kind="cards", title="Support : faire vivre le système", kicker="Clause 7",
           cols=3,
           cards=[
             ("Ressources", "Budget, outils, temps, responsabilités", "GOLD"),
             ("Compétence", "Former les personnes selon leurs rôles", "TEAL"),
             ("Sensibilisation", "Faire comprendre la politique et les impacts", "TEAL"),
             ("Communication", "Qui communique quoi, quand, à qui ?", "BLUE"),
             ("Information documentée", "Créer, mettre à jour, maîtriser les preuves", "BLUE"),
             ("Traçabilité", "Démontrer que le SMSI fonctionne réellement", "RED"),
           ],
           note="Le SMSI ne vit pas dans un classeur : il vit dans les habitudes et les preuves."),
      dict(kind="process", title="Opération, évaluation, amélioration", kicker="Clauses 8, 9, 10",
           steps=[
             ("Opérer", "Exécuter les processus : risques, traitements, contrôles"),
             ("Mesurer", "Suivre indicateurs, incidents, écarts, efficacité"),
             ("Auditer", "Vérifier objectivement conformité et fonctionnement"),
             ("Revoir", "La direction arbitre sur la base des résultats"),
             ("Corriger", "Traiter non-conformités et améliorer le SMSI"),
           ],
           example="Une non-conformité n'est pas un échec : c'est une opportunité de rendre le système plus robuste."),
      dict(kind="matrix", title="La déclaration d'applicabilité (SoA)", kicker="Document central",
           headers=["Contenu", "Pourquoi c'est important"],
           rows=[
             ["Mesures nécessaires", "Montre ce que l'organisation a choisi de mettre en place"],
             ["Justification d'inclusion", "Relie chaque mesure au risque ou à l'exigence"],
             ["Statut de mise en œuvre", "Indique ce qui est fait, partiel ou prévu"],
             ["Justification d'exclusion", "Explique pourquoi une mesure Annex A n'est pas retenue"],
             ["Lien au plan de traitement", "Fait le pont entre risques, décisions et actions"],
           ],
           warning="Une SoA générique sans lien au registre des risques est une faiblesse majeure en audit."),
      dict(kind="process", title="Le cycle de certification", kicker="Audit externe",
           steps=[
             ("Préparation", "Gap analysis, preuves, audit interne, revue de direction"),
             ("Stage 1", "Revue documentaire : le SMSI est-il prêt ?"),
             ("Stage 2", "Audit de mise en œuvre : le SMSI fonctionne-t-il ?"),
             ("Surveillance", "Audits annuels partiels pendant le cycle"),
             ("Recertification", "Audit complet tous les trois ans"),
           ],
           note="La certification prouve un système maîtrisé à un instant donné ; elle n'élimine pas les risques."),
    ],
    dict(title="TD — Définir un périmètre SMSI", kicker="Travaux dirigés",
         duration="45 min",
         brief="Pour une PME SaaS fictive, rédiger un périmètre ISO 27001 défendable.",
         tasks=[
           "Décrire l'activité, les clients et les informations sensibles",
           "Inclure/exclure sites, équipes, systèmes et processus",
           "Identifier 5 parties intéressées et leurs attentes",
           "Rédiger une phrase de périmètre en langage audit",
         ],
         deliverable="Un paragraphe de périmètre + une liste d'exclusions justifiées."),
    "ISO/IEC 27001:2022 structure le SMSI autour d'un cycle de management : contexte, leadership, planification, support, opération, évaluation et amélioration. Le périmètre, le registre de risques et la SoA en sont les pièces maîtresses."
)


M4 = MODULE(
    4, "ISO/IEC 27002:2022 — choisir et appliquer les mesures",
    "Comprendre les 93 mesures de sécurité, leurs thèmes et leur sélection par le risque",
    ["27001 vs 27002", "93 mesures", "4 thèmes", "11 nouveautés 2022", "Attributs", "Sélection des contrôles"],
    [
        "Différencier ISO/IEC 27001 et ISO/IEC 27002",
        "Présenter les 4 thèmes et 93 mesures de l'édition 2022",
        "Classer les mesures selon leur type et leur objectif",
        "Choisir des mesures à partir d'un risque identifié",
        "Documenter l'applicabilité et les preuves attendues",
    ],
    [
      dict(kind="twocol", title="ISO 27001 vs ISO 27002", kicker="Complémentarité",
           left_head="ISO/IEC 27001",
           left_items=[
             "Standard d'exigences certifiable",
             "Définit le SMSI et ses clauses",
             "Demande d'identifier et traiter les risques",
             "Annex A sert de référence de mesures",
           ],
           right_head="ISO/IEC 27002",
           right_items=[
             "Guide de bonnes pratiques",
             "Explique les mesures de sécurité",
             "Aide à les sélectionner et les mettre en œuvre",
             "Non certifiable directement",
           ],
           left_color="GOLD", right_color="TEAL",
           takeaway="27001 pose les exigences ; 27002 éclaire le choix et l'application des contrôles."),
      dict(kind="cards", title="ISO/IEC 27002:2022 en chiffres", kicker="Structure",
           cols=2,
           cards=[
             ("93 mesures", "Référence Annex A alignée ISO 27001:2022", "GOLD"),
             ("4 thèmes", "Organisationnel, personnes, physique, technologique", "TEAL"),
             ("11 nouvelles mesures", "Cloud, threat intelligence, secure coding, DLP…", "BLUE"),
             ("Attributs", "Vues par type, propriétés DICP, concepts cyber, capacités", "RED"),
           ],
           note="L'édition 2022 simplifie la structure : 114 contrôles/14 domaines en 2013 → 93 mesures/4 thèmes."),
      dict(kind="cards", title="Thème 1 — Mesures organisationnelles", kicker="A.5 · 37 mesures",
           cols=3,
           cards=[
             ("Politiques", "Règles et responsabilités de sécurité", "GOLD"),
             ("Gestion des actifs", "Inventaire, classification, usage acceptable", "TEAL"),
             ("Fournisseurs", "Contrats, exigences, surveillance, supply chain", "BLUE"),
             ("Cloud", "Sécurité de l'utilisation des services cloud", "BLUE"),
             ("Incidents", "Préparation, décision, réponse, preuve, retour d'expérience", "RED"),
             ("Conformité", "Lois, propriété intellectuelle, données personnelles", "GOLD"),
           ],
           takeaway="Le plus grand thème est organisationnel : la norme rappelle que la sécurité est d'abord pilotée."),
      dict(kind="cards", title="Thème 2 — Personnes", kicker="A.6 · 8 mesures",
           cols=2,
           cards=[
             ("Avant l'emploi", "Screening proportionné, conditions d'emploi", "GOLD"),
             ("Pendant l'emploi", "Sensibilisation, formation, processus disciplinaire", "TEAL"),
             ("Changement / départ", "Responsabilités après terminaison ou changement", "RED"),
             ("Télétravail & signalement", "Règles hors site et canal de remontée d'événements", "BLUE"),
           ],
           example="Un départ collaborateur doit déclencher restitution des actifs, révocation des accès et rappel des engagements de confidentialité."),
      dict(kind="cards", title="Thème 3 — Physique", kicker="A.7 · 14 mesures",
           cols=2,
           cards=[
             ("Périmètres", "Zones, badges, visiteurs, salles sensibles", "GOLD"),
             ("Surveillance", "Détection intrusion, vidéo, journal visiteurs", "TEAL"),
             ("Environnement", "Feu, eau, énergie, climatisation, protections", "BLUE"),
             ("Équipements", "Positionnement, maintenance, effacement, destruction", "RED"),
           ],
           warning="Le cloud ne supprime pas le physique : il le transfère partiellement au fournisseur, à vérifier contractuellement."),
      dict(kind="cards", title="Thème 4 — Technologique", kicker="A.8 · 34 mesures",
           cols=3,
           cards=[
             ("Identités & accès", "Authentification, privilèges, restriction", "GOLD"),
             ("Postes & malware", "Terminaux, anti-malware, filtrage web", "TEAL"),
             ("Vulnérabilités", "Patch, configuration, durcissement", "BLUE"),
             ("Données", "Chiffrement, masquage, suppression, DLP", "RED"),
             ("Réseau & logs", "Segmentation, services réseau, journalisation", "BLUE"),
             ("Développement", "Cycle de vie sécurisé, exigences, test, code sûr", "GOLD"),
           ],
           note="Les mesures techniques ne se choisissent pas seules : elles doivent répondre à un risque ou une exigence."),
      dict(kind="matrix", title="Les 11 nouvelles mesures de l'édition 2022", kicker="Mise à jour",
           headers=["Mesure", "Pourquoi elle apparaît"],
           rows=[
             ["A.5.7 Threat intelligence", "Mieux intégrer la connaissance de la menace"],
             ["A.5.23 Cloud services", "Clarifier la responsabilité partagée du cloud"],
             ["A.5.30 ICT readiness", "Relier sécurité et continuité d'activité"],
             ["A.7.4 Physical monitoring", "Surveiller les accès physiques"],
             ["A.8.9 Configuration", "Maîtriser les configurations et dérives"],
             ["A.8.10 Information deletion", "Supprimer correctement les données"],
             ["A.8.11 Data masking", "Limiter l'exposition des données sensibles"],
             ["A.8.12 DLP", "Réduire les fuites d'information"],
             ["A.8.16 Monitoring", "Détecter les comportements anormaux"],
             ["A.8.23 Web filtering", "Réduire les accès web dangereux"],
             ["A.8.28 Secure coding", "Prévenir les vulnérabilités applicatives"],
           ],
           note="Ces nouveautés reflètent l'évolution du cloud, du développement logiciel et de la menace."),
      dict(kind="matrix", title="Attributs des mesures", kicker="Créer des vues utiles",
           headers=["Attribut", "Utilité"],
           rows=[
             ["Type", "Préventif, détectif, correctif"],
             ["Propriétés sécurité", "Confidentialité, intégrité, disponibilité"],
             ["Concept cyber", "Identifier, protéger, détecter, répondre, rétablir"],
             ["Capacité opérationnelle", "IAM, gouvernance, sécurité applicative, continuité…"],
             ["Domaine de sécurité", "Gouvernance, protection, défense, résilience"],
           ],
           example="Une mesure de journalisation est détective, soutient la preuve et sert surtout la détection/réponse."),
      dict(kind="process", title="Sélectionner une mesure par le risque", kicker="Méthode",
           steps=[
             ("Scénario", "Formuler un risque clair : menace + vulnérabilité + impact"),
             ("Besoin", "Identifier le critère DICP à protéger"),
             ("Options", "Comparer mesures possibles : coût, efficacité, faisabilité"),
             ("Choix", "Documenter inclusion/exclusion dans la SoA"),
             ("Preuve", "Définir comment l'efficacité sera démontrée"),
           ],
           takeaway="Un contrôle est fort quand il est justifié, implémenté, prouvé et revu."),
    ],
    dict(title="TD — Choisir des contrôles ISO 27002", kicker="Travaux dirigés",
         duration="50 min",
         brief="À partir d'un risque de fuite de données clients, sélectionner des mesures ISO 27002 adaptées.",
         tasks=[
           "Formuler le risque et le critère DICP principal",
           "Choisir 6 mesures : au moins une organisationnelle, une humaine et une technique",
           "Justifier chaque mesure par rapport au risque",
           "Indiquer une preuve d'audit attendue pour chaque mesure",
         ],
         deliverable="Mini-SoA : mesure → justification → preuve attendue."),
    "ISO/IEC 27002:2022 est une boîte à outils de 93 mesures. On ne les applique pas mécaniquement : on les sélectionne selon les risques, les exigences et les preuves attendues."
)


M5 = MODULE(
    5, "Méthodes de gestion des risques",
    "ISO 27005 et EBIOS Risk Manager v1.5 : de l'analyse au plan de traitement",
    ["Critères de risque", "Identification", "Analyse", "Traitement", "EBIOS RM 1.5", "Plan de traitement"],
    [
        "Construire un vocabulaire solide du risque",
        "Décrire le cycle ISO 27005 aligné avec ISO 31000",
        "Évaluer impact et vraisemblance avec des critères explicites",
        "Dérouler les 5 ateliers EBIOS Risk Manager v1.5",
        "Produire un registre de risques et un plan de traitement",
    ],
    [
      dict(kind="process", title="Cycle de gestion du risque", kicker="ISO 27005 / ISO 31000",
           steps=[
             ("Contexte", "Périmètre, critères, parties prenantes, objectifs"),
             ("Appréciation", "Identifier, analyser, évaluer les risques"),
             ("Traitement", "Modifier, éviter, transférer ou accepter le risque"),
             ("Communication", "Partager décisions et responsabilités"),
             ("Surveillance", "Réviser selon incidents, changements et indicateurs"),
           ],
           note="Le risque est dynamique : une analyse non mise à jour devient rapidement fausse."),
      dict(kind="matrix", title="Définir les critères de risque", kicker="Avant d'évaluer",
           headers=["Critère", "Question pratique"],
           rows=[
             ["Échelle d'impact", "Quels niveaux : mineur, significatif, majeur, critique ?"],
             ["Échelle de vraisemblance", "Sur quoi se fonde-t-on : exposition, menace, maturité ?"],
             ["Seuil d'acceptation", "À partir de quel niveau faut-il traiter ?"],
             ["Propriétaires", "Qui décide d'accepter un risque résiduel ?"],
             ["Catégories d'impact", "Financier, juridique, image, opérationnel, humain"],
           ],
           warning="Changer les critères en cours d'analyse pour obtenir un résultat souhaité détruit la crédibilité de la démarche."),
      dict(kind="bullets", title="Identifier les risques", kicker="Créer les scénarios",
           accent="TEAL",
           items=[
             "Partir des valeurs métier et biens supports",
             "Associer sources de menace, vulnérabilités et événements redoutés",
             "Formuler le risque comme un scénario compréhensible",
             "Éviter les formulations vagues : « cyberattaque » n'est pas un risque assez précis",
             "Documenter hypothèses et sources utilisées",
           ],
           example="« Un attaquant obtient un compte administrateur via phishing et exfiltre la base clients » est plus utile que « piratage du SI »."),
      dict(kind="matrix", title="Analyser : impact × vraisemblance", kicker="Évaluer",
           headers=["Dimension", "À observer"],
           rows=[
             ["Impact", "Conséquences sur DICP, finance, juridique, image, continuité"],
             ["Vraisemblance", "Exposition, facilité d'exploitation, niveau de menace, contrôles existants"],
             ["Risque initial", "Niveau avant mesures additionnelles"],
             ["Risque résiduel", "Niveau après traitement prévu"],
             ["Priorité", "Décision : traiter maintenant, surveiller, accepter"],
           ],
           note="Une matrice de risque n'est qu'un outil de décision : elle ne remplace pas l'argumentation."),
      dict(kind="cards", title="Options de traitement", kicker="Décider",
           cols=2,
           cards=[
             ("Modifier / réduire", "Mettre en place des mesures pour diminuer impact ou vraisemblance", "TEAL"),
             ("Éviter", "Arrêter ou changer l'activité trop risquée", "RED"),
             ("Partager / transférer", "Assurance, contrat, externalisation partielle", "BLUE"),
             ("Accepter", "Assumer le risque résiduel à un niveau autorisé", "GOLD"),
           ],
           warning="Transférer n'efface pas le risque : l'organisation reste responsable vis-à-vis de ses clients et régulateurs."),
      dict(kind="process", title="EBIOS Risk Manager v1.5 : vue d'ensemble", kicker="Méthode ANSSI",
           steps=[
             ("Atelier 1", "Cadrage et socle de sécurité"),
             ("Atelier 2", "Sources de risque et objectifs visés"),
             ("Atelier 3", "Scénarios stratégiques dans l'écosystème"),
             ("Atelier 4", "Scénarios opérationnels techniques"),
             ("Atelier 5", "Traitement du risque et suivi"),
           ],
           note="La version 1.5 publiée par l'ANSSI en 2024 est alignée avec ISO 27005:2022."),
      dict(kind="bullets", title="Atelier 1 — Cadrage et socle", kicker="EBIOS RM",
           accent="GOLD",
           items=[
             "Définir l'objet de l'étude et le cadre temporel",
             "Identifier missions, valeurs métier et biens supports",
             "Identifier les événements redoutés et leur gravité",
             "Évaluer les écarts au socle de sécurité existant",
           ],
           takeaway="Si le périmètre est flou, toute l'analyse de risque sera floue."),
      dict(kind="bullets", title="Atelier 2 — Sources de risque", kicker="EBIOS RM",
           accent="RED",
           items=[
             "Identifier qui pourrait attaquer ou nuire",
             "Associer chaque source à un objectif visé",
             "Évaluer motivation, ressources et activité",
             "Retenir les couples source de risque / objectif visé pertinents",
           ],
           example="Source : cybercriminels ; objectif : obtenir une rançon ; cible : disponibilité du service client."),
      dict(kind="bullets", title="Atelier 3 — Scénarios stratégiques", kicker="EBIOS RM",
           accent="BLUE",
           items=[
             "Cartographier l'écosystème : fournisseurs, partenaires, clients, prestataires",
             "Évaluer la dangerosité des parties prenantes",
             "Construire des chemins d'attaque de haut niveau",
             "Associer les scénarios aux événements redoutés et à la gravité",
           ],
           note="Les attaques passent souvent par l'écosystème : fournisseur, compte prestataire, API tierce."),
      dict(kind="bullets", title="Atelier 4 — Scénarios opérationnels", kicker="EBIOS RM",
           accent="TEAL",
           items=[
             "Traduire les chemins stratégiques en modes opératoires techniques",
             "Identifier les actions élémentaires sur biens supports",
             "Évaluer la vraisemblance de chaque scénario opérationnel",
             "Produire une synthèse des scénarios de risque",
           ],
           example="Phishing d'un administrateur → vol de jeton MFA → accès VPN → extraction base clients."),
      dict(kind="process", title="Atelier 5 — Traitement et suivi", kicker="EBIOS RM",
           steps=[
             ("Synthèse", "Classer les risques selon leur niveau"),
             ("Stratégie", "Décider traitement, acceptation ou évitement"),
             ("Mesures", "Définir actions, responsables, échéances"),
             ("Résiduel", "Évaluer et faire accepter le risque restant"),
             ("Suivi", "Mettre à jour selon incidents, changements et menaces"),
           ],
           takeaway="Le livrable important n'est pas seulement la matrice : c'est le plan de traitement suivi dans le temps."),
    ],
    dict(title="TD — Construire un scénario EBIOS", kicker="Travaux dirigés",
         duration="60 min",
         brief="Sur le cas d'une plateforme de notes universitaires, construire un scénario EBIOS simplifié.",
         tasks=[
           "Identifier 2 valeurs métier et 2 événements redoutés",
           "Choisir 1 source de risque et 1 objectif visé",
           "Décrire un scénario stratégique via un fournisseur ou utilisateur",
           "Décrire un scénario opérationnel en 4 actions élémentaires",
           "Proposer 4 mesures de traitement",
         ],
         deliverable="Fiche scénario : SR/OV, chemin stratégique, mode opératoire, mesures."),
    "La gestion des risques transforme une peur générale en scénarios discutables, priorisables et traitables. ISO 27005 donne le cadre ; EBIOS RM fournit une méthode concrète par ateliers."
)


M6 = MODULE(
    6, "NIST CSF 2.0 et autres référentiels",
    "Comparer, cartographier et utiliser plusieurs cadres de sécurité sans se perdre",
    ["NIST CSF 2.0", "Core, Profiles, Tiers", "CIS Controls", "OWASP", "COBIT / ITIL", "Mappings"],
    [
        "Présenter les composants du NIST Cybersecurity Framework 2.0",
        "Expliquer les 6 fonctions : Govern, Identify, Protect, Detect, Respond, Recover",
        "Utiliser les profils current/target pour prioriser",
        "Situer CIS Controls, OWASP, COBIT, PCI DSS et SOC 2",
        "Construire une cartographie entre référentiels",
    ],
    [
      dict(kind="cards", title="NIST CSF 2.0 : les composants", kicker="Cadre flexible",
           cols=3,
           cards=[
             ("Core", "Taxonomie d'objectifs de cybersécurité", "GOLD"),
             ("Profiles", "État courant et état cible adaptés à l'organisation", "TEAL"),
             ("Tiers", "Maturité de gouvernance et gestion du risque", "BLUE"),
           ],
           note="CSF 2.0 est volontaire et non prescriptif : il décrit des résultats attendus, pas une check-list unique."),
      dict(kind="cards", title="Les 6 fonctions du NIST CSF 2.0", kicker="Cycle cyber",
           cols=3,
           cards=[
             ("Govern", "Stratégie, rôles, politiques, supply chain", "GOLD"),
             ("Identify", "Actifs, risques, améliorations, contexte", "BLUE"),
             ("Protect", "Accès, formation, données, plateformes", "TEAL"),
             ("Detect", "Surveillance et détection d'événements", "ORANGE"),
             ("Respond", "Gestion et communication d'incident", "RED"),
             ("Recover", "Rétablissement et amélioration", "TEAL"),
           ],
           note="La fonction Govern a été ajoutée dans CSF 2.0 pour rendre visible la gouvernance."),
      dict(kind="process", title="Créer un profil CSF", kicker="Current → Target",
           steps=[
             ("Scope", "Définir l'activité ou le périmètre évalué"),
             ("Current profile", "Décrire l'état actuel face aux outcomes CSF"),
             ("Target profile", "Définir l'état cible selon risques et obligations"),
             ("Gap", "Identifier écarts et priorités"),
             ("Roadmap", "Planifier les actions et mesurer les progrès"),
           ],
           example="Une PME peut viser un Target Profile plus ambitieux sur Respond/Recover si elle dépend fortement de sa plateforme en ligne."),
      dict(kind="matrix", title="Tiers CSF : maturité de gestion du risque", kicker="Niveaux",
           headers=["Tier", "Sens"],
           rows=[
             ["1 · Partial", "Pratiques ad hoc, peu formalisées"],
             ["2 · Risk informed", "Risques connus mais approche pas toujours répétable"],
             ["3 · Repeatable", "Processus formalisés, gouvernance établie"],
             ["4 · Adaptive", "Amélioration continue, anticipation et adaptation"],
           ],
           note="Les Tiers ne sont pas une note de performance ; ils aident à choisir un niveau adapté au contexte."),
      dict(kind="matrix", title="Mapping ISO 27001 ↔ NIST CSF", kicker="Traduire les cadres",
           headers=["Besoin", "Lecture ISO / NIST"],
           rows=[
             ["Gouvernance", "ISO clauses 4-6 ↔ CSF Govern"],
             ["Inventaire actifs", "ISO A.5.9 ↔ CSF Identify"],
             ["Accès", "ISO A.5.15/A.8.2 ↔ CSF Protect"],
             ["Logs", "ISO A.8.15/A.8.16 ↔ CSF Detect"],
             ["Incident", "ISO A.5.24-5.28 ↔ CSF Respond"],
             ["Continuité", "ISO A.5.29/A.5.30 ↔ CSF Recover"],
           ],
           takeaway="Le mapping évite les doublons et permet de parler à plusieurs parties prenantes avec leur référentiel."),
      dict(kind="cards", title="CIS Controls", kicker="Hygiène opérationnelle",
           cols=2,
           cards=[
             ("Priorisé", "Mesures concrètes classées pour démarrer vite", "GOLD"),
             ("Technique", "Inventaire, configuration, vulnérabilités, logs", "TEAL"),
             ("Groupes IG", "Implementation Groups adaptés à la maturité", "BLUE"),
             ("Complément ISO", "Très utile pour opérationnaliser les exigences", "RED"),
           ],
           example="Une petite structure peut commencer par les contrôles CIS d'inventaire et de configuration avant de viser une certification ISO."),
      dict(kind="cards", title="OWASP, SAMM, ASVS", kicker="Sécurité applicative",
           cols=3,
           cards=[
             ("OWASP Top 10", "Risques applicatifs les plus courants", "RED"),
             ("ASVS", "Exigences de vérification applicative", "GOLD"),
             ("SAMM", "Modèle de maturité du développement sécurisé", "TEAL"),
           ],
           note="Pour les applications, ISO 27002 donne le cadre ; OWASP donne le détail opérationnel."),
      dict(kind="cards", title="COBIT, ITIL, PCI DSS, SOC 2", kicker="Autres cadres",
           cols=2,
           cards=[
             ("COBIT", "Gouvernance et management de l'IT", "BLUE"),
             ("ITIL", "Gestion des services IT et processus opérationnels", "TEAL"),
             ("PCI DSS", "Exigences pour les données de cartes de paiement", "RED"),
             ("SOC 2", "Rapport d'assurance sur contrôles de service (Trust Services Criteria)", "GOLD"),
           ],
           warning="Chaque cadre a son objectif : les mélanger sans comprendre leur périmètre produit une conformité confuse."),
      dict(kind="process", title="Méthode pour ne pas se perdre", kicker="Multi-référentiels",
           steps=[
             ("Périmètre", "Quel service, données, organisation ?"),
             ("Obligatoire", "Quelles lois ou exigences client s'imposent ?"),
             ("Référence principale", "Choisir le cadre de pilotage : souvent ISO ou NIST"),
             ("Mappings", "Relier les autres cadres aux contrôles existants"),
             ("Preuves communes", "Mutualiser preuves, audits et indicateurs"),
           ],
           takeaway="Une bonne GRC réduit les doublons : un contrôle bien documenté peut répondre à plusieurs exigences."),
    ],
    dict(title="TD — Construire un profil NIST CSF simplifié", kicker="Travaux dirigés",
         duration="45 min",
         brief="Pour une PME qui subit beaucoup de phishing, créer un mini Current/Target Profile.",
         tasks=[
           "Choisir 8 outcomes répartis sur Govern, Protect, Detect, Respond",
           "Décrire l'état actuel en une phrase par outcome",
           "Définir l'état cible et le Tier souhaité",
           "Prioriser 5 actions de progression",
         ],
         deliverable="Tableau current → target → actions."),
    "Le NIST CSF 2.0 aide à communiquer et prioriser. ISO structure le SMSI, CIS et OWASP opérationnalisent, COBIT/ITIL gouvernent l'IT : l'enjeu est de cartographier plutôt que d'empiler."
)


M7 = MODULE(
    7, "Politiques de sécurité et mesures concrètes",
    "Passer des référentiels aux règles applicables dans l'organisation",
    ["PSSI", "IAM", "Classification", "Cryptographie", "Journalisation", "Vulnérabilités", "Fournisseurs"],
    [
        "Structurer une politique de sécurité et ses documents associés",
        "Définir les règles essentielles d'accès, d'identité et de privilèges",
        "Relier classification de l'information et mesures de protection",
        "Comprendre les exigences de chiffrement, logs, vulnérabilités et fournisseurs",
        "Produire une procédure simple et audit-able",
    ],
    [
      dict(kind="process", title="Hiérarchie documentaire sécurité", kicker="PSSI",
           steps=[
             ("Politique", "Engagements de haut niveau approuvés par la direction"),
             ("Standards", "Règles obligatoires par domaine : mots de passe, cloud, logs"),
             ("Procédures", "Modes opératoires répétables : créer un compte, traiter un incident"),
             ("Guides", "Aide pratique et recommandations pour les utilisateurs"),
             ("Enregistrements", "Preuves : tickets, journaux, revues, attestations"),
           ],
           note="Plus on descend dans la hiérarchie, plus le document doit être concret et vérifiable."),
      dict(kind="cards", title="IAM : gérer les identités et accès", kicker="Contrôle fondamental",
           cols=3,
           cards=[
             ("Joiner", "Créer l'identité et les droits à l'arrivée", "TEAL"),
             ("Mover", "Modifier les droits lors d'un changement de poste", "GOLD"),
             ("Leaver", "Révoquer immédiatement au départ", "RED"),
             ("MFA", "Ajouter un facteur d'authentification", "BLUE"),
             ("PAM", "Contrôler les comptes à privilèges", "RED"),
             ("Revue", "Vérifier régulièrement les droits", "GOLD"),
           ],
           takeaway="L'IAM est souvent la mesure la plus structurante : elle réduit les abus, les erreurs et les compromissions."),
      dict(kind="twocol", title="Moindre privilège vs privilèges permanents", kicker="Accès",
           left_head="Risque",
           left_items=[
             "Comptes admin utilisés au quotidien",
             "Droits jamais retirés après mutation",
             "Comptes partagés sans traçabilité",
             "Prestataires avec accès trop larges",
           ],
           right_head="Bonne pratique",
           right_items=[
             "Droits just-in-time ou limités",
             "Revue périodique par le métier",
             "Comptes nominatifs et journaux",
             "Accès prestataire bornés et surveillés",
           ],
           left_color="RED", right_color="TEAL"),
      dict(kind="cards", title="Classification de l'information", kicker="Protéger selon la valeur",
           cols=2,
           cards=[
             ("Public", "Diffusion sans dommage significatif", "GREY"),
             ("Interne", "Usage réservé à l'organisation", "BLUE"),
             ("Confidentiel", "Impact fort en cas de divulgation", "GOLD"),
             ("Secret / très sensible", "Accès très restreint, mesures renforcées", "RED"),
           ],
           example="Un support de cours public, une liste d'étudiants interne, un dossier médical confidentiel, une clé de chiffrement secrète."),
      dict(kind="bullets", title="Cryptographie : objectifs et limites", kicker="Mesure technique",
           accent="GOLD",
           items=[
             "Chiffrement en transit : protéger les échanges (TLS, VPN)",
             "Chiffrement au repos : protéger fichiers, disques, bases",
             "Gestion des clés : création, stockage, rotation, révocation",
             "Signature : garantir origine et intégrité",
             "La cryptographie ne corrige pas une mauvaise gestion des accès",
           ],
           warning="Le vrai problème est souvent la gestion des clés, pas l'algorithme."),
      dict(kind="bullets", title="Journalisation et supervision", kicker="Détecter et prouver",
           accent="TEAL",
           items=[
             "Logs d'authentification, administration, accès aux données sensibles",
             "Horodatage fiable et synchronisation des systèmes",
             "Protection des journaux contre modification et suppression",
             "Analyse : alertes, corrélation, tableaux de bord",
             "Conservation proportionnée aux obligations et risques",
           ],
           note="Sans logs, on ne sait ni détecter, ni enquêter, ni prouver."),
      dict(kind="process", title="Gestion des vulnérabilités", kicker="Cycle opérationnel",
           steps=[
             ("Inventorier", "Savoir quels actifs et versions existent"),
             ("Scanner", "Identifier vulnérabilités et mauvaises configurations"),
             ("Prioriser", "Selon criticité, exposition, exploitabilité, métier"),
             ("Corriger", "Patch, configuration, mitigation ou exception formelle"),
             ("Vérifier", "Contrôler que la correction est effective"),
           ],
           example="Un CVSS critique sur un serveur non exposé peut être moins urgent qu'un CVSS élevé exploité activement sur Internet."),
      dict(kind="cards", title="Sécurité fournisseurs", kicker="Supply chain",
           cols=2,
           cards=[
             ("Avant contrat", "Évaluer criticité, données, accès, maturité", "GOLD"),
             ("Contrat", "Clauses sécurité, audit, incident, sous-traitance", "TEAL"),
             ("Pendant service", "Suivi, revues, changements, indicateurs", "BLUE"),
             ("Fin de contrat", "Réversibilité, restitution, suppression des données", "RED"),
           ],
           note="Un fournisseur critique devient une extension du système d'information."),
      dict(kind="bullets", title="Sensibilisation : changer les comportements", kicker="Humain",
           accent="BLUE",
           items=[
             "Former selon les rôles : utilisateurs, développeurs, administrateurs, direction",
             "Répéter régulièrement plutôt qu'une session unique annuelle",
             "Utiliser des exemples réalistes : phishing, données, télétravail",
             "Mesurer : taux de clic, signalements, quiz, incidents évités",
             "Valoriser les signalements plutôt que punir l'erreur de bonne foi",
           ],
           takeaway="Une culture de sécurité se construit par répétition, simplicité et confiance."),
    ],
    dict(title="TD — Rédiger une procédure audit-able", kicker="Travaux dirigés",
         duration="50 min",
         brief="Rédiger une procédure courte de création/suppression de compte utilisateur.",
         tasks=[
           "Définir objectif, périmètre, rôles et responsabilités",
           "Lister les étapes joiner/mover/leaver",
           "Indiquer les preuves à conserver",
           "Ajouter un contrôle périodique de revue des droits",
         ],
         deliverable="Procédure d'une page + liste des preuves."),
    "Les politiques transforment les normes en règles locales. Une bonne règle est comprise, applicable, reliée à un risque et vérifiable par des preuves."
)


M8 = MODULE(
    8, "Audit, conformité et cadre juridique",
    "Prouver, vérifier et respecter les obligations de sécurité",
    ["Audit", "Preuves", "Non-conformités", "RGPD", "NIS2", "DORA", "Conformité intégrée"],
    [
        "Expliquer le déroulement d'un audit de sécurité ou de certification",
        "Identifier les types de preuves attendues",
        "Distinguer non-conformité, observation et opportunité d'amélioration",
        "Résumer les exigences clés RGPD, NIS2 et DORA",
        "Construire une approche de conformité intégrée",
    ],
    [
      dict(kind="process", title="Déroulement d'un audit", kicker="Méthode",
           steps=[
             ("Planifier", "Objectif, périmètre, critères, programme"),
             ("Préparer", "Demander documents, échantillons, interlocuteurs"),
             ("Collecter", "Entretiens, preuves, observations, tests"),
             ("Conclure", "Constats, non-conformités, niveau de confiance"),
             ("Suivre", "Plan d'action et vérification de clôture"),
           ],
           takeaway="Un audit n'est pas une chasse au coupable : c'est une évaluation objective."),
      dict(kind="matrix", title="Types de preuves d'audit", kicker="Démontrer",
           headers=["Preuve", "Exemple"],
           rows=[
             ["Documentaire", "Politique, procédure, SoA, registre de risques"],
             ["Enregistrement", "Ticket, log, compte rendu de revue, rapport de test"],
             ["Entretien", "Explication cohérente par un responsable ou opérateur"],
             ["Observation", "Constat direct d'une configuration ou pratique"],
             ["Échantillon", "Vérification sur quelques cas représentatifs"],
           ],
           note="La meilleure preuve combine document, pratique observée et enregistrement."),
      dict(kind="twocol", title="Non-conformité majeure vs mineure", kicker="Constats",
           left_head="Majeure",
           left_items=[
             "Exigence absente ou non maîtrisée",
             "Risque important non traité",
             "Répétition d'écarts similaires",
             "Peut bloquer une certification",
           ],
           right_head="Mineure / observation",
           right_items=[
             "Écart ponctuel ou partiel",
             "Processus existant mais perfectible",
             "Amélioration recommandée",
             "Plan d'action suivi requis",
           ],
           left_color="RED", right_color="GOLD"),
      dict(kind="bullets", title="Réussir un entretien d'audit", kicker="Pratique",
           accent="TEAL",
           items=[
             "Répondre factuellement, sans inventer",
             "Montrer les preuves plutôt que promettre",
             "Dire « je vérifie » si l'information manque",
             "Relier la pratique au risque et à la procédure",
             "Ne pas cacher un écart : expliquer le plan de correction",
           ],
           warning="Une incohérence entre discours et preuve pèse plus lourd qu'un simple oubli."),
      dict(kind="cards", title="RGPD : principes clés", kicker="Données personnelles",
           cols=3,
           cards=[
             ("Licéité", "Base légale et information des personnes", "GOLD"),
             ("Minimisation", "Collecter seulement le nécessaire", "TEAL"),
             ("Exactitude", "Données à jour et rectifiables", "BLUE"),
             ("Durée limitée", "Conserver selon une durée justifiée", "ORANGE"),
             ("Sécurité", "Mesures techniques et organisationnelles appropriées", "RED"),
             ("Droits", "Accès, rectification, effacement, opposition…", "GOLD"),
           ],
           note="Le RGPD demande une sécurité proportionnée au risque pour les personnes."),
      dict(kind="matrix", title="RGPD : sécurité et responsabilité", kicker="Accountability",
           headers=["Élément", "Exigence pratique"],
           rows=[
             ["Registre", "Documenter les traitements et finalités"],
             ["DPIA / AIPD", "Analyser les risques élevés pour les personnes"],
             ["Violation", "Notifier si risque pour les droits et libertés"],
             ["Sous-traitants", "Contrats, instructions, sécurité, assistance"],
             ["Privacy by design", "Intégrer la protection dès la conception"],
           ],
           example="Un projet biométrique ou de données santé nécessite souvent une AIPD avant mise en production."),
      dict(kind="cards", title="NIS2 : logique générale", kicker="Europe",
           cols=2,
           cards=[
             ("Champ élargi", "18 secteurs critiques ou importants", "GOLD"),
             ("Mesures de risque", "Politiques, incident, continuité, supply chain, MFA…", "TEAL"),
             ("Notification", "Incidents significatifs selon calendrier national", "RED"),
             ("Responsabilité", "Management impliqué, supervision renforcée", "BLUE"),
           ],
           note="NIS2 est une directive : chaque État membre la transpose dans son droit national."),
      dict(kind="cards", title="DORA : résilience numérique financière", kicker="Secteur financier",
           cols=2,
           cards=[
             ("ICT risk management", "Cadre complet de gestion des risques ICT", "GOLD"),
             ("Incident reporting", "Classification et notification des incidents majeurs", "RED"),
             ("Testing", "Tests de résilience, dont TLPT pour certains acteurs", "TEAL"),
             ("Third-party risk", "Exigences contractuelles et supervision des prestataires ICT critiques", "BLUE"),
           ],
           note="DORA est un règlement directement applicable au secteur financier depuis janvier 2025."),
      dict(kind="process", title="Conformité intégrée", kicker="Éviter les silos",
           steps=[
             ("Inventaire obligations", "Lois, contrats, normes, exigences clients"),
             ("Mapping contrôles", "Relier exigences à des contrôles communs"),
             ("Preuves mutualisées", "Un même ticket ou rapport sert plusieurs exigences"),
             ("Calendrier", "Audits, revues, renouvellements, notifications"),
             ("Pilotage", "Tableau de bord conformité et risques résiduels"),
           ],
           takeaway="Une conformité efficace réutilise les mêmes contrôles et preuves au lieu de créer un dossier séparé par référentiel."),
    ],
    dict(title="TD — Préparer une checklist d'audit", kicker="Travaux dirigés",
         duration="50 min",
         brief="Créer une checklist d'audit pour la gestion des accès d'une application sensible.",
         tasks=[
           "Définir 6 critères d'audit",
           "Associer une preuve attendue à chaque critère",
           "Prévoir 3 questions d'entretien",
           "Classer les constats possibles : majeur, mineur, observation",
         ],
         deliverable="Checklist : critère → preuve → question → risque."),
    "L'audit transforme les promesses en preuves. Le droit impose des obligations, mais un SMSI bien construit permet de répondre à plusieurs cadres avec des contrôles communs."
)


M9 = MODULE(
    9, "Sécurité opérationnelle, DevSecOps, Cloud et résilience",
    "Faire fonctionner la sécurité au quotidien et préparer l'organisation aux incidents",
    ["SecOps", "Incident response", "DevSecOps", "OWASP", "Cloud", "PCA/PRA", "Indicateurs"],
    [
        "Décrire les fonctions de sécurité opérationnelle et de SOC",
        "Construire un cycle simple de réponse à incident",
        "Intégrer la sécurité dans le développement logiciel",
        "Expliquer la responsabilité partagée du cloud",
        "Définir RTO, RPO, PCA, PRA et indicateurs de pilotage",
    ],
    [
      dict(kind="cards", title="SecOps : sécurité au quotidien", kicker="Opérations",
           cols=3,
           cards=[
             ("Surveiller", "SIEM, EDR, alertes, journaux", "TEAL"),
             ("Vulnérabilités", "Scans, patch, priorisation", "GOLD"),
             ("Identités", "Revues, MFA, PAM, anomalies", "BLUE"),
             ("Incidents", "Triage, escalade, containment", "RED"),
             ("Threat intel", "Veille menace et exploitation active", "ORANGE"),
             ("Reporting", "Indicateurs et amélioration continue", "GOLD"),
           ],
           note="SecOps est le bras opérationnel de la gouvernance sécurité."),
      dict(kind="process", title="Réponse à incident", kicker="Cycle",
           steps=[
             ("Préparer", "Rôles, playbooks, outils, contacts, exercices"),
             ("Détecter", "Qualifier l'alerte et préserver les preuves"),
             ("Contenir", "Limiter la propagation et l'impact"),
             ("Éradiquer", "Supprimer cause racine, comptes, malware, faille"),
             ("Rétablir", "Restaurer service et surveiller le retour à la normale"),
             ("Apprendre", "REX, corrections, mise à jour des risques"),
           ],
           takeaway="Pendant une crise, on applique une procédure préparée ; on n'improvise pas toute la méthode."),
      dict(kind="matrix", title="Playbook d'incident : contenu minimal", kicker="Prêt à l'emploi",
           headers=["Section", "Questions"],
           rows=[
             ["Déclenchement", "Quels signaux ? Qui peut déclarer l'incident ?"],
             ["Rôles", "Incident manager, technique, communication, juridique, DPO"],
             ["Actions", "Isoler, préserver preuve, changer secrets, restaurer"],
             ["Communication", "Interne, client, autorités, presse"],
             ["Clôture", "Critères de retour à la normale et REX"],
           ],
           example="Un playbook ransomware doit inclure : isolation réseau, gel des sauvegardes, communication, décision juridique et restauration."),
      dict(kind="process", title="DevSecOps : intégrer la sécurité au pipeline", kicker="Développement",
           steps=[
             ("Plan", "Exigences sécurité et threat modeling"),
             ("Code", "Guides de codage, secrets, revue"),
             ("Build", "SAST, dépendances, SBOM, signature"),
             ("Test", "DAST, tests d'abus, scans conteneurs"),
             ("Deploy", "IaC sécurisé, approbations, segmentation"),
             ("Run", "Logs, monitoring, correction continue"),
           ],
           note="DevSecOps ne veut pas dire ralentir : il automatise les contrôles pour détecter tôt."),
      dict(kind="cards", title="OWASP Top 10 : familles de risques applicatifs", kicker="Web",
           cols=2,
           cards=[
             ("Contrôle d'accès cassé", "Droits mal appliqués côté serveur", "RED"),
             ("Cryptographie défaillante", "Données mal protégées", "GOLD"),
             ("Injection", "SQL, commandes, expressions", "RED"),
             ("Mauvaise configuration", "Services, headers, cloud, debug", "ORANGE"),
             ("Composants vulnérables", "Dépendances obsolètes ou compromises", "BLUE"),
             ("Identification/auth", "Sessions, mots de passe, MFA", "TEAL"),
           ],
           note="OWASP aide à rendre concrètes les mesures ISO sur le développement sécurisé."),
      dict(kind="twocol", title="Cloud : responsabilité partagée", kicker="Externalisation",
           left_head="Fournisseur cloud",
           left_items=[
             "Sécurité physique datacenter",
             "Infrastructure de base",
             "Certaines couches réseau / hyperviseur",
             "Disponibilité selon contrat",
           ],
           right_head="Client",
           right_items=[
             "Identités, accès, clés et configurations",
             "Données, classification, chiffrement",
             "Architecture, journaux, supervision",
             "Conformité métier et paramétrage",
           ],
           left_color="BLUE", right_color="GOLD",
           warning="La plupart des incidents cloud viennent de mauvaises configurations côté client."),
      dict(kind="cards", title="PCA, PRA, RTO, RPO", kicker="Résilience",
           cols=2,
           cards=[
             ("PCA", "Plan de continuité : continuer l'activité malgré la crise", "TEAL"),
             ("PRA", "Plan de reprise : restaurer le SI après interruption", "GOLD"),
             ("RTO", "Durée maximale acceptable d'interruption", "RED"),
             ("RPO", "Perte maximale de données acceptable dans le temps", "BLUE"),
           ],
           example="RTO 4h signifie : le service doit redémarrer en moins de 4h. RPO 15 min signifie : on accepte au maximum 15 min de données perdues."),
      dict(kind="process", title="Construire une résilience réaliste", kicker="Méthode",
           steps=[
             ("BIA", "Identifier processus critiques et impacts d'interruption"),
             ("Objectifs", "Fixer RTO/RPO validés par les métiers"),
             ("Architecture", "Sauvegardes, redondance, modes dégradés"),
             ("Procédures", "Restauration, communication, priorités"),
             ("Tests", "Exercices réguliers et amélioration"),
           ],
           takeaway="Une sauvegarde jamais testée est une hypothèse, pas une preuve."),
      dict(kind="matrix", title="Indicateurs SSI", kicker="Piloter",
           headers=["Indicateur", "Ce qu'il montre"],
           rows=[
             ["Taux MFA", "Couverture d'une mesure clé d'accès"],
             ["Délai patch critique", "Capacité à réduire l'exposition"],
             ["MTTD / MTTR", "Détection et réponse aux incidents"],
             ["Taux de revues d'accès", "Maîtrise du moindre privilège"],
             ["Tests PRA réussis", "Résilience prouvée"],
             ["Non-conformités ouvertes", "Dette de conformité et de risque"],
           ],
           warning="Un indicateur doit guider une décision. S'il ne déclenche aucune action, il est décoratif."),
    ],
    dict(title="TD — Exercice de crise ransomware", kicker="Tabletop",
         duration="60 min",
         brief="Simulation : le serveur de fichiers est chiffré lundi 8h30, les sauvegardes sont incertaines.",
         tasks=[
           "Définir les 5 premières décisions en 30 minutes",
           "Identifier les rôles à mobiliser",
           "Lister les preuves à préserver",
           "Préparer un message interne aux collaborateurs",
           "Définir les critères de retour à la normale",
         ],
         deliverable="Plan d'action de crise en une page."),
    "La sécurité opérationnelle donne vie au SMSI : détecter, répondre, développer plus sûr, maîtriser le cloud et tester la continuité. Les indicateurs ferment la boucle d'amélioration."
)


M10 = MODULE(
    10, "Étude de cas fil rouge et préparation à l'examen",
    "Synthétiser le cours en construisant le mini-SMSI d'une organisation fictive",
    ["Cas fil rouge", "Périmètre", "Risques", "SoA", "PSSI", "Audit", "Révision"],
    [
        "Appliquer l'ensemble du cours à une organisation fictive",
        "Produire un périmètre, un registre de risques et une SoA simplifiée",
        "Justifier des mesures de sécurité selon ISO 27002 et NIST CSF",
        "Préparer un mini-dossier d'audit",
        "Réviser efficacement les notions attendues à l'examen",
    ],
    [
      dict(kind="cards", title="Organisation fictive : EduSanté Services", kicker="Cas fil rouge",
           cols=2,
           cards=[
             ("Activité", "Plateforme SaaS de gestion de stages en santé", "GOLD"),
             ("Données", "Étudiants, conventions, évaluations, données de santé incidentes", "RED"),
             ("Clients", "Universités, hôpitaux partenaires, écoles privées", "BLUE"),
             ("SI", "Application web cloud, SSO, base PostgreSQL, prestataire infogérance", "TEAL"),
           ],
           note="Le cas est volontairement réaliste : données sensibles, cloud, fournisseurs, exigences clients."),
      dict(kind="process", title="Livrable 1 — Périmètre SMSI", kicker="Projet",
           steps=[
             ("Inclure", "Plateforme SaaS, production cloud, support client, processus sécurité"),
             ("Interfaces", "SSO universités, hôpitaux, prestataire infogérance"),
             ("Exclure", "Systèmes internes hors support si justification claire"),
             ("Parties intéressées", "Clients, étudiants, CNIL, hébergeur, direction"),
             ("Phrase de périmètre", "Formulation courte et audit-able"),
           ],
           takeaway="Le périmètre doit être assez clair pour qu'un auditeur sache quoi vérifier."),
      dict(kind="matrix", title="Livrable 2 — Valeurs métier et DICP", kicker="Projet",
           headers=["Valeur métier", "Critère critique"],
           rows=[
             ["Dossiers de stage", "Confidentialité + intégrité"],
             ["Disponibilité de la plateforme", "Disponibilité"],
             ["Identités et rôles", "Intégrité + preuve"],
             ["Conventions signées", "Intégrité + preuve"],
             ["Historique d'accès", "Preuve + confidentialité"],
           ],
           note="Un même actif peut porter plusieurs critères ; justifier la priorité est important."),
      dict(kind="matrix", title="Livrable 3 — Registre de risques simplifié", kicker="Projet",
           headers=["Risque", "Traitement attendu"],
           rows=[
             ["Phishing administrateur → accès base", "MFA fort, PAM, sensibilisation, logs"],
             ["Mauvaise configuration cloud → fuite", "Revue IaC, durcissement, scan CSPM"],
             ["Ransomware prestataire → interruption", "Clauses, sauvegardes, PRA, segmentation"],
             ["Erreur développeur → vulnérabilité web", "SAST, revue code, OWASP ASVS"],
             ["Demande RGPD mal traitée", "Procédure droits, registre, rôle DPO"],
           ],
           warning="Le registre doit être priorisé : cinq risques bien argumentés valent mieux que trente lignes vagues."),
      dict(kind="process", title="Livrable 4 — Scénario EBIOS", kicker="Projet",
           steps=[
             ("SR/OV", "Cybercriminel veut monétiser les données ou rançonner"),
             ("Stratégique", "Passe par un prestataire infogérance moins mature"),
             ("Opérationnel", "Vol VPN → mouvement latéral → exfiltration → chiffrement"),
             ("Gravité", "Indisponibilité plateforme + notification RGPD + perte de confiance"),
             ("Mesures", "PAM, segmentation, EDR, sauvegardes testées, clauses fournisseur"),
           ],
           note="Le scénario doit raconter une histoire plausible que la direction comprend."),
      dict(kind="matrix", title="Livrable 5 — Mini-SoA", kicker="Projet",
           headers=["Mesure", "Justification"],
           rows=[
             ["A.5.23 Cloud services", "Plateforme SaaS hébergée en cloud"],
             ["A.5.19 Suppliers", "Prestataire infogérance critique"],
             ["A.8.2 Privileged access", "Comptes admin à fort impact"],
             ["A.8.15 Logging", "Détection et preuve des accès"],
             ["A.8.28 Secure coding", "Risque applicatif web"],
             ["A.5.30 ICT readiness", "Objectifs de continuité clients"],
           ],
           note="Chaque inclusion doit être reliée à un risque ou une exigence ; chaque exclusion doit être défendable."),
      dict(kind="cards", title="Livrable 6 — Pack documentaire minimal", kicker="Projet",
           cols=2,
           cards=[
             ("Politique SSI", "Engagements, périmètre, objectifs, responsabilités", "GOLD"),
             ("Procédure accès", "Joiner/mover/leaver, MFA, revues", "TEAL"),
             ("Procédure incident", "Détection, escalade, communication, preuve", "RED"),
             ("Procédure sauvegarde", "RPO/RTO, tests, restauration, responsabilités", "BLUE"),
           ],
           takeaway="Un pack minimal bien tenu vaut mieux qu'une bibliothèque documentaire jamais appliquée."),
      dict(kind="process", title="Livrable 7 — Préparer l'audit", kicker="Projet",
           steps=[
             ("Critères", "Choisir clauses ISO 27001 et mesures Annex A à démontrer"),
             ("Preuves", "Rassembler politiques, tickets, logs, rapports, comptes rendus"),
             ("Entretiens", "Préparer direction, RSSI, DevOps, support, DPO"),
             ("Échantillons", "Comptes utilisateurs, incidents, changements, sauvegardes"),
             ("Plan d'action", "Identifier écarts avant l'auditeur externe"),
           ],
           note="La préparation d'audit doit vérifier la réalité opérationnelle, pas seulement le dossier documentaire."),
      dict(kind="checklist", title="Checklist de révision", kicker="Avant examen",
           cols=2, accent="TEAL",
           items=[
             "Définir DICP et donner un exemple",
             "Distinguer menace, vulnérabilité, risque",
             "Expliquer norme / méthode / règlement",
             "Citer les clauses ISO 27001:2022",
             "Expliquer SoA et registre de risques",
             "Présenter les 4 thèmes ISO 27002",
             "Dérouler les 5 ateliers EBIOS RM",
             "Présenter les 6 fonctions NIST CSF 2.0",
             "Donner les principes RGPD, NIS2, DORA",
             "Décrire audit, preuves, non-conformités",
             "Expliquer PCA/PRA/RTO/RPO",
             "Justifier une mesure par un risque",
           ],
           note="Savoir réciter ne suffit pas : l'examen demandera d'appliquer les notions à un cas."),
      dict(kind="matrix", title="Structure indicative de l'examen", kicker="Évaluation",
           headers=["Partie", "Compétence évaluée"],
           rows=[
             ["Questions courtes", "Définitions : DICP, SMSI, SoA, RTO, NIS2…"],
             ["Analyse de cas", "Identifier actifs, risques, impacts, mesures"],
             ["Mini-audit", "Associer exigence, preuve, non-conformité"],
             ["Question de synthèse", "Comparer ISO 27001, ISO 27002, NIST CSF, EBIOS"],
           ],
           note="La meilleure préparation est de refaire les TD et de savoir justifier ses choix."),
      dict(kind="cards", title="Ressources fiables", kicker="Pour aller plus loin",
           cols=2,
           cards=[
             ("ISO/IEC", "Famille 27000, 27001, 27002, 27005", "GOLD"),
             ("ANSSI", "Guides d'hygiène, EBIOS RM, recommandations cloud", "BLUE"),
             ("NIST", "CSF 2.0, SP 800-53, SP 800-61, SP 800-218", "TEAL"),
             ("CNIL / ENISA", "RGPD, guides pratiques, cybersécurité européenne", "RED"),
           ],
           takeaway="Un bon professionnel cite ses sources et vérifie les versions des référentiels."),
    ],
    dict(title="Projet final — Soutenance courte", kicker="Travaux dirigés",
         duration="90 min",
         brief="Chaque groupe présente son mini-SMSI EduSanté Services en 8 minutes + 4 minutes de questions.",
         tasks=[
           "Présenter périmètre, valeurs métier et 5 risques prioritaires",
           "Expliquer un scénario EBIOS en langage direction",
           "Justifier 8 mesures ISO 27002 dans une mini-SoA",
           "Montrer 4 preuves attendues en audit",
           "Conclure par 3 priorités d'amélioration",
         ],
         deliverable="Diaporama court ou fiche synthèse de 3 pages."),
    "Le module 10 assemble tout : gouvernance, risque, mesures, droit, audit et opérations. La compétence centrale est de justifier une décision de sécurité de façon claire, traçable et proportionnée."
)


BACK = [
    S("closing", "Merci de votre attention", module=0,
      subtitle="Questions, échanges et retours sur le projet",
      speech=[
        ("p", "Le cours est terminé. Remercier les étudiants, rappeler que les "
              "normes ne sont pas une fin en soi mais un langage commun pour "
              "maîtriser les risques, puis ouvrir les questions."),
        ("key", "Conclusion : être professionnel en sécurité, c'est savoir "
                "justifier des choix proportionnés, documentés et vérifiables."),
      ]),
]


SLIDES = []


def _register(*groups):
    for g in groups:
        SLIDES.extend(g)


_register(FRONT, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, BACK)
