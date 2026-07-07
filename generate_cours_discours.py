#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère le DISCOURS COMPLET (support de l'enseignant) :
    « Normes et méthodes de sécurité » — cours de licence 3 (40 h)

Le contenu est lu depuis `cours_contenu.SLIDES` (source unique partagée avec le
générateur de présentation), ce qui garantit un alignement diapositive par diapositive.

Sorties :
    - discours_normes_securite_40h.pdf   (document principal, prêt à imprimer)
    - discours_normes_securite_40h.md    (même contenu, lisible partout)

Dépendances : reportlab
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

import cours_contenu

# --------------------------------------------------------------------------
# Polices (Bitstream Vera, livrées avec reportlab)
# --------------------------------------------------------------------------
FDIR = os.path.join(os.path.dirname(reportlab.__file__), "fonts")
pdfmetrics.registerFont(TTFont("Vera",          os.path.join(FDIR, "Vera.ttf")))
pdfmetrics.registerFont(TTFont("Vera-Bold",     os.path.join(FDIR, "VeraBd.ttf")))
pdfmetrics.registerFont(TTFont("Vera-Italic",   os.path.join(FDIR, "VeraIt.ttf")))
pdfmetrics.registerFont(TTFont("Vera-BoldItalic", os.path.join(FDIR, "VeraBI.ttf")))
pdfmetrics.registerFontFamily("Vera", normal="Vera", bold="Vera-Bold",
                               italic="Vera-Italic", boldItalic="Vera-BoldItalic")

# --------------------------------------------------------------------------
# Couleurs (alignées sur la palette du cours)
# --------------------------------------------------------------------------
NAVY   = HexColor("#0E1B2A")   # bleu nuit profond
BLUE   = HexColor("#356A9A")   # bleu ardoise
TEAL   = HexColor("#2F7E78")   # teal
GOLD   = HexColor("#C7A24A")   # or
RED    = HexColor("#B03A2E")   # rouge sobre
ORANGE = HexColor("#C26B2D")   # ambre
GREY   = HexColor("#636F7B")   # texte secondaire
DARK   = HexColor("#1C2733")   # texte principal
WHITE  = HexColor("#FFFFFF")

# Encadrés : (couleur_accent, fond, étiquette_PDF, étiquette_Markdown)
CALLOUTS = {
    "trans": (BLUE,   HexColor("#EAF1F9"), "TRANSITION",            "➜ Transition"),
    "tip":   (TEAL,   HexColor("#E6F4F1"), "CONSEIL D'ANIMATION",   "💡 Conseil d'animation"),
    "inter": (ORANGE, HexColor("#FCEEE3"), "INTERACTION — À FAIRE", "🙋 Interaction"),
    "key":   (NAVY,   HexColor("#E7ECF2"), "À RETENIR",             "🔑 À retenir"),
    "obj":   (BLUE,   HexColor("#EBF4F8"), "OBJECTIF",              "🎯 Objectif"),
    "def":   (GOLD,   HexColor("#FFF8E7"), "DÉFINITION",            "📖 Définition"),
    "ex":    (TEAL,   HexColor("#E6F5F0"), "EXEMPLE",               "💡 Exemple"),
    "warn":  (RED,    HexColor("#FDEAEA"), "POINT DE VIGILANCE",    "⚠️  Vigilance"),
}

MARGIN = 18 * mm
USABLE = A4[0] - 2 * MARGIN

# --------------------------------------------------------------------------
# Styles de paragraphes
# --------------------------------------------------------------------------
st_title   = ParagraphStyle("title",   fontName="Vera-Bold", fontSize=24, leading=30,
                             textColor=NAVY, alignment=TA_CENTER, spaceAfter=6)
st_sub     = ParagraphStyle("sub",     fontName="Vera-Italic", fontSize=13, leading=18,
                             textColor=BLUE, alignment=TA_CENTER, spaceAfter=4)
st_meta    = ParagraphStyle("meta",    fontName="Vera", fontSize=10, leading=14,
                             textColor=GREY, alignment=TA_CENTER)
st_h1      = ParagraphStyle("h1",      fontName="Vera-Bold", fontSize=14, leading=18,
                             textColor=WHITE)
st_h2      = ParagraphStyle("h2",      fontName="Vera-Bold", fontSize=12.5, leading=15,
                             textColor=NAVY)
st_body    = ParagraphStyle("body",    fontName="Vera", fontSize=10.5, leading=15.5,
                             textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=6)
st_bul     = ParagraphStyle("bul",     fontName="Vera", fontSize=10.5, leading=15,
                             textColor=DARK, alignment=TA_LEFT, leftIndent=14,
                             bulletIndent=2, spaceAfter=3)
st_section = ParagraphStyle("section", fontName="Vera-Bold", fontSize=11, leading=15,
                             textColor=NAVY, spaceBefore=4, spaceAfter=4)
st_lead    = ParagraphStyle("lead",    fontName="Vera-BoldItalic", fontSize=11,
                             leading=16, textColor=NAVY, spaceAfter=6)


def esc(t):
    """Échappe le texte pour ReportLab et remplace les caractères hors-Vera."""
    t = t.replace("\u2192", "»")
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------------
# Constructeurs de blocs (flowables)
# --------------------------------------------------------------------------
def module_bar(text):
    """Bandeau coloré de section (fond bleu nuit)."""
    p = Paragraph(esc(text), st_h1)
    t = Table([[p]], colWidths=[USABLE])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def slide_head(num, title):
    """En-tête souligné pour chaque diapositive."""
    left = Paragraph("Diapositive %s — %s" % (num, esc(title)), st_h2)
    t = Table([[left]], colWidths=[USABLE])
    t.setStyle(TableStyle([
        ("LINEBELOW",     (0, 0), (-1, -1), 1.2, TEAL),
        ("VALIGN",        (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def callout(kind, text):
    """Encadré de couleur pour les repères enseignant."""
    accent, tint, label, _ = CALLOUTS[kind]
    lab  = Paragraph(label, ParagraphStyle(
        "lab", fontName="Vera-Bold", fontSize=8,
        textColor=accent, leading=11, spaceAfter=3))
    body = Paragraph(esc(text), ParagraphStyle(
        "cob", fontName="Vera", fontSize=10,
        textColor=DARK, leading=14.5, alignment=TA_JUSTIFY))
    t = Table([[[lab, body]]], colWidths=[USABLE])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), tint),
        ("LINEBEFORE",    (0, 0), (0, -1),  3, accent),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 9),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


# --------------------------------------------------------------------------
# En-tête / pied de page PDF
# --------------------------------------------------------------------------
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Vera", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, 10 * mm,
                      "Discours enseignant — Normes et méthodes de sécurité (L3, 40 h)")
    canvas.drawRightString(A4[0] - MARGIN, 10 * mm, "p. %d" % doc.page)
    canvas.setStrokeColor(HexColor("#D6DFEA"))
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 13 * mm, A4[0] - MARGIN, 13 * mm)
    canvas.restoreState()


# --------------------------------------------------------------------------
# Rendu des blocs de discours (partagé PDF / Markdown)
# --------------------------------------------------------------------------
def _render_speech_pdf(speech, story):
    """Ajoute les blocs de discours d'une diapositive au story ReportLab."""
    for tag, content in speech:
        if tag == "p":
            story.append(Paragraph(esc(content), st_body))
        elif tag == "sec":
            story.append(Paragraph(esc(content), st_section))
        elif tag == "bul":
            for item in content:
                story.append(Paragraph(esc(item), st_bul, bulletText="\u2022"))
            story.append(Spacer(1, 3))
        elif tag in CALLOUTS:
            story.append(Spacer(1, 1.5 * mm))
            story.append(callout(tag, content))
            story.append(Spacer(1, 1.5 * mm))


def _render_speech_md(speech, out):
    """Ajoute les blocs de discours d'une diapositive à la liste de lignes Markdown."""
    for tag, content in speech:
        if tag == "p":
            out.append(content)
            out.append("")
        elif tag == "sec":
            out.append("**" + content + "**")
            out.append("")
        elif tag == "bul":
            for item in content:
                out.append("- " + item)
            out.append("")
        elif tag in CALLOUTS:
            _, _, _, md_label = CALLOUTS[tag]
            out.append("> **%s —** %s" % (md_label, content))
            out.append("")


# --------------------------------------------------------------------------
# Constantes de navigation (sections)
# --------------------------------------------------------------------------
SCHEDULE = [
    ("Introduction",                           "h 0",  "h 1"),
    ("Module 1 — Fondamentaux de la sécurité", "h 1",  "h 5"),
    ("Module 2 — Gouvernance & cadre normatif","h 5",  "h 9"),
    ("Module 3 — ISO/IEC 27001:2022 — le SMSI","h 9",  "h 13"),
    ("Module 4 — ISO/IEC 27002:2022 — mesures","h 13", "h 17"),
    ("Module 5 — Gestion des risques",         "h 17", "h 21"),
    ("Module 6 — NIST CSF 2.0 & référentiels", "h 21", "h 25"),
    ("Module 7 — Politiques & mesures",        "h 25", "h 29"),
    ("Module 8 — Audit, conformité & droit",   "h 29", "h 33"),
    ("Module 9 — SecOps, DevSecOps & Cloud",   "h 33", "h 37"),
    ("Module 10 — Étude de cas & examen",      "h 37", "h 40"),
]

CALLOUT_DESCRIPTIONS = {
    "trans": "annonce le passage d'une notion à la suivante.",
    "tip":   "conseil d'animation ou de rythme.",
    "inter": "moment d'échange ou d'activité avec les étudiants.",
    "key":   "message essentiel à faire retenir.",
    "obj":   "rappel de l'objectif d'apprentissage associé.",
    "def":   "définition à poser clairement.",
    "ex":    "exemple concret pour ancrer la notion.",
    "warn":  "piège fréquent ou point de vigilance.",
}


# ==========================================================================
#  RENDU PDF
# ==========================================================================
def build_pdf(path):
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=18 * mm, bottomMargin=18 * mm,
        title="Discours enseignant — Normes et méthodes de sécurité (40 h)",
        author="Cours de licence 3")
    story = []

    # --- Page de garde ---
    story.append(Spacer(1, 35 * mm))
    story.append(Paragraph("Normes et méthodes de sécurité", st_title))
    story.append(Paragraph("Cours de licence 3 — 40 heures", st_sub))
    story.append(Spacer(1, 5 * mm))
    story.append(HRFlowable(width="60%", thickness=1.2, color=TEAL,
                            spaceBefore=2, spaceAfter=10, hAlign="CENTER"))
    story.append(Paragraph("DISCOURS COMPLET DE L'ENSEIGNANT", ParagraphStyle(
        "kick", fontName="Vera-Bold", fontSize=11, textColor=TEAL,
        alignment=TA_CENTER, spaceAfter=10)))
    story.append(Paragraph(
        "10 modules de 4 h  ·  Cours + travaux dirigés  ·  Étude de cas fil rouge",
        st_meta))
    story.append(Paragraph(
        "Support aligné diapositive par diapositive sur normes_methodes_securite_40h.pptx",
        st_meta))
    story.append(PageBreak())

    # --- Mode d'emploi ---
    story.append(module_bar("COMMENT UTILISER CE DOCUMENT"))
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(
        "Ce document contient l'intégralité de ce que l'enseignant peut dire, diapositive par "
        "diapositive. Le texte courant correspond au discours à prononcer (reformulable avec "
        "ses propres mots). Les encadrés de couleur sont des repères pour l'enseignant ; ils "
        "ne se lisent pas à voix haute.", st_body))
    story.append(Spacer(1, 2 * mm))
    for kind in ("trans", "tip", "inter", "key", "obj", "def", "ex", "warn"):
        story.append(callout(kind, CALLOUT_DESCRIPTIONS[kind]))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Découpage horaire indicatif (40 heures)", st_lead))
    for label, start, end in SCHEDULE:
        dots = "." * max(2, 55 - len(label))
        story.append(Paragraph(
            "%s %s %s → %s" % (label, dots, start, end),
            ParagraphStyle("tl", fontName="Vera", fontSize=10, leading=16,
                           textColor=DARK, leftIndent=6)))
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "Les durées sont indicatives ; adapter selon le rythme du groupe et les exercices choisis.",
        ParagraphStyle("note", fontName="Vera-Italic", fontSize=9.5, leading=14,
                       textColor=GREY)))

    # --- Corps du discours ---
    current_section = None

    for i, d in enumerate(cours_contenu.SLIDES):
        slide_num  = i + 1
        kind       = d["kind"]
        title      = d.get("title", "")
        module_num = d.get("module", 0)
        speech     = d.get("speech") or []

        # ---- Rupture de section ----
        if kind == "title":
            story.append(PageBreak())
            story.append(module_bar("INTRODUCTION"))
            story.append(Spacer(1, 5 * mm))
            current_section = "intro"

        elif kind == "module":
            story.append(PageBreak())
            mod_id  = d.get("number", str(module_num))
            mod_sub = d.get("subtitle", "")
            bar_text = "MODULE %s — %s" % (mod_id, title.upper())
            if mod_sub:
                bar_text += "  ·  " + mod_sub
            story.append(module_bar(bar_text))
            story.append(Spacer(1, 5 * mm))
            current_section = module_num

        elif kind == "closing" and current_section != "closing":
            story.append(PageBreak())
            story.append(module_bar("CLÔTURE DU COURS"))
            story.append(Spacer(1, 5 * mm))
            current_section = "closing"

        # ---- En-tête de diapositive ----
        story.append(Spacer(1, 4 * mm))
        story.append(slide_head(slide_num, title))
        story.append(Spacer(1, 2.5 * mm))

        # ---- Blocs de discours ----
        _render_speech_pdf(speech, story)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)


# ==========================================================================
#  RENDU MARKDOWN
# ==========================================================================
def build_md(path):
    out = []
    out.append("# Normes et méthodes de sécurité — Cours de licence 3 (40 h)")
    out.append("### Discours complet de l'enseignant")
    out.append("*10 modules de 4 h · Cours + travaux dirigés · Étude de cas fil rouge*")
    out.append("*Support aligné diapositive par diapositive sur "
               "`normes_methodes_securite_40h.pptx`.*")
    out.append("")
    out.append("## Comment utiliser ce document")
    out.append("Le texte courant correspond au **discours à prononcer**. "
               "Les encadrés sont des repères pour l'enseignant (ils ne se lisent pas à voix haute) :")
    out.append("")
    for kind in ("trans", "tip", "inter", "key", "obj", "def", "ex", "warn"):
        _, _, _, md_label = CALLOUTS[kind]
        out.append("- **%s** — %s" % (md_label, CALLOUT_DESCRIPTIONS[kind]))
    out.append("")
    out.append("### Découpage horaire indicatif (40 heures)")
    out.append("| Module | Horaire |")
    out.append("|---|---|")
    for label, start, end in SCHEDULE:
        out.append("| %s | %s → %s |" % (label, start, end))
    out.append("")

    current_section = None

    for i, d in enumerate(cours_contenu.SLIDES):
        slide_num  = i + 1
        kind       = d["kind"]
        title      = d.get("title", "")
        module_num = d.get("module", 0)
        speech     = d.get("speech") or []

        # ---- Rupture de section ----
        if kind == "title":
            out.append("")
            out.append("---")
            out.append("## INTRODUCTION")
            current_section = "intro"

        elif kind == "module":
            out.append("")
            out.append("---")
            mod_id  = d.get("number", str(module_num))
            mod_sub = d.get("subtitle", "")
            header  = "MODULE %s — %s" % (mod_id, title)
            if mod_sub:
                header += "  ·  " + mod_sub
            out.append("## " + header)
            current_section = module_num

        elif kind == "closing" and current_section != "closing":
            out.append("")
            out.append("---")
            out.append("## CLÔTURE DU COURS")
            current_section = "closing"

        # ---- En-tête de diapositive ----
        out.append("")
        out.append("### Diapositive %d — %s" % (slide_num, title))

        # ---- Blocs de discours ----
        _render_speech_md(speech, out)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


# ==========================================================================
def count_speech_words():
    n = 0
    for d in cours_contenu.SLIDES:
        for tag, content in (d.get("speech") or []):
            if tag in ("p", "sec") or tag in CALLOUTS:
                if isinstance(content, str):
                    n += len(content.split())
            elif tag == "bul" and isinstance(content, list):
                n += sum(len(x.split()) for x in content)
    return n


if __name__ == "__main__":
    build_pdf("discours_normes_securite_40h.pdf")
    build_md("discours_normes_securite_40h.md")
    n_slides = len(cours_contenu.SLIDES)
    print("OK — PDF + Markdown generés.")
    print("   Diapositives couvertes : %d" % n_slides)
    print("   Mots (discours)        : ~%d" % count_speech_words())
