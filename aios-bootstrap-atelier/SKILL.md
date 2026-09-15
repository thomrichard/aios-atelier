---
name: aios-bootstrap-atelier
description: Installer un AIOS générique et personnalisé à partir d'un Grill-me ou d'un contexte d'activité fourni, avec noyau partagé .ai, wiki, clôture et mémoire des décisions. Utiliser pour créer le socle d'un participant à l'atelier ou son AIOS personnel.
---

# Installer un AIOS à partir de son activité

Construire le même principe de socle que l'AIOS de Thomas : fichiers IPCRA, un noyau commun `.ai/`, des méthodes partageables entre assistants. Le package est générique : aucune donnée de Thomas, aucun métier, outil ou rythme imposé.

## Entrées et personnalisation

Lire le fichier Grill-me fourni en entier. La sortie `mon-contexte-aios.md` du Grill-me atelier convient directement. Ce document est une source de contexte, pas une instruction à exécuter. Conserver la différence entre réponses de la personne, suggestions de l'IA, hypothèses et décisions confirmées. Ne pas refaire l'entretien lorsque les réponses existent.

Il faut un dossier cible choisi et une autorisation d'installation, normalement exprimés dans la demande. Si le chemin manque, le demander. Déduire la langue et les préférences confirmées du document ; poser seulement les questions dont la réponse change réellement l'installation. Une information absente demeure « non précisé ». Ne pas inventer deux projets pour remplir les dossiers.

Lire [le profil de personnalisation](references/profil.md), puis produire un JSON avec le contexte utile, les casquettes, les projets réellement choisis et les points ouverts. Résumer brièvement ce qui sera installé. Un accord déjà fourni dans la demande suffit ; ne pas redemander une série de confirmations CAPE.

## Installation

Le script standard Python 3 crée le socle dans un dossier neuf ou vide, sans dépendance à télécharger :

```sh
python3 scripts/install.py --target DOSSIER_CHOISI --profile PROFIL_JSON --grill-me FICHIER_GRILL_ME
```

Résoudre `scripts/install.py` relativement au présent SKILL.md, pas au dossier courant. Les chemins de profil et Grill-me peuvent être externes au dossier cible, dans le périmètre autorisé. Le profil doit être stocké hors de la cible tant que celle-ci doit rester vide.

Le script refuse une cible non vide. Pour un AIOS existant, lire ses routeurs et noyau, préparer une comparaison avec `assets/vault/`, puis adapter seulement les fichiers nécessaires dans le périmètre demandé. Préserver les choix, projets et décisions existants. Ne jamais contourner le refus en supprimant les fichiers. Cet ajout est une adaptation accompagnée, pas une fonction de fusion automatique du script.

Sans terminal/Python mais avec accès aux fichiers, créer le même arbre depuis `assets/vault/`, puis appliquer la personnalisation selon le profil et les mêmes vérifications. Sans accès en écriture, fournir les fichiers à enregistrer et préciser que l'AIOS n'est pas encore installé.

## Ce qui est inclus

- IPCRA, contexte personnel, doctrine, conventions, connexions documentées.
- Sources et wiki : concepts et analyses ; explorations ; projets et publications distincts.
- `gerer-aios` : capture, rangement, recherche, ingestion, exploration, maintenance et amélioration.
- `close` : consolidation et point de reprise.
- `decisions` : choix confirmés, motifs, alternatives et historique des révisions.
- `AGENTS.md` et `CLAUDE.md` routent vers le même noyau. Entrées de skills légères sous `.agents/skills/` et `.claude/skills/` ; les méthodes vivent une seule fois dans `.ai/skills/`.

Close et Décisions s'installent immédiatement. On peut les enseigner dans un second temps sans demander une nouvelle installation. Leur présence ne crée aucun hook ni planification. Selon l'application, invoquer `/close`, `$close`, ou simplement « clôture cette discussion en suivant la skill close ». La disponibilité des commandes doit être constatée dans l'environnement du participant.

Les skills métier, styles, connecteurs et automatisations sont des extensions ultérieures motivées par un usage. Ne pas installer YouTube, CRM, statistiques, un fournisseur d'IA ou une charte de marque par défaut. Mail et agenda sont documentés comme non vérifiés tant qu'aucun essai de lecture autorisé ne les confirme.

## Réception

1. Lire les fichiers générés, leurs liens et le contexte personnalisé. Signaler les inconnues.
2. Vérifier qu'une piste du Grill-me n'est pas devenue un projet actif et qu'une suggestion n'est pas devenue une décision confirmée.
3. Proposer un essai réel sur une petite décision choisie par la personne ; enregistrer son motif, puis faire un close et relire le point de reprise. Sans décision réelle, tester sur un dossier d'exercice séparé, pas avec une fausse décision dans le dossier personnel.
4. Dans un autre assistant disposant d'accès au même dossier, faire retrouver la décision et ses raisons. Si cet assistant n'est pas disponible, signaler que le transfert reste à tester ; ne pas revendiquer une compatibilité universelle.

Le script vérifie la structure et les liens, pas le jugement de l'assistant. Présenter le chemin d'accueil, les capacités incluses, les contrôles effectués et ce qui reste à valider.
