# AIOS atelier

Un AIOS générique à personnaliser depuis un entretien Grill-me : fichiers IPCRA, noyau partagé `.ai/`, clôture et mémoire des décisions. Aucun compte ni outil métier n'est installé.

## Pendant l'atelier

1. Télécharger le dossier `aios-bootstrap-atelier` ou le ZIP fourni.
2. Le rendre disponible à un assistant ayant accès en lecture et écriture aux fichiers. La méthode est dans `aios-bootstrap-atelier/SKILL.md` ; lire ce fichier directement fonctionne aussi sans découverte automatique.
3. Fournir son `mon-contexte-aios.md` et choisir un **dossier neuf ou vide**.
4. Demander : « Utilise la skill aios-bootstrap-atelier de ce dossier pour installer mon AIOS dans [chemin], à partir de mon fichier Grill-me. Ne me repose pas les questions déjà renseignées. »
5. Ouvrir `accueil.md`, vérifier le contexte et les projets, puis essayer une décision et un close.

Le modèle transforme le Grill-me en profil ; le script Python 3 installe les fichiers sans dépendance ni réseau. Close et Décisions sont inclus dès l'installation, même s'ils sont expliqués plus tard pendant l'atelier.

## Assistant et portabilité

`AGENTS.md` et `CLAUDE.md` renvoient au même noyau. Des entrées légères de skills sont créées sous `.agents/skills/` et `.claude/skills/`, sans liens symboliques. Les méthodes vivent une seule fois sous `.ai/skills/`.

L'assistant doit pouvoir lire et modifier les fichiers. Les noms de commande varient : `/close`, `$close`, ou « clôture cette discussion en suivant la skill close ». La découverte automatique et la reprise entre deux applications doivent être testées dans les environnements utilisés ; elles ne sont pas garanties par la seule présence des fichiers.

## Inclus et extensions

| Dès le départ | Selon l'usage, ensuite |
|---|---|
| Contexte, IPCRA, recherche et rangement | Skills de métier ou de production |
| Close et point de reprise | Connexions mail, agenda et autres services |
| Décisions avec motifs et révisions | Statistiques, publication et CRM |
| Explorations, maintenance, amélioration | Automatisations explicitement demandées |

Le package reproduit les principes du socle, pas les données, la charte, le globe ou les outils personnels de son auteur. Un ajout à un AIOS existant demande une comparaison accompagnée ; l'installateur refuse de remplacer un dossier non vide.

## Vérification locale

```sh
python3 -m unittest discover -s tests -v
```

Les tests vérifient une installation depuis un profil fictif, les liens, les entrées communes, le refus d'écrasement et de chemins de sortie dans les slugs. Ils ne simulent pas une validation humaine du Grill-me ni un second assistant.
