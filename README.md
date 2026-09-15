# AIOS atelier — v1.0.3

Un AIOS générique à personnaliser depuis un entretien Grill-me : fichiers IPCRA, noyau partagé `.ai/`, clôture et mémoire des décisions. Aucun compte ni outil métier n'est installé.

## Télécharger le kit

[Télécharger le ZIP v1.0.3](https://github.com/thomrichard/aios-atelier/releases/download/v1.0.3/aios-bootstrap-atelier-v1.0.3.zip) puis le décompresser. Il contient le questionnaire Grill-me, le dossier d'installation, ce guide et la présentation HTML.

## Avant l'atelier : préparer son contexte (environ 10 minutes)

1. Ouvrir [le questionnaire Grill-me](grill-me-atelier-aios.md) et télécharger le fichier avec le bouton de téléchargement du fichier brut de GitHub, ou le retrouver dans le ZIP.
2. Joindre `grill-me-atelier-aios.md` à une conversation avec son IA, ou copier son contenu dans la conversation.
3. Copier cette demande :

> Lis le fichier joint et suis ses consignes Grill-me pour m'aider à préparer mon AIOS. J'ai environ 10 minutes : pose-moi une question à la fois pour comprendre mon activité, mes projets, mes outils, ma manière de travailler et ce que j'aimerais confier à mon IA. Je peux répondre en dictant mes messages. Quand je te dis de terminer, génère un fichier Markdown téléchargeable nommé mon-contexte-aios.md. Reprends les éléments utiles avec suffisamment de détails et distingue les informations confirmées des points à préciser.

4. Relire et corriger la synthèse, puis conserver `mon-contexte-aios.md` sur son ordinateur pour l'atelier. Si l'IA ne peut pas créer de fichier téléchargeable, enregistrer le Markdown fourni dans un fichier texte portant ce nom.

Le questionnaire est public ; les réponses personnelles restent dans vos fichiers. Ne publiez pas votre `mon-contexte-aios.md` dans ce dépôt.

## Pendant l'atelier

1. Décompresser le ZIP et repérer le dossier `aios-bootstrap-atelier`.
2. Le rendre disponible à un assistant ayant accès en lecture et écriture aux fichiers. La méthode est dans `aios-bootstrap-atelier/SKILL.md` ; lire ce fichier directement fonctionne aussi sans découverte automatique.
3. Fournir son `mon-contexte-aios.md` et choisir un **dossier neuf ou vide**.
4. Demander : « Utilise la skill aios-bootstrap-atelier de ce dossier pour installer mon AIOS dans [chemin], à partir de mon fichier Grill-me. Ne me repose pas les questions déjà renseignées. »
5. Ouvrir `accueil.md`, vérifier le contexte et les projets, puis essayer une décision et un close.

Le modèle transforme le Grill-me en profil ; le script Python 3 installe les fichiers sans dépendance ni réseau. Close et Décisions sont inclus dès l'installation, même s'ils sont expliqués plus tard pendant l'atelier.

## Présentation de l'atelier

La [présentation HTML](supports/atelier-aios.html) est incluse dans le ZIP : ouvrir `supports/atelier-aios.html` dans un navigateur après décompression. GitHub affiche son code ; le téléchargement permet de voir les diapositives. Elle fonctionne hors ligne. Flèches droite/gauche : sujets ; bas/haut : détails ; N : notes ; O : sommaire ; F : plein écran.

Les connexions mail et calendrier seront accompagnées pendant l'atelier. Les capsules vidéo seront ajoutées séparément.

## Assistant et portabilité

`AGENTS.md` et `CLAUDE.md` renvoient au même noyau. Des entrées légères de skills sont créées sous `.agents/skills/` et `.claude/skills/`, sans liens symboliques. Les méthodes vivent une seule fois sous `.ai/skills/`.

L'assistant doit pouvoir lire et modifier les fichiers. Les noms de commande varient : `/close`, `$close`, ou « clôture cette discussion en suivant la skill close ». La découverte automatique et la reprise entre deux applications doivent être testées dans les environnements utilisés ; elles ne sont pas garanties par la seule présence des fichiers.

## Inclus et extensions

| Dès le départ | Selon l'usage, ensuite |
|---|---|
| Contexte, IPCRA, recherche et rangement | Skills de métier ou de production |
| Close et point de reprise | Connexions mail, agenda et autres services |
| Décisions avec motifs et révisions | Statistiques, publication et CRM |
| Explorations et amélioration | Automatisations explicitement demandées |

L’audit de cohérence est hors package ; il sera à retrouver dans les ressources du Club SMART. L’interface de workflows à nœuds est en préparation et n’est pas encore installée par cette version.

Le package reproduit les principes du socle, pas les données, la charte, le globe ou les outils personnels de son auteur. Un ajout à un AIOS existant demande une comparaison accompagnée ; l'installateur refuse de remplacer un dossier non vide.

## Vérification locale

```sh
python3 -m unittest discover -s tests -v
```

Les tests vérifient une installation depuis un profil fictif, les liens, les entrées communes, le refus d'écrasement et de chemins de sortie dans les slugs. Ils ne simulent pas une validation humaine du Grill-me ni un second assistant.
