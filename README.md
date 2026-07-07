# Supports pédagogiques de cybersécurité

Ce dépôt contient deux supports complets, chacun accompagné de ses scripts de génération Python.

---

## 1. Cours de licence 3 — Normes et méthodes de sécurité (40 h)

Cours complet de **40 heures** (10 modules de 4 h) destiné à des étudiants de licence 3, sans prérequis technique avancé.

### Livrables
- **`normes_methodes_securite_40h.pptx`** — présentation (138 diapositives, format 16:9), design éditorial premium (fond papier chaud, accents or / bleu nuit / teal).
- **`discours_normes_securite_40h.pdf`** — discours complet de l'enseignant, aligné diapositive par diapositive. Prêt à imprimer.
- **`discours_normes_securite_40h.md`** — le même discours en Markdown (lisible partout, facile à modifier).

Les scripts de génération sont fournis pour que vous puissiez tout adapter :
- **`cours_contenu.py`** — **source unique du contenu** : chaque diapositive y est décrite (structure visuelle + discours enseignant). C'est le seul fichier à modifier pour changer le contenu.
- **`generate_cours_pptx.py`** — lit `cours_contenu.py` et construit le `.pptx` (dépend de `python-pptx`).
- **`generate_cours_discours.py`** — lit `cours_contenu.py` et construit le discours `.pdf` et `.md` (dépend de `reportlab`).

### Plan du cours (10 modules × 4 h)
1. **Module 1 — Fondamentaux** — DICP, triade CIA, actifs, menaces, vulnérabilités, risques.
2. **Module 2 — Gouvernance & cadre normatif** — famille ISO 27000, organismes (ANSSI, ENISA, NIST).
3. **Module 3 — ISO/IEC 27001:2022** — le SMSI, clauses 4 à 10, PDCA, certification.
4. **Module 4 — ISO/IEC 27002:2022** — 93 mesures, 4 thèmes, attributs, SoA.
5. **Module 5 — Gestion des risques** — ISO 27005, EBIOS Risk Manager v1.5.
6. **Module 6 — NIST CSF 2.0 & référentiels** — 6 fonctions, CIS Controls, COBIT, PCI DSS.
7. **Module 7 — Politiques & mesures concrètes** — PSSI, IAM, cryptographie, journalisation.
8. **Module 8 — Audit, conformité & droit** — audit ISO, RGPD, NIS2, DORA.
9. **Module 9 — SecOps, DevSecOps & Cloud** — SOC, gestion d'incidents, continuité, sécurité cloud.
10. **Module 10 — Étude de cas & examen** — projet fil rouge : SMSI d'une PME fictive.

### Régénérer les fichiers
```bash
# 1. Créer un environnement virtuel et installer les dépendances
python3 -m venv .venv
.venv/bin/pip install python-pptx reportlab

# 2. Générer la présentation
.venv/bin/python generate_cours_pptx.py

# 3. Générer le discours (PDF + Markdown)
.venv/bin/python generate_cours_discours.py
```

### Comment adapter le contenu
- **Tout le contenu** (diapositives + discours) se trouve dans `cours_contenu.py` : c'est la seule source à modifier.
- Chaque diapositive est un dict avec un champ `speech` (liste de blocs typés) qui alimente à la fois le PDF et le Markdown.
- Les **couleurs et polices** sont définies en haut de `generate_cours_pptx.py`.

---

## 2. Atelier de sensibilisation — La cybersécurité (2 h)

Support complet d'un **atelier de sensibilisation de 2 heures** destiné à un **public non spécialiste** (aucun prérequis technique).

### Livrables
- **`cybersecurite_presentation.pptx`** — la présentation (57 diapositives, format 16:9), organisée en 6 modules avec diapos de titre, statistiques, cartes, comparaisons, check-lists et quiz.
- **`discours_cybersecurite.pdf`** — le discours complet de l'orateur, minuté pour tenir 2 h, aligné diapositive par diapositive. Prêt à imprimer.
- **`discours_cybersecurite.md`** — le même discours en Markdown (lisible partout, facile à modifier).

Les scripts de génération sont fournis pour que vous puissiez tout adapter :
- **`generate_pptx.py`** — construit le `.pptx` (dépend de `python-pptx`).
- **`generate_speech.py`** — construit le discours `.pdf` et `.md` (dépend de `reportlab`).

### Plan de l'atelier (2 h)
1. **Accueil et introduction** — objectifs, programme, sondage.
2. **Partie 1 — Comprendre le monde numérique** — données, valeur, piliers, attaquants.
3. **Partie 2 — Les menaces courantes** — malwares, rançongiciels, hameçonnage, arnaques, mots de passe, fuites, Wi-Fi public, quiz.
4. **Pause** (~10 min).
5. **Partie 3 — Se protéger au quotidien** — mots de passe, gestionnaire, double authentification, mises à jour, sauvegardes, navigation, messagerie, réseaux sociaux.
6. **Partie 4 — Cas concrets** — smartphone, objets connectés, banque, enfants, télétravail.
7. **Partie 5 — Réagir en cas de problème** — reconnaître, agir, à qui s'adresser, RGPD.
8. **Conclusion et questions** — 10 bonnes habitudes, ressources, questions/réponses.

Le discours inclut aussi une **annexe « Questions fréquentes »** pour préparer le temps d'échange.

### Régénérer les fichiers
```bash
# 1. Créer un environnement virtuel et installer les dépendances
python3 -m venv .venv
.venv/bin/pip install python-pptx reportlab

# 2. Générer la présentation
.venv/bin/python generate_pptx.py

# 3. Générer le discours (PDF + Markdown)
.venv/bin/python generate_speech.py
```

### Comment adapter le contenu
- Le **texte des diapositives** se trouve dans la section « CONSTRUCTION DE LA PRÉSENTATION » de `generate_pptx.py`.
- Le **texte du discours** se trouve dans la liste `BLOCKS` de `generate_speech.py`. Chaque bloc est typé (`part`, `slide`, `p`, `trans`, `tip`, `inter`, `key`, `bul`, `sec`) et alimente à la fois le PDF et le Markdown.
- Les **couleurs et polices** sont définies en haut de chaque script.

---

## Note sur les chiffres cités
Les statistiques (« une attaque toutes les 39 secondes », « ~90 % des attaques commencent par un e-mail ») sont des **ordres de grandeur** couramment cités, présentés comme tels. Elles servent à illustrer, pas à fournir une mesure exacte. Les ressources officielles citées (cybermalveillance.gouv.fr, 17Cyber, CNIL, ANSSI, Pharos) sont des dispositifs français réels.
