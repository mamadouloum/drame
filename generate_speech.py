#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère le DISCOURS COMPLET (support de l'orateur) :
    « La cybersécurité : protéger ses données à l'ère du numérique »

Public non spécialiste — séance de 2 heures.
Sorties :
    - discours_cybersecurite.pdf   (document principal, prêt à imprimer)
    - discours_cybersecurite.md    (même contenu, lisible partout)

Le discours est aligné diapo par diapo sur cybersecurite_presentation.pptx
(57 diapositives) et minuté pour tenir 2 h, pause et questions comprises.

Dépendances : reportlab (polices Bitstream Vera fournies avec reportlab).
"""

import os
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --------------------------------------------------------------------------
# Polices (Bitstream Vera, livrées avec reportlab : couverture latine complète)
# --------------------------------------------------------------------------
FDIR = os.path.join(os.path.dirname(reportlab.__file__), "fonts")
pdfmetrics.registerFont(TTFont("Vera", os.path.join(FDIR, "Vera.ttf")))
pdfmetrics.registerFont(TTFont("Vera-Bold", os.path.join(FDIR, "VeraBd.ttf")))
pdfmetrics.registerFont(TTFont("Vera-Italic", os.path.join(FDIR, "VeraIt.ttf")))
pdfmetrics.registerFont(TTFont("Vera-BoldItalic", os.path.join(FDIR, "VeraBI.ttf")))
pdfmetrics.registerFontFamily("Vera", normal="Vera", bold="Vera-Bold",
                              italic="Vera-Italic", boldItalic="Vera-BoldItalic")

# --------------------------------------------------------------------------
# Couleurs
# --------------------------------------------------------------------------
NAVY   = HexColor("#0F2A47")
BLUE   = HexColor("#2E75B6")
TEAL   = HexColor("#1F9E8F")
RED    = HexColor("#C0392B")
ORANGE = HexColor("#E06C2B")
GREY   = HexColor("#5A6B7B")
DARK   = HexColor("#1B2A3A")

# encadrés : (couleur d'accent, fond, étiquette PDF, étiquette Markdown)
CALLOUTS = {
    "trans": (BLUE,   HexColor("#EAF1F9"), "TRANSITION",            "➜ Transition"),
    "tip":   (TEAL,   HexColor("#E6F4F1"), "CONSEIL D'ANIMATION",   "💡 Conseil d'animation"),
    "inter": (ORANGE, HexColor("#FCEEE3"), "INTERACTION — À FAIRE", "🙋 Interaction"),
    "key":   (NAVY,   HexColor("#E7ECF2"), "À RETENIR",             "🔑 À retenir"),
}

MARGIN = 18 * mm
USABLE = A4[0] - 2 * MARGIN

# --------------------------------------------------------------------------
# Styles de paragraphes
# --------------------------------------------------------------------------
st_title = ParagraphStyle("title", fontName="Vera-Bold", fontSize=25, leading=30,
                          textColor=NAVY, alignment=TA_CENTER, spaceAfter=6)
st_sub = ParagraphStyle("sub", fontName="Vera-Italic", fontSize=14, leading=19,
                        textColor=BLUE, alignment=TA_CENTER, spaceAfter=4)
st_meta = ParagraphStyle("meta", fontName="Vera", fontSize=10.5, leading=15,
                         textColor=GREY, alignment=TA_CENTER)
st_h1 = ParagraphStyle("h1", fontName="Vera-Bold", fontSize=15, leading=20,
                       textColor=colors.white)
st_h2 = ParagraphStyle("h2", fontName="Vera-Bold", fontSize=12.5, leading=15,
                       textColor=NAVY)
st_dur = ParagraphStyle("dur", fontName="Vera", fontSize=9.5, leading=15,
                        textColor=GREY, alignment=TA_RIGHT)
st_body = ParagraphStyle("body", fontName="Vera", fontSize=10.5, leading=15.5,
                         textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=6)
st_bul = ParagraphStyle("bul", fontName="Vera", fontSize=10.5, leading=15,
                        textColor=DARK, alignment=TA_LEFT, leftIndent=14,
                        bulletIndent=2, spaceAfter=3)
st_section = ParagraphStyle("section", fontName="Vera-Bold", fontSize=11,
                            leading=15, textColor=NAVY, spaceBefore=4, spaceAfter=4)
st_lead = ParagraphStyle("lead", fontName="Vera-BoldItalic", fontSize=11,
                         leading=16, textColor=NAVY, spaceAfter=6)


def esc(t):
    # La police Vera n'a pas la flèche U+2192 : on la remplace par un chevron.
    t = t.replace("\u2192", "»")
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------------
# Constructeurs de blocs (flowables PDF)
# --------------------------------------------------------------------------
def part_bar(text):
    p = Paragraph(esc(text), st_h1)
    t = Table([[p]], colWidths=[USABLE])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t


def slide_head(num, title, dur):
    left = Paragraph("Diapositive %s — %s" % (num, esc(title)), st_h2)
    right = Paragraph(dur, st_dur)
    t = Table([[left, right]], colWidths=[USABLE * 0.80, USABLE * 0.20])
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 1.2, TEAL),
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def callout(kind, text):
    accent, tint, label, _ = CALLOUTS[kind]
    lab = Paragraph(label, ParagraphStyle("lab", fontName="Vera-Bold", fontSize=8,
                                          textColor=accent, leading=11, spaceAfter=3))
    body = Paragraph(esc(text), ParagraphStyle("cob", fontName="Vera", fontSize=10,
                                               textColor=DARK, leading=14.5,
                                               alignment=TA_JUSTIFY))
    t = Table([[[lab, body]]], colWidths=[USABLE])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tint),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


# --------------------------------------------------------------------------
# En-tête / pied de page
# --------------------------------------------------------------------------
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Vera", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, 10 * mm,
                      "Discours — La cybersécurité : protéger ses données à l'ère du numérique")
    canvas.drawRightString(A4[0] - MARGIN, 10 * mm, "p. %d" % doc.page)
    canvas.setStrokeColor(HexColor("#D6DFEA"))
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 13 * mm, A4[0] - MARGIN, 13 * mm)
    canvas.restoreState()


# ==========================================================================
#  CONTENU DU DISCOURS
#  Chaque bloc : ("part"|"slide"|"p"|"lead"|"trans"|"tip"|"inter"|"key"|"bul"|"sec", ...)
# ==========================================================================
BLOCKS = [

# ======================= ACCUEIL / INTRODUCTION ===========================
("part", "ACCUEIL ET INTRODUCTION  ·  0:00 → 0:08"),

("slide", "1", "Diapositive de titre — Accueil", "1 min"),
("p", "Bonjour à toutes et à tous, et merci d'être là. Installez-vous tranquillement. "
      "Pendant les deux heures qui viennent, nous allons parler d'un sujet qui nous concerne "
      "absolument tous, que l'on soit très à l'aise avec la technologie ou pas du tout : "
      "la cybersécurité, c'est-à-dire l'art de protéger ses données et sa vie numérique."),
("p", "Je vais vous rassurer tout de suite : il n'y aura aucun jargon compliqué, aucune ligne "
      "de code, et aucune question piège. Mon objectif n'est pas de faire de vous des experts, "
      "mais de vous donner des réflexes simples que vous pourrez appliquer dès ce soir, chez vous, "
      "sur votre téléphone et votre ordinateur."),
("inter", "Se présenter en une phrase. Demander à la salle, à main levée : « Qui est venu un peu "
          "inquiet, parce qu'il a déjà entendu parler d'arnaques ou de piratages ? » Cela crée "
          "tout de suite de la proximité."),

("slide", "2", "Les objectifs de cet atelier", "2 min"),
("p", "Voici ce que je vous propose. À la fin de ces deux heures, vous devriez repartir avec cinq choses. "
      "Premièrement, comprendre pourquoi la cybersécurité nous concerne tous, et pas seulement les "
      "entreprises ou les célébrités. Deuxièmement, savoir reconnaître les principales menaces que vous "
      "croisez au quotidien, souvent sans les voir."),
("p", "Troisièmement — et c'est le cœur de la séance — adopter des réflexes simples, concrets et gratuits. "
      "Quatrièmement, savoir quoi faire si un jour vous êtes victime d'une attaque, car cela peut arriver "
      "à tout le monde. Et cinquièmement, repartir avec une petite check-list et des ressources fiables, "
      "pour ne pas tout retenir par cœur."),
("key", "Le message de fond de tout l'atelier : la sécurité, c'est 80 % de bonnes habitudes et 20 % de "
        "technique. Ces bonnes habitudes sont à la portée de tout le monde ici présent."),

("slide", "3", "Au programme des 2 heures", "1 min 30"),
("p", "Rapidement, comment on va s'organiser. La première partie sera consacrée à la compréhension : "
      "on pose les bases, puis on fait le tour des menaces. Ensuite, on fera une petite pause d'une "
      "dizaine de minutes, parce que deux heures, c'est long, et le cerveau a besoin de respirer."),
("p", "La deuxième partie sera tournée vers l'action : comment se protéger concrètement, quelques cas "
      "de la vie courante, et comment réagir en cas de problème. Et surtout : n'attendez pas la fin pour "
      "poser vos questions. Coupez-moi quand vous voulez, c'est un atelier, pas une conférence."),
("tip", "Prévenir la salle de la pause dès maintenant : les gens sont plus détendus quand ils savent "
        "qu'un moment de repos est prévu."),

("slide", "4", "Un petit sondage pour démarrer", "2 min 30"),
("p", "Avant d'entrer dans le vif, faisons un petit sondage à main levée. Ne réfléchissez pas trop, "
      "répondez spontanément, et surtout : il n'y a aucune honte à avoir, nous sommes tous concernés."),
("inter", "Poser les questions une par une et laisser les mains se lever. « Qui a déjà reçu un SMS ou un "
          "e-mail qui semblait suspect ? » — « Qui utilise, ne serait-ce que parfois, le même mot de passe "
          "sur plusieurs sites ? » — « Qui a déjà hésité avant de cliquer sur un lien ? » — « Qui a déjà eu "
          "un proche victime d'une arnaque en ligne ? » Commenter avec bienveillance le nombre de mains."),
("p", "Regardez autour de vous. Vous voyez ? Vous n'êtes pas seuls. Si vous avez levé la main au moins "
      "une fois, et c'est le cas de presque tout le monde, alors vous êtes exactement au bon endroit. "
      "Ces comportements sont parfaitement normaux — le but d'aujourd'hui, c'est simplement de les rendre "
      "un peu plus sûrs."),
("trans", "Enchaîner : « Pour bien se protéger, il faut d'abord comprendre de quoi on parle. Commençons "
          "par le commencement. »"),

# ======================= PARTIE 1 — COMPRENDRE ============================
("part", "PARTIE 1 — COMPRENDRE LE MONDE NUMÉRIQUE  ·  0:08 → 0:33"),

("slide", "5", "Ouverture de la Partie 1", "30 s"),
("p", "Première partie : comprendre le monde numérique. De quoi parle-t-on exactement quand on dit "
      "« données » et « cybersécurité », et pourquoi est-ce devenu si important ? On prend cinq minutes "
      "pour poser le décor, ça rendra tout le reste beaucoup plus clair."),

("slide", "6", "Notre vie est devenue numérique", "3 min"),
("p", "Faisons ensemble un petit exercice mental. Repensez à votre journée d'hier. Vous avez "
      "probablement consulté votre téléphone au réveil. Peut-être regardé vos e-mails, vos messages. "
      "Vous avez peut-être payé quelque chose sans contact, consulté votre compte en banque, pris une "
      "photo, cherché un itinéraire, ou envoyé un document. Chacune de ces actions a produit des données."),
("p", "En quelques années, notre vie est devenue numérique presque sans qu'on s'en rende compte. La "
      "banque, les impôts, la santé avec le dossier médical en ligne, le travail, l'école des enfants, "
      "les loisirs, les relations avec la famille et les amis : tout passe désormais, au moins en partie, "
      "par des écrans. Le smartphone, en particulier, est devenu une sorte de prolongement de nous-mêmes. "
      "Il connaît nos habitudes, nos déplacements, nos proches, nos secrets."),
("p", "C'est extrêmement pratique, personne ne veut revenir en arrière. Mais ce confort a un revers : "
      "plus notre vie est connectée, plus il y a de portes et de fenêtres par lesquelles quelqu'un de "
      "mal intentionné pourrait entrer. On appelle ça, dans le jargon, la « surface d'exposition ». "
      "Retenez simplement l'idée : nous avons tous, aujourd'hui, beaucoup plus à protéger qu'il y a "
      "vingt ans."),
("key", "Plus notre vie est connectée, plus la surface exposée est grande. Ce n'est pas une raison pour "
        "avoir peur, mais une raison pour être un peu attentif."),

("slide", "7", "Statistique : une attaque toutes les 39 secondes", "1 min 30"),
("p", "Un chiffre pour donner l'échelle du phénomène. On estime qu'une attaque informatique a lieu, en "
      "moyenne, toutes les 39 secondes dans le monde. Ce chiffre vient d'une étude universitaire souvent "
      "citée, et il faut le prendre pour ce qu'il est : un ordre de grandeur, pas une mesure au chronomètre."),
("p", "Ce qu'il faut en retenir, ce n'est pas le nombre exact, c'est l'idée : ces attaques sont "
      "permanentes, massives, et en grande partie automatisées. Pendant que je vous parle, des programmes "
      "testent des millions de combinaisons et de portes à travers le monde. La bonne nouvelle, on y "
      "reviendra, c'est que contre des attaques automatiques, des gestes simples suffisent la plupart du temps."),

("slide", "8", "Statistique : 90 % des attaques commencent par un e-mail", "1 min 30"),
("p", "Deuxième chiffre, encore plus parlant. On estime que la grande majorité des cyberattaques — de "
      "l'ordre de neuf sur dix — commencent par quelque chose de très banal : un simple message. Un e-mail, "
      "un SMS, parfois un appel. Pas une faille technique obscure dans un serveur, non : un message qui "
      "vous est adressé, à vous."),
("p", "Pourquoi ? Parce que c'est beaucoup plus facile de convaincre une personne de cliquer que de "
      "casser une protection informatique. Autrement dit, la principale porte d'entrée, dans la plupart "
      "des cas, c'est nous. C'est un peu vexant dit comme ça, mais c'est en réalité une excellente "
      "nouvelle : cela veut dire que notre vigilance est la protection la plus puissante qui existe."),
("trans", "« Puisque nous sommes la cible, comprenons d'abord ce qu'est vraiment la cybersécurité. »"),

("slide", "9", "Qu'est-ce que la cybersécurité ?", "3 min"),
("p", "La cybersécurité, c'est simplement l'ensemble des moyens qui servent à protéger nos appareils, "
      "nos comptes et nos données. Protéger contre quoi ? Contre trois choses : l'accès par quelqu'un qui "
      "n'a rien à y faire, le vol, et la destruction ou la modification de nos informations."),
("p", "Pour rendre ça concret, prenons une image que tout le monde connaît : la sécurité d'une maison. "
      "Vous avez des outils techniques : une porte solide, une bonne serrure, peut-être une alarme. Mais "
      "ces outils ne servent à rien si vous laissez la porte ouverte, si vous cachez la clé sous le "
      "paillasson, ou si vous ouvrez à un inconnu qui prétend être un livreur. La sécurité d'une maison, "
      "c'est donc un peu de matériel, et beaucoup de comportement."),
("p", "La cybersécurité, c'est exactement pareil. On peut installer tous les logiciels du monde : si on "
      "clique sur n'importe quoi et qu'on utilise « 123456 » comme mot de passe, ça ne tiendra pas. À "
      "l'inverse, avec quelques bons réflexes, on se protège déjà énormément. C'est pour ça que cet "
      "atelier parle surtout de comportements, pas de technique."),
("key", "80 % de la sécurité, ce sont des habitudes. La technique est utile, mais elle ne fait pas tout — "
        "et surtout, elle ne vous remplace pas."),

("slide", "10", "Une « donnée », c'est quoi au juste ?", "3 min"),
("p", "On parle beaucoup de « données », mais qu'est-ce que c'est concrètement ? Ce sont toutes les "
      "informations qui vous concernent. Prenons-les par familles, parce que toutes n'ont pas la même "
      "sensibilité."),
("bul", [
    "Votre identité : nom, date de naissance, numéro de sécurité sociale, pièces d'identité.",
    "Vos coordonnées : adresse postale, numéro de téléphone, adresse e-mail.",
    "Vos accès : vos identifiants et vos mots de passe — les clés de tout le reste.",
    "Votre argent : coordonnées bancaires, numéros de carte.",
    "Votre vie privée : vos photos, vos messages, votre liste de contacts.",
    "Vos traces : votre localisation, votre historique de navigation, vos achats.",
]),
("p", "Ce qui est intéressant, c'est que même les données qui semblent anodines ont de la valeur. Votre "
      "historique d'achats en dit long sur vos habitudes. Votre localisation révèle où vous habitez et "
      "quand vous êtes absent. Mises bout à bout, ces petites informations dressent un portrait très "
      "précis de vous — et c'est précisément ce qui intéresse aussi bien les publicitaires que les "
      "escrocs."),

("slide", "11", "Pourquoi VOS données ont de la valeur", "3 min"),
("p", "J'entends souvent une objection très légitime : « Mais moi, je n'ai rien à cacher, pourquoi "
      "quelqu'un s'intéresserait à mes données ? » C'est une excellente question. La réponse tient en une "
      "phrase : « ne rien avoir à cacher » n'est pas la même chose que « ne rien avoir à protéger »."),
("p", "Vous n'avez rien à cacher, mais avez-vous envie que quelqu'un vide votre compte en banque ? "
      "Ouvre un crédit à votre nom ? Se fasse passer pour vous auprès de vos proches pour leur soutirer "
      "de l'argent ? Publie vos photos privées ? Voilà ce qu'il y a à protéger."),
("p", "Concrètement, les données volées se revendent, sur des marchés cachés d'internet qu'on appelle "
      "parfois le « dark web ». Elles servent à l'usurpation d'identité, à la fraude bancaire, et à "
      "fabriquer des arnaques sur mesure, très crédibles, parce qu'elles utilisent vos vraies "
      "informations. Et gardez en tête cette règle simple sur internet : quand un service est gratuit, "
      "c'est très souvent que le produit vendu, c'est vous — ou plus exactement, vos données."),
("key", "On ne vole pas que les célébrités. Les particuliers sont des cibles faciles, nombreuses et "
        "rentables. Être « quelqu'un d'ordinaire » ne vous met pas à l'abri, au contraire."),

("slide", "12", "Les 3 piliers de la sécurité", "2 min 30"),
("p", "Les professionnels résument la sécurité en trois mots, et ils sont faciles à comprendre. Premier "
      "pilier : la confidentialité. Cela veut dire que seules les bonnes personnes ont accès à "
      "l'information. Votre médecin voit votre dossier médical, mais pas votre voisin."),
("p", "Deuxième pilier : l'intégrité. L'information ne doit pas être modifiée à votre insu. Imaginez "
      "que quelqu'un change discrètement le numéro de compte sur une facture que vous vous apprêtez à "
      "payer : les données ont l'air normales, mais elles ont été altérées. C'est une attaque contre "
      "l'intégrité."),
("p", "Troisième pilier : la disponibilité. Vos données doivent être accessibles quand vous en avez "
      "besoin. Un rançongiciel qui verrouille toutes vos photos, c'est une attaque contre la "
      "disponibilité. Retenez ces trois mots — confidentialité, intégrité, disponibilité — ils "
      "résument tout ce contre quoi on se protège."),

("slide", "13", "Qui sont les attaquants ?", "3 min"),
("p", "Qui sont ces fameux « pirates » ? Il n'y a pas un seul profil, mais plusieurs, avec des "
      "motivations différentes. Les connaître aide à comprendre les risques."),
("bul", [
    "Les cybercriminels, motivés par l'argent : c'est l'immense majorité. Ils veulent votre argent, "
    "directement ou en revendant vos données.",
    "Les arnaqueurs opportunistes : ils ratissent large, de façon automatisée, en espérant que "
    "quelques personnes tombent dans le panneau.",
    "Les hacktivistes : ils agissent pour défendre une cause, une idée.",
    "L'espionnage et les États : ils visent des cibles stratégiques, des entreprises, des "
    "institutions — cela nous concerne moins directement au quotidien.",
    "Les proches malveillants : un ex-conjoint, un membre de l'entourage, un curieux. On y pense "
    "peu, mais ça existe.",
    "Et enfin, l'erreur humaine : pas de méchant ici, juste une fausse manipulation. C'est l'une "
    "des causes les plus fréquentes de pertes de données.",
]),
("p", "Ce qu'il faut retenir : dans votre vie de tous les jours, la menace numéro un, ce n'est pas "
      "l'espion d'un film, c'est l'escroc qui cherche de l'argent, vite et facilement."),

("slide", "14", "Le mythe du génie encapuchonné", "2 min 30"),
("p", "Justement, cassons tout de suite une image. Quand on dit « hacker », beaucoup imaginent un génie "
      "solitaire, encapuchonné, dans une pièce sombre, qui tape frénétiquement sur son clavier. C'est une "
      "image de cinéma. La réalité est à la fois moins spectaculaire et plus inquiétante."),
("p", "La réalité, c'est une véritable industrie, organisée comme une entreprise. Il y a des équipes, de "
      "la sous-traitance, des logiciels qu'on peut carrément louer, un « service client » pour les "
      "victimes qui paient une rançon. Et surtout, énormément d'automatisation : des programmes qui "
      "tournent jour et nuit et testent des millions de cibles."),
("p", "Ce qui veut dire une chose importante : la plupart du temps, on ne vous vise pas, vous, "
      "personnellement. On lance un immense filet sur des millions de gens, et on attend de voir qui va "
      "mordre à l'hameçon. Vous n'êtes pas visé pour qui vous êtes ; vous êtes visé parce que vous êtes "
      "là. C'est vexant, mais c'est libérateur :"),
("key", "Contre des attaques automatisées et opportunistes, ne pas être une cible facile suffit le plus "
        "souvent à passer entre les mailles du filet. C'est tout l'objet de la deuxième partie."),
("trans", "« Maintenant qu'on sait à qui on a affaire, regardons concrètement leurs techniques. »"),

# ======================= PARTIE 2 — LES MENACES ===========================
("part", "PARTIE 2 — LES MENACES LES PLUS COURANTES  ·  0:33 → 1:06"),

("slide", "15", "Ouverture de la Partie 2", "30 s"),
("p", "Deuxième partie : le panorama des menaces. L'idée n'est pas de vous faire peur, mais de vous "
      "apprendre à reconnaître l'ennemi. Car une menace qu'on sait identifier est déjà à moitié "
      "neutralisée. On va voir les grandes familles, avec à chaque fois des exemples très concrets."),

("slide", "16", "Panorama des menaces", "2 min"),
("p", "Voici la carte du territoire. On peut regrouper l'essentiel des menaces en six familles : les "
      "logiciels malveillants, le hameçonnage, l'ingénierie sociale, le vol de mots de passe, les fuites "
      "de données, et les arnaques en ligne. Ne vous inquiétez pas, on va les reprendre une par une."),
("p", "Vous allez remarquer un point commun frappant à presque toutes : à un moment ou à un autre, elles "
      "reposent sur une action de notre part. Un clic, une saisie, un mot de passe faible, une pièce "
      "jointe ouverte trop vite. C'est une excellente nouvelle : cela signifie que nous avons, à chaque "
      "fois, une occasion d'arrêter l'attaque."),

("slide", "17", "Les logiciels malveillants (malwares)", "3 min"),
("p", "Commençons par les logiciels malveillants, qu'on appelle aussi « malwares ». Ce sont simplement "
      "des programmes conçus pour vous nuire ou vous espionner, à votre insu. Il en existe plusieurs "
      "grandes familles."),
("bul", [
    "Les virus et les vers : ils se propagent d'un fichier ou d'un appareil à l'autre, comme une "
    "maladie contagieuse.",
    "Le cheval de Troie : comme dans la légende, il se cache dans un logiciel d'apparence tout à fait "
    "normale — un jeu, un utilitaire gratuit — et agit une fois installé.",
    "L'espiogiciel, ou spyware : il vous surveille en silence — ce que vous tapez, vos mots de passe, "
    "ce qui s'affiche à l'écran.",
]),
("p", "Comment arrivent-ils chez vous ? Presque toujours par les mêmes chemins : une pièce jointe qu'on "
      "ouvre, un logiciel téléchargé sur un site douteux, une fausse mise à jour qui surgit dans le "
      "navigateur, ou même une clé USB trouvée ou prêtée. La règle d'or : on n'installe et on n'ouvre "
      "que ce dont on connaît la provenance."),

("slide", "18", "Focus : les rançongiciels (ransomware)", "3 min"),
("p", "Zoom sur une catégorie devenue tristement célèbre : les rançongiciels, ou « ransomware ». Le "
      "principe est simple et redoutable : le programme chiffre vos fichiers, c'est-à-dire qu'il les "
      "verrouille avec un code que vous n'avez pas, puis il affiche un message qui réclame une rançon "
      "pour vous rendre l'accès."),
("p", "Du jour au lendemain, tout devient inaccessible d'un coup : vos photos de famille, vos documents, "
      "vos souvenirs, votre travail. Ces attaques ont paralysé des hôpitaux qui ne pouvaient plus accéder "
      "aux dossiers des patients, des mairies, des écoles, des entreprises entières. Et ça touche aussi "
      "les particuliers."),
("p", "Un conseil essentiel : si cela vous arrive, payer ne garantit rien du tout. Vous n'avez aucune "
      "assurance de récupérer vos fichiers, et vous financez et encouragez les criminels, qui vous "
      "marqueront comme un bon client. La vraie parade existe, elle est simple et gratuite, et on en "
      "reparlera longuement : c'est la sauvegarde."),
("key", "Avec une bonne sauvegarde, un rançongiciel passe du statut de catastrophe à celui de simple "
        "contretemps : on efface tout, on restaure, et on repart."),

("slide", "19", "Le hameçonnage (phishing) — le plus fréquent", "3 min"),
("p", "Voici LA menace à connaître par cœur, parce que c'est de très loin la plus fréquente : le "
      "hameçonnage, ou « phishing » en anglais. Le mot est bien choisi : comme à la pêche, on vous "
      "envoie un appât, en espérant que vous mordiez."),
("p", "Concrètement, c'est un faux message qui imite un organisme en qui vous avez confiance : votre "
      "banque, les impôts, l'Assurance maladie, la CAF, La Poste, un service de livraison, un site de "
      "streaming... Le message a l'air vrai, avec le bon logo, les bonnes couleurs. Son but : vous faire "
      "cliquer sur un lien, puis vous faire saisir vos identifiants ou vos coordonnées bancaires sur une "
      "fausse page qui ressemble à la vraie."),
("p", "Et attention, le hameçonnage se décline sur tous les canaux. Par e-mail, c'est le phishing "
      "classique. Par SMS, on parle de « smishing » — le fameux SMS de colis en attente. Et par "
      "téléphone, on parle de « vishing » — le faux conseiller qui vous appelle. Le support change, mais "
      "la recette est toujours la même."),

("slide", "20", "Anatomie d'un message piégé", "4 min"),
("p", "Le plus utile, maintenant, c'est d'apprendre à repérer un message piégé. Bonne nouvelle : ils "
      "présentent presque tous les mêmes signaux d'alerte. Je vous en donne six. Si vous en repérez ne "
      "serait-ce qu'un ou deux, la sonnette d'alarme doit sonner."),
("bul", [
    "Signal 1 — l'expéditeur douteux : une adresse bizarre, avec des chiffres, ou qui imite "
    "grossièrement le vrai nom (par exemple « service-clients-laposte.info »).",
    "Signal 2 — l'urgence ou la peur : « Votre compte va être suspendu », « Agissez sous 24 heures ». "
    "On cherche à vous faire paniquer pour vous empêcher de réfléchir.",
    "Signal 3 — la formulation étrange : des fautes, un ton inhabituel, un « Cher client » impersonnel.",
    "Signal 4 — le lien trompeur : le texte affiché ne correspond pas à la vraie adresse. On peut le "
    "vérifier en survolant le lien sans cliquer.",
    "Signal 5 — la demande sensible : un vrai organisme ne vous demandera jamais votre mot de passe "
    "complet ou votre code de carte par message.",
    "Signal 6 — la pièce jointe inattendue : une « facture » ou un « bon de livraison » à ouvrir vite.",
]),
("inter", "Exercice concret : lire à voix haute un faux SMS type — « Votre colis n'a pas pu être livré, "
          "réglez 1,99 € de frais sous 48h : [lien] ». Demander à la salle : « Combien de signaux "
          "d'alerte repérez-vous ? » Faire lever la main. Excellent pour ancrer la méthode."),
("key", "Dans le doute, on ne clique jamais dans le message. On ouvre soi-même l'application ou le site "
        "officiel, ou on appelle le numéro qui figure au dos de sa carte."),

("slide", "21", "L'ingénierie sociale : manipuler l'humain", "3 min 30"),
("p", "Derrière le hameçonnage se cache une idée plus large et fascinante : l'ingénierie sociale. C'est "
      "l'art de manipuler les personnes plutôt que les machines. Un attaquant préfère souvent vous "
      "demander gentiment la clé plutôt que de forcer la porte — c'est moins fatigant et plus efficace."),
("p", "Pour cela, il joue sur nos émotions et nos réflexes naturels : l'urgence, qui nous empêche de "
      "réfléchir ; la peur, qui nous fait obéir ; l'autorité, quand quelqu'un se fait passer pour votre "
      "banque ou votre patron ; l'appât du gain, avec un faux cadeau ou un faux remboursement ; la "
      "curiosité, avec un lien trop tentant ; et même la gentillesse, notre envie naturelle d'aider."),
("p", "Quelques exemples classiques : le faux service technique qui appelle en disant que votre "
      "ordinateur est infecté ; le « faux patron » qui écrit à un employé pour réclamer un virement "
      "urgent et confidentiel ; le faux conseiller bancaire qui vous met la pression au téléphone. Le "
      "point commun : on vous presse, on vous isole, on vous empêche de vérifier."),
("key", "Le doute est votre meilleur allié. Un organisme sérieux ne vous mettra jamais la pression et "
        "acceptera toujours que vous rappeliez par un canal officiel. La précipitation, c'est le signal."),

("slide", "22", "Les arnaques que vous croiserez", "4 min"),
("p", "Passons à des exemples très concrets, ceux que vous allez réellement croiser — certains les ont "
      "peut-être déjà reçus cette semaine."),
("bul", [
    "Le colis en attente : un SMS vous demande de payer une petite somme, 1 ou 2 euros, pour "
    "« libérer » un colis. Le but n'est pas ces 2 euros, c'est de récupérer votre numéro de carte.",
    "Le faux support technique : une fenêtre ou un appel vous dit que votre PC est infecté et qu'il "
    "faut appeler un numéro. Au bout du fil, on vous fait payer ou installer un logiciel espion.",
    "Le faux conseiller bancaire : « Nous avons détecté un virement suspect, confirmez votre identité. » "
    "On vous fait valider vous-même l'opération frauduleuse.",
    "Les bonnes affaires trop belles : un site qui imite une grande marque et propose des prix "
    "imbattables. Vous payez, vous ne recevez rien — ou une contrefaçon.",
    "L'arnaque sentimentale : une belle rencontre en ligne, une relation qui s'installe, puis un jour "
    "une demande d'argent pour un problème urgent.",
    "Le faux remboursement : « Les impôts vous doivent 200 euros, cliquez pour être remboursé. » "
    "L'administration ne fonctionne jamais comme ça.",
]),
("inter", "Demander à la salle : « Qui a déjà reçu l'un de ces messages ? » Inviter une ou deux personnes "
          "à raconter brièvement. Les témoignages réels marquent beaucoup plus que les exemples théoriques."),

("slide", "23", "Le nerf de la guerre : les mots de passe", "3 min"),
("p", "Parlons maintenant du nerf de la guerre : les mots de passe. Pourquoi sont-ils si importants ? "
      "Parce qu'ils sont les clés de toute votre vie numérique. Et malheureusement, c'est souvent par là "
      "que tout s'effondre."),
("p", "Voici comment les attaquants s'y prennent. D'abord, ils exploitent les fuites : quand un site se "
      "fait pirater, des millions de mots de passe se retrouvent dans la nature, et les criminels les "
      "testent partout ailleurs. Ensuite, ils devinent : le prénom, la date de naissance, « 123456 » — "
      "oui, c'est encore aujourd'hui le mot de passe le plus utilisé au monde. Enfin, ils utilisent la "
      "force brute : des programmes qui essaient des millions de combinaisons par seconde."),
("p", "Et pourquoi ça marche si bien ? Parce que nous faisons tous, ou presque, la même erreur : on "
      "réutilise le même mot de passe un peu partout. Le problème, c'est l'effet domino. Un seul site "
      "piraté, et si vous avez le même mot de passe ailleurs, c'est toute votre vie qui s'ouvre : "
      "l'e-mail, puis via l'e-mail, la banque, les réseaux sociaux, tout."),
("key", "Un mot de passe réutilisé, c'est une seule clé qui ouvre toutes vos portes. Le voleur n'a "
        "besoin de la trouver qu'une seule fois."),

("slide", "24", "Les fuites de données (data breaches)", "3 min"),
("p", "Justement, un mot sur les fuites de données, parce que c'est un point qui déresponsabilise "
      "souvent, à tort. Même les très grandes entreprises, avec des moyens énormes, se font parfois "
      "pirater leurs bases de clients. Ça a touché des géants du web, des opérateurs, des sites de vente."),
("p", "Résultat : vos adresses e-mail, vos mots de passe, vos numéros de téléphone peuvent se retrouver "
      "en circulation sans que vous n'ayez rien fait de mal, et souvent sans même que vous le sachiez. "
      "C'est en grande partie hors de votre contrôle. Mais — et c'est le point important — vous pouvez "
      "limiter les dégâts."),
("p", "Il existe un outil gratuit et sérieux, « Have I Been Pwned », dont le nom veut dire à peu près "
      "« est-ce que je me suis fait avoir ». Vous y entrez votre adresse e-mail, et il vous dit dans "
      "quelles fuites connues elle apparaît. Si c'est le cas, pas de panique : cela veut simplement dire "
      "qu'il faut changer le mot de passe concerné — et ne plus jamais le réutiliser ailleurs."),
("key", "C'est toute l'importance d'un mot de passe unique par site : quand une fuite se produit, le "
        "dégât reste isolé à ce seul site, au lieu de se propager partout."),

("slide", "25", "Le Wi-Fi public : pratique mais risqué", "3 min"),
("p", "Dernier grand risque avant la pause : le Wi-Fi public. Celui de la gare, du café, de l'hôtel, de "
      "l'aéroport. C'est très pratique, surtout en voyage, mais c'est un réseau ouvert et partagé, et ça "
      "change tout."),
("p", "Deux dangers principaux. Premièrement, sur un réseau mal sécurisé, une personne mal intentionnée "
      "peut parfois « écouter » ce qui circule. Deuxièmement, les faux réseaux : n'importe qui peut créer "
      "un point d'accès nommé « WiFi_Gratuit_Gare » pour vous attirer et intercepter votre connexion. Le "
      "nom rassurant ne prouve rien du tout."),
("p", "Alors, faut-il bannir le Wi-Fi public ? Non, mais avec des réflexes. Évitez d'y faire des choses "
      "sensibles comme consulter votre banque ou faire un achat. Si vous devez le faire, préférez le "
      "partage de connexion de votre téléphone, en 4G ou 5G, qui est bien plus sûr. Et pour les plus "
      "prudents, un VPN chiffre votre connexion — on en reparlera brièvement tout à l'heure."),

("slide", "26", "Quiz express — vrai ou faux ?", "3 min 30"),
("p", "Avant la pause bien méritée, faisons un petit quiz pour vérifier qu'on est bien accordés. Je "
      "vous lis une affirmation, et vous me dites, à main levée : vrai ou faux ?"),
("inter", "Poser chaque question, laisser voter la salle à main levée, PUIS donner la réponse. C'est le "
          "moment le plus interactif de la première moitié : prendre son temps, féliciter, dédramatiser."),
("bul", [
    "« Le petit cadenas https garantit que le site est honnête. » FAUX. Le cadenas garantit seulement "
    "que la connexion est chiffrée, pas que le site est fiable. Un site d'arnaque peut très bien avoir "
    "un cadenas.",
    "« Un mot de passe très compliqué est incassable. » FAUX. S'il fuite dans une base de données "
    "piratée, sa complexité n'y change absolument rien : il est déjà connu.",
    "« Mon smartphone n'a besoin d'aucune précaution. » FAUX. C'est l'appareil le plus personnel que "
    "vous possédez, donc l'un des plus sensibles.",
]),
("trans", "« Sur cette bonne nouvelle — vous avez tous très bien répondu — je vous propose une pause de "
          "dix minutes. Notez vos questions, on y répondra juste après. »"),

# ============================== PAUSE =====================================
("part", "PAUSE  ·  1:06 → 1:16"),
("slide", "27", "Pause (10 minutes)", "10 min"),
("p", "[Pause de 10 minutes.] Profitez-en pour vous dégourdir les jambes, boire un verre d'eau, et "
      "surtout noter les questions qui vous sont venues. À votre retour, on passe à la partie la plus "
      "utile : comment se protéger, très concrètement."),
("tip", "Rester disponible pendant la pause : c'est souvent là que les gens osent poser, en tête à tête, "
        "la question qu'ils n'ont pas voulu poser devant tout le monde. Noter ces questions pour y "
        "répondre ensuite à la cantonade, de façon anonyme."),

# ======================= PARTIE 3 — SE PROTÉGER ===========================
("part", "PARTIE 3 — SE PROTÉGER AU QUOTIDIEN  ·  1:16 → 1:38"),

("slide", "28", "Ouverture de la Partie 3", "30 s"),
("p", "Bon retour à tous. Fini de faire peur : place aux solutions. Et vous allez voir, la plupart sont "
      "simples, gratuites, et se mettent en place en quelques minutes. On va aller du plus important au "
      "plus spécifique."),

("slide", "29", "Si vous ne retenez que 3 choses", "1 min 30"),
("p", "Si vous deviez ne retenir que trois choses de tout l'atelier, ce serait celles-ci. Un : des mots "
      "de passe solides et uniques, aidés d'un gestionnaire. Deux : les mises à jour, faites "
      "régulièrement, idéalement automatiques. Trois : la vigilance, ces fameuses trois secondes de "
      "réflexion avant de cliquer."),
("p", "Ces trois réflexes, à eux seuls, vous protègent déjà contre l'écrasante majorité des attaques du "
      "quotidien. Tout le reste, c'est du bonus. Alors si à un moment vous décrochez, revenez à ces trois "
      "piliers : mots de passe, mises à jour, vigilance."),

("slide", "30", "Mots de passe : erreurs vs bonnes pratiques", "3 min"),
("p", "Commençons par les mots de passe, puisque c'est le socle de tout. Voyons d'abord ce qu'il ne faut "
      "surtout pas faire, et vous allez peut-être vous reconnaître — c'est normal, sans jugement."),
("bul", [
    "À éviter : les grands classiques comme « 123456 », « azerty », « motdepasse », « 0000 ».",
    "À éviter : le prénom suivi de la date de naissance, trouvable en trente secondes sur les réseaux.",
    "À éviter : le même mot de passe partout — on a vu pourquoi, l'effet domino.",
    "À éviter : le mot de passe noté sur un post-it collé à l'écran, ou envoyé par SMS ou par e-mail.",
]),
("p", "Et maintenant, les bonnes pratiques, qui sont finalement assez simples. Un : de la longueur, au "
      "moins douze à quatorze caractères. Deux : une « phrase de passe » facile à retenir plutôt qu'un "
      "charabia. Trois : un mot de passe différent pour chaque site important. Quatre : on le range dans "
      "un gestionnaire dédié. Et cinq : on ajoute par-dessus la double authentification. On détaille les "
      "deux derniers points juste après, car ce sont les plus puissants."),

("slide", "31", "Fabriquer un bon mot de passe", "2 min 30"),
("p", "« D'accord, mais comment on fabrique un bon mot de passe dont on se souvient ? » C'est la vraie "
      "question. La méthode gagnante, c'est la phrase de passe. Au lieu de chercher un mot compliqué, "
      "vous prenez une petite phrase, si possible absurde, donc facile à retenir et difficile à deviner."),
("p", "Par exemple : « MonChatGrisMange3Croquettes! ». Comptez les caractères : c'est très long, donc "
      "très solide. C'est unique, personne n'ira le deviner. Et pourtant, vous vous en souvenez sans "
      "effort, parce que ça raconte une image. Retenez ce principe contre-intuitif : la longueur compte "
      "davantage que la complexité. Quatre mots assemblés valent mieux qu'un « P-arobase-s-s-zéro-r-d » "
      "impossible à mémoriser."),
("key", "Une phrase de passe de quatre mots est à la fois plus solide ET plus simple à retenir qu'un "
        "mot de passe court bourré de symboles. Longueur avant complexité."),

("slide", "32", "Le gestionnaire de mots de passe", "3 min"),
("p", "Mais soyons honnêtes : avoir un mot de passe unique et long pour chacun de ses quarante comptes, "
      "c'est humainement impossible à mémoriser. C'est là qu'intervient l'outil le plus utile de tout "
      "l'atelier : le gestionnaire de mots de passe."),
("p", "Imaginez un coffre-fort numérique. À l'intérieur, tous vos mots de passe, bien rangés. Vous, "
      "vous n'avez plus qu'une seule chose à retenir : le mot de passe maître qui ouvre le coffre — "
      "celui-là, on le soigne, c'est une belle phrase de passe. Le gestionnaire, lui, se charge du reste : "
      "il génère pour chaque site un mot de passe long, unique et incassable, et il le remplit "
      "automatiquement quand vous vous connectez."),
("p", "Résultat : c'est à la fois plus sûr ET plus pratique qu'avant. Fini les « mot de passe oublié ». "
      "Il existe des solutions gratuites et reconnues comme Bitwarden ou KeePass, et votre navigateur "
      "internet en propose déjà un, intégré. Le meilleur est celui que vous utiliserez vraiment."),
("key", "Le gestionnaire de mots de passe, c'est le meilleur retour sur investissement en cybersécurité "
        "pour un particulier. Un petit effort au départ, une tranquillité durable ensuite."),

("slide", "33", "La double authentification (2FA)", "3 min"),
("p", "Deuxième outil magique : la double authentification, qu'on note parfois « 2FA » ou « A2F ». Le "
      "principe est simple : en plus de votre mot de passe, on vous demande une deuxième preuve que "
      "c'est bien vous. C'est le principe de la carte bancaire : la carte plus le code."),
("p", "Cette deuxième preuve peut être un code reçu par SMS, un code affiché par une petite application "
      "sur votre téléphone comme Google ou Microsoft Authenticator, ou une clé physique pour les plus "
      "exigeants. L'intérêt est énorme : même si un pirate vole votre mot de passe, il ne peut rien "
      "faire sans ce deuxième facteur, qui est dans votre poche."),
("p", "Alors oui, c'est un tout petit peu moins pratique — il faut sortir son téléphone. Mais c'est "
      "infiniment plus sûr. Mon conseil : activez-la en priorité sur les comptes les plus sensibles, "
      "dans cet ordre : votre messagerie e-mail d'abord, puis votre banque, puis vos réseaux sociaux."),
("key", "La double authentification, c'est un deuxième verrou sur la porte. Un peu moins pratique, mais "
        "c'est l'une des protections les plus efficaces qui existent aujourd'hui."),

("slide", "34", "Les mises à jour : ne pas remettre à demain", "2 min"),
("p", "Parlons de ce petit message qu'on ferme tous machinalement : « Une mise à jour est disponible ». "
      "On la reporte, encore et encore. Grave erreur. Car une mise à jour, ce n'est pas seulement de "
      "nouvelles fonctions ou une icône qui change : c'est très souvent la correction de failles de "
      "sécurité que les pirates connaissent et exploitent déjà."),
("p", "Reporter une mise à jour, c'est laisser sciemment une fenêtre ouverte alors qu'on sait qu'un "
      "voleur rôde. Le bon réflexe : activez les mises à jour automatiques partout où c'est possible. "
      "Comme ça, vous n'avez même plus à y penser. Et n'oubliez pas que ça concerne tout : le téléphone, "
      "l'ordinateur, mais aussi les applications, la box internet, la télévision connectée, les objets "
      "connectés."),
("key", "Quand le choix se présente, cliquez sur « Installer maintenant » plutôt que sur « Me le "
        "rappeler demain ». Votre « vous » de demain vous remerciera."),

("slide", "35", "Antivirus, pare-feu : que faut-il vraiment ?", "2 min"),
("p", "Question qu'on me pose souvent : « Faut-il payer un antivirus ? » Rassurez-vous, la réponse est "
      "plutôt simple. Sur un ordinateur Windows, un antivirus reste utile — mais celui qui est déjà "
      "intégré et gratuit, Windows Defender, suffit largement pour la plupart des gens. Pas besoin, en "
      "général, d'acheter une usine à gaz."),
("p", "Le pare-feu, lui, est ce qui filtre les connexions entrantes et sortantes. Il est activé par "
      "défaut : laissez-le tranquille, il fait son travail. Mais attention au piège : aucun logiciel ne "
      "remplacera jamais votre vigilance. L'antivirus est un filet de sécurité, pas un bouclier magique. "
      "Il rattrape certaines erreurs, il n'empêche pas toutes les bêtises."),
("tip", "Insister sur ce point de bon sens : ces fenêtres qui hurlent « Votre PC est infecté, cliquez "
        "ici ! » sont, dans l'immense majorité des cas, l'arnaque elle-même. Un vrai antivirus ne "
        "s'affole pas dans une pop-up de navigateur."),

("slide", "36", "Les sauvegardes : votre filet de sécurité", "3 min"),
("p", "On l'a évoquée plusieurs fois, la voici enfin en détail : la sauvegarde. C'est votre assurance "
      "tous risques. Perte, vol, casse, rançongiciel, ou simplement le café renversé sur l'ordinateur : "
      "avec une sauvegarde, vous récupérez tout. Sans elle, vos photos et documents peuvent disparaître "
      "définitivement."),
("p", "Les professionnels résument la bonne méthode par une règle facile à retenir : la règle 3-2-1. "
      "Trois copies de vos données importantes : l'original plus deux sauvegardes. Sur deux supports "
      "différents : par exemple un disque dur externe et un service en ligne, un « cloud ». Et au moins "
      "une copie conservée hors de chez vous : ainsi, en cas d'incendie ou de cambriolage, vous ne "
      "perdez pas tout d'un coup."),
("key", "La règle 3-2-1 : trois copies, deux supports différents, une copie hors du domicile. Simple à "
        "retenir, redoutablement efficace."),

("slide", "37", "Pourquoi la sauvegarde change tout", "1 min 30"),
("p", "Je veux vraiment insister, parce que c'est peut-être le conseil le plus rentable de la journée. "
      "Avec une bonne sauvegarde, le pire scénario — un rançongiciel qui verrouille tout — devient gérable : "
      "on nettoie l'appareil, on restaure, et on continue sa vie. Sans sauvegarde, ce même incident est "
      "un drame irréversible."),
("p", "Un dernier point, et non des moindres : testez votre sauvegarde de temps en temps. Essayez de "
      "récupérer un fichier, pour vérifier que ça marche vraiment. Une sauvegarde qu'on n'a jamais testée "
      "est une sauvegarde en laquelle on ne peut pas avoir pleinement confiance. Beaucoup de gens "
      "découvrent le jour du problème que leur sauvegarde était vide depuis des mois."),

("slide", "38", "Naviguer sur internet en sécurité", "2 min"),
("p", "Quelques réflexes pour la navigation de tous les jours. D'abord, avant de saisir un identifiant "
      "ou un numéro de carte, jetez un œil à l'adresse du site, ce qu'on appelle l'URL, tout en haut. "
      "Est-ce bien le vrai site ? Attention aux fautes subtiles dans le nom."),
("p", "Rappelez-vous le quiz : le petit cadenas et le « https » signifient que la connexion est "
      "chiffrée, c'est bien, mais ça ne veut pas dire que le site est honnête. Méfiez-vous aussi des "
      "fenêtres qui surgissent, des boutons « Télécharger » clignotants, des fausses alertes. Et sur un "
      "ordinateur partagé — au travail, dans une bibliothèque — pensez toujours à vous déconnecter et à "
      "fermer votre session en partant."),

("slide", "39", "Protéger sa messagerie : la clé du royaume", "2 min"),
("p", "S'il y a bien un compte à protéger avant tous les autres, c'est votre boîte e-mail. Pourquoi ? "
      "Parce que c'est la clé du royaume. Réfléchissez : quand vous oubliez un mot de passe, comment "
      "faites-vous ? Vous cliquez sur « mot de passe oublié », et vous recevez un lien par e-mail."),
("p", "Cela veut dire que celui qui contrôle votre e-mail peut, de proche en proche, réinitialiser et "
      "prendre la main sur presque tous vos autres comptes : la banque, les réseaux sociaux, les achats "
      "en ligne. C'est le trousseau de clés de toute votre vie numérique. Donc, sur ce compte plus que "
      "tout autre : un mot de passe unique et solide, et la double authentification activée. Et méfiance "
      "sur les pièces jointes et les liens, même quand le message semble venir d'un proche — son compte à "
      "lui a peut-être été piraté."),
("key", "Si vous ne sécurisez qu'un seul compte en rentrant ce soir, que ce soit votre adresse e-mail "
        "principale."),

("slide", "40", "Réseaux sociaux et vie privée", "2 min 30"),
("p", "Terminons cette partie par les réseaux sociaux. Ils sont formidables pour garder le lien, mais "
      "ils nous poussent à partager, parfois un peu trop. Premier réflexe : allez dans les réglages de "
      "confidentialité et vérifiez qui peut voir vos publications. Souvent, c'est réglé sur « public » "
      "par défaut, c'est-à-dire le monde entier."),
("p", "Deuxième réflexe : limitez les informations personnelles que vous rendez publiques — votre "
      "adresse, votre lieu de travail, et surtout vos absences. Méfiez-vous aussi des petits jeux et "
      "quiz du type « quel personnage es-tu ? » : beaucoup sont conçus pour aspirer vos données et celles "
      "de vos amis."),
("p", "Et gardez en tête deux idées. D'une part, ce qui est publié en ligne peut y rester très, très "
      "longtemps, et échapper à votre contrôle. D'autre part, une belle photo postée en direct de vos "
      "vacances, c'est aussi une façon d'annoncer publiquement : « ma maison est vide en ce moment ». "
      "Rien n'interdit de partager — mais mieux vaut le faire au retour."),
("trans", "« On a vu les grands principes. Voyons maintenant comment ils s'appliquent à des situations "
          "très concrètes de la vie quotidienne. »"),

# ======================= PARTIE 4 — CAS CONCRETS ==========================
("part", "PARTIE 4 — CAS CONCRETS DE LA VIE QUOTIDIENNE  ·  1:38 → 1:47"),

("slide", "41", "Ouverture de la Partie 4", "30 s"),
("p", "Petite partie, mais très pratique : quelques situations du quotidien, avec pour chacune les deux "
      "ou trois réflexes qui comptent vraiment. Smartphone, objets connectés, achats en ligne, enfants, "
      "et télétravail."),

("slide", "42", "Votre smartphone", "2 min"),
("p", "Commençons par l'objet le plus intime que vous possédez : votre smartphone. Il contient souvent "
      "plus d'informations sensibles que votre ordinateur. Les réflexes essentiels : verrouillez-le avec "
      "un code d'au moins six chiffres — pas « 0000 » ni « 1234 » — complété par l'empreinte ou la "
      "reconnaissance du visage."),
("p", "Ensuite, n'installez des applications que depuis les magasins officiels, l'App Store sur iPhone "
      "et le Play Store sur Android. Vérifiez les autorisations que réclame chaque application : "
      "pourquoi une simple lampe torche voudrait-elle accéder à vos contacts et à votre micro ? Et "
      "enfin, activez la fonction « Localiser mon appareil » : en cas de perte ou de vol, vous pourrez "
      "le localiser, le verrouiller à distance, ou même effacer son contenu."),

("slide", "43", "Les objets connectés (maison intelligente)", "1 min 30"),
("p", "De plus en plus d'objets se connectent à internet : caméras de surveillance, montres, assistants "
      "vocaux, télévisions, thermostats, et même des jouets pour enfants. Chacun est un petit ordinateur, "
      "donc une porte d'entrée potentielle dans votre foyer."),
("p", "Deux réflexes suffisent pour l'essentiel. Un : dès l'installation, changez immédiatement le mot "
      "de passe par défaut, qui est souvent quelque chose comme « admin / admin », connu de tous les "
      "pirates. Deux : mettez ces objets à jour, comme le reste. Le comble de l'ironie, ce serait qu'une "
      "caméra installée pour vous protéger serve, mal configurée, à vous surveiller."),

("slide", "44", "Achats et banque en ligne", "2 min"),
("p", "Les achats et la banque en ligne, maintenant. C'est très sûr aujourd'hui, à condition de "
      "respecter quelques règles. Achetez sur des sites que vous connaissez, et méfiez-vous des prix "
      "« trop beaux pour être vrais » : c'est souvent le signe d'une arnaque ou d'une contrefaçon."),
("p", "Si votre banque le propose, utilisez une carte virtuelle à usage unique pour vos achats en "
      "ligne, ou fixez des plafonds. Surveillez régulièrement vos relevés bancaires, pour repérer vite "
      "un débit anormal. Et surtout, gravez ceci dans le marbre : votre banque ne vous demandera JAMAIS "
      "votre code secret, ni vos codes de validation, par téléphone, par SMS ou par e-mail. Jamais."),
("key", "Un doute sur un appel soi-disant « de votre banque » ? Raccrochez, et rappelez vous-même le "
        "numéro officiel qui figure au dos de votre carte. Une vraie banque comprendra parfaitement."),

("slide", "45", "Les enfants et le numérique", "1 min 30"),
("p", "Pour ceux qui ont des enfants ou des petits-enfants, quelques repères. Activez le contrôle "
      "parental : il permet de limiter le temps d'écran, de filtrer les contenus et de bloquer les "
      "achats. Mais l'outil ne fait pas tout : le plus important, c'est le dialogue et la confiance, "
      "pour que l'enfant vienne vous voir en cas de problème plutôt que de se cacher."),
("p", "Expliquez-leur, avec des mots simples, les inconnus en ligne, le harcèlement, et le fait que "
      "certaines images ne doivent jamais être partagées. Et pensez aussi à protéger LEURS données : "
      "évitez de publier trop de photos et d'informations sur eux — ils n'ont pas choisi cette exposition, "
      "et elle les suivra."),

("slide", "46", "Le télétravail et les usages pro", "1 min 30"),
("p", "Enfin, pour celles et ceux qui télétravaillent. La règle d'or : séparez autant que possible le "
      "professionnel et le personnel. Évitez de traiter des documents de travail sensibles sur votre "
      "ordinateur familial, et inversement."),
("p", "Utilisez les outils fournis par votre employeur, notamment le VPN de l'entreprise, qui crée un "
      "tunnel sécurisé pour accéder aux ressources internes. Ne stockez pas des documents professionnels "
      "sensibles n'importe où, sur une clé USB perdue ou un cloud personnel. Et prenez le réflexe de "
      "verrouiller votre session dès que vous quittez votre poste, même à la maison. En cas de doute sur "
      "la marche à suivre, votre service informatique est là pour ça : mieux vaut une question de trop "
      "qu'un incident."),
("trans", "« Malgré toutes ces précautions, personne n'est jamais protégé à 100 %. Alors voyons comment "
          "réagir si, un jour, ça vous arrive. »"),

# ======================= PARTIE 5 — RÉAGIR ================================
("part", "PARTIE 5 — RÉAGIR EN CAS DE PROBLÈME  ·  1:47 → 1:55"),

("slide", "47", "Ouverture de la Partie 5", "30 s"),
("p", "Cette partie est importante, parce que la peur vient souvent du sentiment d'impuissance. Or, il "
      "existe des gestes clairs à faire, et des interlocuteurs pour vous aider. Savoir cela change tout : "
      "on passe de la panique à l'action."),

("slide", "48", "Reconnaître qu'il se passe quelque chose", "2 min"),
("p", "D'abord, comment savoir qu'on est peut-être victime de quelque chose ? Voici les signaux qui "
      "doivent vous alerter."),
("bul", [
    "Votre appareil devient anormalement lent, chauffe, ou des fenêtres publicitaires surgissent sans arrêt.",
    "Des fichiers deviennent inaccessibles, ou portent des noms bizarres : signe typique d'un rançongiciel.",
    "Vos mots de passe ne fonctionnent plus, ou vous recevez des alertes de connexion inconnues.",
    "Vos proches reçoivent des messages étranges soi-disant « de votre part ».",
    "Vous constatez des débits bancaires que vous ne reconnaissez pas.",
]),
("p", "Aucun de ces signes n'est une preuve absolue à lui seul, mais s'ils s'accumulent, il faut réagir. "
      "Et réagir, ce n'est pas paniquer : c'est suivre une petite procédure."),

("slide", "49", "Que faire immédiatement ?", "2 min"),
("p", "Voici les bons gestes, dans l'ordre, si vous pensez être victime d'une attaque."),
("bul", [
    "Un : gardez votre calme. La panique est mauvaise conseillère et fait commettre des erreurs.",
    "Deux : déconnectez l'appareil d'internet — coupez le Wi-Fi ou débranchez le câble — pour stopper "
    "la propagation et couper le lien avec l'attaquant.",
    "Trois : changez vos mots de passe importants, mais depuis un AUTRE appareil sain, pas depuis celui "
    "que vous soupçonnez infecté.",
    "Quatre : en cas de fraude bancaire, prévenez immédiatement votre banque et faites opposition.",
    "Cinq : conservez les preuves — captures d'écran, messages, e-mails — elles seront utiles pour "
    "porter plainte.",
    "Six : ne payez jamais une rançon sans l'avis d'un professionnel.",
]),
("key", "Agir vite limite les dégâts, mais agir calmement les limite encore plus. Une procédure connue "
        "à l'avance évite de réfléchir dans l'urgence."),

("slide", "50", "À qui s'adresser (en France)", "1 min 30"),
("p", "Et surtout, vous n'êtes pas seul. Il existe des ressources officielles et gratuites, faites "
      "exactement pour ça. Notez-les, ou plutôt : sachez qu'elles existent, vous les retrouverez sur la "
      "dernière diapositive."),
("bul", [
    "Le site cybermalveillance.gouv.fr : le service public d'assistance aux victimes. Il vous aide à "
    "poser un diagnostic et vous met en relation avec des professionnels près de chez vous.",
    "La plateforme 17Cyber, le nouveau guichet unique en ligne pour être orienté et assisté en cas "
    "d'incident.",
    "Le dépôt de plainte, au commissariat ou à la gendarmerie, en cas d'escroquerie ou de piratage.",
    "Le signalement des contenus et arnaques sur internet-signalement.gouv.fr, la plateforme Pharos.",
    "La CNIL, cnil.fr, pour tout ce qui touche à vos données personnelles.",
    "Et bien sûr votre banque, pour l'opposition et le remboursement des fraudes.",
]),

("slide", "51", "Vos droits : le RGPD en une diapo", "1 min 30"),
("p", "Un mot, pour finir cette partie, sur vos droits. Vous avez peut-être entendu parler du RGPD, le "
      "règlement européen sur la protection des données. Derrière ce sigle un peu austère se cache une "
      "bonne nouvelle : il vous donne des droits concrets sur vos données personnelles."),
("p", "Vous avez le droit de savoir quelles données une entreprise détient sur vous : c'est le droit "
      "d'accès. Le droit de faire corriger une information fausse : la rectification. Le droit de "
      "demander leur effacement, ce qu'on appelle le « droit à l'oubli ». Et votre consentement doit "
      "être libre et éclairé — c'est tout l'enjeu des bandeaux « cookies » que vous voyez partout. Si "
      "une entreprise ne respecte pas ces droits, la CNIL est là pour vous défendre."),
("key", "Vous n'êtes pas démuni face aux grandes plateformes : la loi vous donne des droits, et un "
        "gendarme, la CNIL, pour les faire respecter."),
("trans", "« Il est temps de rassembler tout ça en une conclusion simple et actionnable. »"),

# ======================= CONCLUSION =======================================
("part", "CONCLUSION ET QUESTIONS  ·  1:55 → 2:00+"),

("slide", "52", "Ouverture de la conclusion", "30 s"),
("p", "On arrive au bout. Je ne vais pas tout résumer point par point, mais vous donner l'essentiel à "
      "emporter chez vous, sous une forme facile à garder."),

("slide", "53", "Les 10 bonnes habitudes", "3 min"),
("p", "Voici votre check-list, dix bonnes habitudes. Prenez-la en photo, elle résume tout l'atelier."),
("bul", [
    "Un : des mots de passe longs et uniques.",
    "Deux : un gestionnaire de mots de passe pour ne plus avoir à les retenir.",
    "Trois : la double authentification, surtout sur votre e-mail.",
    "Quatre : les mises à jour activées, idéalement automatiques.",
    "Cinq : des sauvegardes régulières, selon la règle 3-2-1.",
    "Six : réfléchir avant de cliquer — les fameuses trois secondes.",
    "Sept : vérifier l'expéditeur d'un message et l'adresse d'un site.",
    "Huit : la prudence sur le Wi-Fi public.",
    "Neuf : régler la confidentialité de ses comptes et réseaux sociaux.",
    "Dix : savoir demander de l'aide, sans honte, quand on a un doute.",
]),
("key", "Regardez bien cette liste : aucune de ces habitudes n'est technique. Toutes sont à votre "
        "portée, et vous pouvez en mettre plusieurs en place dès ce soir."),

("slide", "54", "Le réflexe à retenir : 3 secondes", "1 min"),
("p", "Et si vraiment vous ne deviez retenir qu'une seule chose, une seule, ce serait celle-ci : dans "
      "le doute, on ne clique pas, on vérifie. Ça prend trois secondes. Trois secondes de recul avant "
      "de cliquer sur un lien, d'ouvrir une pièce jointe, de donner une information."),
("p", "Ces trois secondes, c'est le temps que met votre bon sens à rattraper votre réflexe. C'est, de "
      "loin, votre meilleure protection, tous les jours, gratuitement. Les escrocs comptent sur votre "
      "vitesse et votre émotion ; votre arme, c'est la lenteur et le calme."),

("slide", "55", "Pour aller plus loin (ressources fiables)", "1 min 30"),
("p", "Pour continuer à apprendre, voici des ressources fiables, gratuites et officielles. Le site "
      "cybermalveillance.gouv.fr, pour des conseils clairs et de l'assistance. Le site de la CNIL, "
      "cnil.fr, pour tout ce qui concerne votre vie privée. Les guides de l'ANSSI, l'agence nationale, "
      "sur ssi.gouv.fr, très pédagogiques."),
("p", "Le site haveibeenpwned.com, dont on a parlé, pour vérifier si votre adresse e-mail a fuité. Le "
      "gestionnaire de mots de passe que vous aurez choisi, avec ses tutoriels. Et enfin, tout "
      "simplement, vos notes d'aujourd'hui et cette check-list. Vous avez déjà l'essentiel."),

("slide", "56", "Le message à retenir", "2 min"),
("p", "Je voudrais conclure en vous rassurant, parce qu'on a parlé de beaucoup de menaces. La "
      "cybersécurité, ce n'est pas de la magie réservée aux informaticiens. C'est du bon sens, un peu "
      "outillé. Quelques réflexes simples suffisent à éliminer l'immense majorité des risques du "
      "quotidien."),
("p", "L'objectif n'est pas d'atteindre le risque zéro — il n'existe pas, ni en ligne ni dans la vraie "
      "vie. L'objectif, c'est de ne plus être une cible facile, et de savoir quoi faire s'il y a un "
      "souci. Et rappelez-vous que la sécurité est un sport d'équipe : le meilleur service à rendre à "
      "vos proches, surtout les plus vulnérables, c'est de partager avec eux ce que vous avez appris "
      "aujourd'hui."),
("key", "Protéger ses données, au fond, ce n'est pas une affaire de technique : c'est protéger sa "
        "tranquillité, son argent, et ses proches."),

("slide", "57", "Merci et questions", "10 min et +"),
("p", "Voilà, je vous remercie sincèrement de votre attention et de votre participation. J'espère que "
      "vous repartez avec des idées claires et, surtout, avec l'envie de mettre en place une ou deux "
      "choses dès ce soir. Commencez petit : activez la double authentification sur votre e-mail, par "
      "exemple. C'est déjà un grand pas."),
("inter", "Ouvrir largement les questions. Réutiliser les questions notées pendant la pause. Si un "
          "silence s'installe, relancer : « La question qu'on me pose le plus souvent, c'est... » et "
          "prendre un exemple concret. Terminer sur une note positive et encourageante."),
("tip", "Si le temps le permet, proposer un mini atelier pratique : aider les volontaires à activer, "
        "en direct sur leur téléphone, la double authentification de leur messagerie. Rien n'ancre "
        "mieux un conseil qu'un premier geste réussi ensemble."),

# ======================= ANNEXE — Q/R =====================================
("part", "ANNEXE — QUESTIONS FRÉQUENTES DU PUBLIC (préparation de l'orateur)"),
("p", "Cette annexe ne se lit pas pendant l'exposé : elle prépare le temps de questions. Voici les "
      "questions qui reviennent le plus souvent avec un public non spécialiste, et des réponses "
      "courtes, justes et rassurantes que vous pouvez reformuler avec vos mots."),

("sec", "« Un mot de passe différent pour chaque site, c'est impossible à retenir ! »"),
("p", "Vous avez tout à fait raison, et personne n'y arrive de tête. C'est exactement le rôle du "
      "gestionnaire de mots de passe : lui les retient à votre place, et vous n'avez plus qu'un seul "
      "mot de passe maître à mémoriser. On ne vous demande pas un effort de mémoire surhumain, on vous "
      "propose un outil qui fait le travail."),

("sec", "« Mettre tous mes mots de passe au même endroit, ce n'est pas risqué ? »"),
("p", "C'est la première inquiétude, elle est légitime. Deux réponses. D'abord, le coffre est chiffré : "
      "même volé, son contenu est illisible sans le mot de passe maître. Ensuite, comparez au risque "
      "réel actuel : réutiliser le même mot de passe partout, ou les noter sur un carnet, est bien plus "
      "dangereux. Le gestionnaire n'est pas parfait, mais il est très nettement plus sûr que nos "
      "habitudes actuelles."),

("sec", "« La double authentification par SMS, est-ce vraiment fiable ? »"),
("p", "Le code par SMS n'est pas la méthode la plus solide — il existe des attaques ciblées contre le "
      "SMS — mais il vaut infiniment mieux que pas de double authentification du tout. Pour un "
      "particulier, le SMS est déjà une excellente protection. Si vous voulez aller plus loin, une "
      "application d'authentification sur le téléphone est encore plus sûre."),

("sec", "« Comment savoir si un message vient vraiment de ma banque ? »"),
("p", "La règle est simple : on ne le vérifie jamais en cliquant dans le message. On ferme le message, "
      "et on ouvre soi-même l'application officielle de la banque, ou on appelle le numéro qui figure au "
      "dos de la carte. Si l'information est vraie, vous la retrouverez dans votre espace client. Une "
      "vraie banque ne vous en voudra jamais de vérifier."),

("sec", "« J'ai cliqué sur un lien suspect. Qu'est-ce que je fais maintenant ? »"),
("p", "Pas de panique, et ce n'est pas honteux. Si vous avez seulement cliqué sans rien saisir, le "
      "risque est souvent limité : surveillez l'appareil et faites une mise à jour. Si vous avez saisi "
      "un mot de passe, changez-le immédiatement, ainsi que celui des comptes qui utilisaient le même. "
      "Si vous avez donné des informations bancaires, appelez tout de suite votre banque. Et en cas de "
      "doute, le site cybermalveillance.gouv.fr vous guide pas à pas."),

("sec", "« Les Mac et les iPhone n'ont pas de virus, si ? »"),
("p", "C'est un mythe tenace. Il y a historiquement moins de logiciels malveillants sur ces appareils, "
      "mais ils ne sont pas magiques. Et surtout, la principale menace — le hameçonnage, les arnaques, "
      "les mots de passe faibles — ne dépend pas du tout de la marque de l'appareil. Les bons réflexes "
      "valent pour tout le monde, sur toutes les plateformes."),

("sec", "« Le VPN, c'est quoi, et est-ce que j'en ai besoin ? »"),
("p", "Un VPN crée un tunnel chiffré entre votre appareil et internet : il protège surtout votre "
      "connexion sur les réseaux Wi-Fi publics. Pour un usage à la maison, avec une box à jour, ce n'est "
      "pas indispensable. C'est utile si vous vous connectez souvent en déplacement. Méfiez-vous des VPN "
      "« gratuits » : s'ils sont gratuits, ils se paient souvent avec vos données."),

("sec", "« Faut-il couvrir sa webcam ? »"),
("p", "Ce n'est pas de la paranoïa : coller une petite pastille sur la webcam d'un ordinateur portable "
      "est un geste simple, gratuit et sans inconvénient. C'est une sécurité de bon sens, au cas où. "
      "Beaucoup d'ordinateurs récents ont d'ailleurs un petit cache intégré prévu pour ça."),

("sec", "« Mes enfants s'y connaissent mieux que moi, comment les protéger ? »"),
("p", "Vous n'avez pas besoin d'être plus fort qu'eux en technique. Votre rôle, c'est le cadre et le "
      "dialogue : le contrôle parental pour l'âge, des règles claires sur le temps d'écran, et surtout "
      "une relation de confiance pour qu'ils viennent vous voir en cas de souci. La technologie change, "
      "le rôle d'un parent, non."),

("sec", "« On me demande mes données partout. Comment limiter ? »"),
("p", "Adoptez le réflexe du minimum : ne donnez que ce qui est vraiment nécessaire, refusez les "
      "cookies non essentiels, et méfiez-vous des formulaires trop curieux. Le RGPD vous permet aussi de "
      "demander l'effacement de vos données. On ne peut pas tout maîtriser, mais chaque information non "
      "donnée est une information qui ne pourra pas fuiter."),
]


# ==========================================================================
#  RENDU PDF
# ==========================================================================
def build_pdf(path):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=18 * mm, bottomMargin=18 * mm,
                            title="Discours — La cybersécurité",
                            author="Atelier de sensibilisation")
    story = []

    # --- Page de garde ---
    story.append(Spacer(1, 40 * mm))
    story.append(Paragraph("La cybersécurité", st_title))
    story.append(Paragraph("Protéger ses données à l'ère du numérique", st_sub))
    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width="60%", thickness=1.2, color=TEAL,
                            spaceBefore=2, spaceAfter=10, hAlign="CENTER"))
    story.append(Paragraph("DISCOURS COMPLET DE L'ORATEUR", ParagraphStyle(
        "kick", fontName="Vera-Bold", fontSize=11, textColor=TEAL,
        alignment=TA_CENTER, spaceAfter=10)))
    story.append(Paragraph("Atelier de sensibilisation · Durée : 2 heures "
                           "· Public non spécialiste", st_meta))
    story.append(Paragraph("Support aligné sur la présentation de 57 diapositives", st_meta))
    story.append(PageBreak())

    # --- Mode d'emploi + minutage ---
    story.append(part_bar("COMMENT UTILISER CE DOCUMENT"))
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(
        "Ce document contient l'intégralité de ce que l'orateur peut dire, diapositive par "
        "diapositive. Le texte courant correspond au discours à prononcer (vous pouvez le lire "
        "presque tel quel, ou le reformuler avec vos mots). Les encadrés de couleur sont des "
        "repères pour vous, l'animateur : ils ne se lisent pas à voix haute.", st_body))
    story.append(Spacer(1, 2 * mm))
    story.append(callout("trans", "annonce le passage d'une idée ou d'une partie à la suivante."))
    story.append(Spacer(1, 2 * mm))
    story.append(callout("tip", "conseil pour animer, rythmer ou illustrer le propos."))
    story.append(Spacer(1, 2 * mm))
    story.append(callout("inter", "moment d'échange avec la salle (sondage, question, exercice)."))
    story.append(Spacer(1, 2 * mm))
    story.append(callout("key", "phrase forte à marquer, à répéter ou à laisser résonner."))
    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph("Minutage indicatif (2 heures)", st_lead))
    for line in [
        "Accueil et introduction .................... 0:00 → 0:08",
        "Partie 1 · Comprendre le monde numérique ... 0:08 → 0:33",
        "Partie 2 · Les menaces courantes ........... 0:33 → 1:06",
        "Pause ...................................... 1:06 → 1:16",
        "Partie 3 · Se protéger au quotidien ........ 1:16 → 1:38",
        "Partie 4 · Cas concrets .................... 1:38 → 1:47",
        "Partie 5 · Réagir en cas de problème ....... 1:47 → 1:55",
        "Conclusion et questions .................... 1:55 → 2:00 et +",
    ]:
        story.append(Paragraph(esc(line), ParagraphStyle(
            "tl", fontName="Vera", fontSize=10, leading=16, textColor=DARK, leftIndent=6)))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "Les durées sont des repères souples : elles incluent les temps d'échange. Un bon atelier "
        "respire — n'hésitez pas à ralentir sur les moments interactifs et à raccourcir les "
        "passages que la salle maîtrise déjà.", ParagraphStyle(
            "note", fontName="Vera-Italic", fontSize=9.5, leading=14, textColor=GREY)))

    # --- Corps du discours ---
    for block in BLOCKS:
        kind = block[0]
        if kind == "part":
            story.append(PageBreak())
            story.append(part_bar(block[1]))
            story.append(Spacer(1, 5 * mm))
        elif kind == "slide":
            story.append(Spacer(1, 4 * mm))
            story.append(slide_head(block[1], block[2], block[3]))
            story.append(Spacer(1, 2.5 * mm))
        elif kind == "p":
            story.append(Paragraph(esc(block[1]), st_body))
        elif kind == "lead":
            story.append(Paragraph(esc(block[1]), st_lead))
        elif kind == "sec":
            story.append(Paragraph(esc(block[1]), st_section))
        elif kind == "bul":
            for item in block[1]:
                story.append(Paragraph(esc(item), st_bul, bulletText="\u2022"))
            story.append(Spacer(1, 3))
        elif kind in CALLOUTS:
            story.append(Spacer(1, 1.5 * mm))
            story.append(callout(kind, block[1]))
            story.append(Spacer(1, 1.5 * mm))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)


# ==========================================================================
#  RENDU MARKDOWN
# ==========================================================================
def build_md(path):
    out = []
    out.append("# La cybersécurité : protéger ses données à l'ère du numérique")
    out.append("### Discours complet de l'orateur")
    out.append("*Atelier de sensibilisation · Durée : 2 heures · Public non spécialiste*")
    out.append("*Support aligné sur la présentation de 57 diapositives "
               "(`cybersecurite_presentation.pptx`).*")
    out.append("")
    out.append("## Comment utiliser ce document")
    out.append("Le texte courant correspond au **discours à prononcer**. Les encadrés sont des "
               "repères pour l'animateur (ils ne se lisent pas à voix haute) :")
    out.append("")
    out.append("- **➜ Transition** — passage d'une idée à la suivante.")
    out.append("- **💡 Conseil d'animation** — pour rythmer ou illustrer.")
    out.append("- **🙋 Interaction** — moment d'échange avec la salle.")
    out.append("- **🔑 À retenir** — phrase forte à marquer.")
    out.append("")
    out.append("### Minutage indicatif (2 heures)")
    out.append("| Séquence | Horaire |")
    out.append("|---|---|")
    out.append("| Accueil et introduction | 0:00 → 0:08 |")
    out.append("| Partie 1 · Comprendre le monde numérique | 0:08 → 0:33 |")
    out.append("| Partie 2 · Les menaces courantes | 0:33 → 1:06 |")
    out.append("| Pause | 1:06 → 1:16 |")
    out.append("| Partie 3 · Se protéger au quotidien | 1:16 → 1:38 |")
    out.append("| Partie 4 · Cas concrets | 1:38 → 1:47 |")
    out.append("| Partie 5 · Réagir en cas de problème | 1:47 → 1:55 |")
    out.append("| Conclusion et questions | 1:55 → 2:00 et + |")
    out.append("")

    for block in BLOCKS:
        kind = block[0]
        if kind == "part":
            out.append("")
            out.append("---")
            out.append("## " + block[1])
        elif kind == "slide":
            out.append("")
            out.append("### Diapositive %s — %s  ·  ⏱ %s" % (block[1], block[2], block[3]))
        elif kind in ("p", "lead"):
            out.append(block[1])
            out.append("")
        elif kind == "sec":
            out.append("**" + block[1] + "**")
            out.append("")
        elif kind == "bul":
            for item in block[1]:
                out.append("- " + item)
            out.append("")
        elif kind in CALLOUTS:
            label = CALLOUTS[kind][3]
            out.append("> **%s —** %s" % (label, block[1]))
            out.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


# ==========================================================================
def count_words():
    n = 0
    for b in BLOCKS:
        if b[0] in ("p", "lead", "sec") + tuple(CALLOUTS):
            n += len(b[1].split())
        elif b[0] == "bul":
            n += sum(len(x.split()) for x in b[1])
    return n


if __name__ == "__main__":
    build_pdf("discours_cybersecurite.pdf")
    build_md("discours_cybersecurite.md")
    n_slides = sum(1 for b in BLOCKS if b[0] == "slide")
    print("OK — PDF + Markdown generes.")
    print("   Diapos couvertes : %d" % n_slides)
    print("   Mots (discours)  : ~%d" % count_words())
