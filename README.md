# La cybersécurité : protéger ses données à l'ère du numérique
Support complet d'un **atelier de sensibilisation de 2 heures** destiné à un **public non spécialiste** (aucun prérequis technique).
Ce dépôt contient une présentation PowerPoint et le discours complet de l'orateur, ainsi que les scripts Python qui les génèrent.
## Livrables
- **`cybersecurite_presentation.pptx`** — la présentation (57 diapositives, format 16:9), organisée en 6 modules avec diapos de titre, statistiques, cartes, comparaisons, check-lists et quiz.
- **`discours_cybersecurite.pdf`** — le discours complet de l'orateur, minuté pour tenir 2 h, aligné diapositive par diapositive. Prêt à imprimer.
- **`discours_cybersecurite.md`** — le même discours en Markdown (lisible partout, facile à modifier).
Les scripts de génération sont fournis pour que vous puissiez tout adapter :
- **`generate_pptx.py`** — construit le `.pptx` (dépend de `python-pptx`).
- **`generate_speech.py`** — construit le discours `.pdf` et `.md` (dépend de `reportlab`).
## Plan de l'atelier (2 h)
1. **Accueil et introduction** — objectifs, programme, sondage.
2. **Partie 1 — Comprendre le monde numérique** — données, valeur, piliers, attaquants.
3. **Partie 2 — Les menaces courantes** — malwares, rançongiciels, hameçonnage, arnaques, mots de passe, fuites, Wi-Fi public, quiz.
4. **Pause** (~10 min).
5. **Partie 3 — Se protéger au quotidien** — mots de passe, gestionnaire, double authentification, mises à jour, sauvegardes, navigation, messagerie, réseaux sociaux.
6. **Partie 4 — Cas concrets** — smartphone, objets connectés, banque, enfants, télétravail.
7. **Partie 5 — Réagir en cas de problème** — reconnaître, agir, à qui s'adresser, RGPD.
8. **Conclusion et questions** — 10 bonnes habitudes, ressources, questions/réponses.
Le discours inclut aussi une **annexe « Questions fréquentes »** pour préparer le temps d'échange.
## Régénérer les fichiers
Les documents sont déjà générés ; ces étapes ne sont utiles que si vous modifiez le contenu.
```bash
# 1. Créer un environnement virtuel et installer les dépendances
python3 -m venv .venv
.venv/bin/pip install python-pptx reportlab

# 2. Générer la présentation
.venv/bin/python generate_pptx.py

# 3. Générer le discours (PDF + Markdown)
.venv/bin/python generate_speech.py
```
## Comment adapter le contenu
- Le **texte des diapositives** se trouve dans la section « CONSTRUCTION DE LA PRÉSENTATION » de `generate_pptx.py`.
- Le **texte du discours** se trouve dans la liste `BLOCKS` de `generate_speech.py`. Chaque bloc est typé (`part`, `slide`, `p`, `trans`, `tip`, `inter`, `key`, `bul`, `sec`) et alimente à la fois le PDF et le Markdown.
- Les **couleurs et polices** sont définies en haut de chaque script.
## Note sur les chiffres cités
Les statistiques (« une attaque toutes les 39 secondes », « ~90 % des attaques commencent par un e-mail ») sont des **ordres de grandeur** couramment cités, présentés comme tels. Elles servent à illustrer, pas à fournir une mesure exacte. Les ressources officielles citées (cybermalveillance.gouv.fr, 17Cyber, CNIL, ANSSI, Pharos) sont des dispositifs français réels.
