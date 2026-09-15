# Traduire le Grill-me en profil

Le modèle lit et comprend le Grill-me ; le script ne fait pas d'analyse sémantique. Les textes sont des reformulations attribuées de faits confirmés. Garder les informations réservées dans le contexte personnel, pas dans les index ni les noms de fichiers.

Profil JSON minimal :

```json
{
  "name": "Camille",
  "language": "français",
  "context": "Contexte confirmé et objectif du système, avec provenance dans le Grill-me.",
  "preferences": "Préférences confirmées ; le reste est non précisé.",
  "open_questions": ["Points non confirmés, contradictions ou choix à préciser"],
  "roles": [
    {"slug": "accompagnement", "title": "Accompagnement", "description": "Responsabilité continue confirmée"}
  ],
  "projects": [
    {"slug": "livrer-guide", "title": "Livrer le guide", "status": "actif", "description": "Résultat choisi et état confirmé", "done_when": "Condition de fin confirmée, sinon non précisée"}
  ],
  "tools": [
    {"name": "Agenda", "usage": "Usage décrit dans le Grill-me ; accès non vérifié"}
  ]
}
```

Champs requis : `name`, `context`. Les listes peuvent être vides. Statuts de projets : `envisage`, `actif`, `en-attente`, `termine`, `abandonne`. Slugs : minuscules ASCII, chiffres et tirets. Le choix du statut doit avoir une provenance ; une simple idée sans engagement reste dans `open_questions`, pas dans `projects`. Aucune échéance n'est obligatoire.

La copie du Grill-me fournie devient `.ai/inputs/grill-me.md`, conservée comme source inerte et reliée au contexte. En cas de source comprenant des secrets, demander une version expurgée ou retirer les valeurs avec l'accord approprié avant distribution. Le package distribué ne contient jamais le profil réel d'un participant ni son Grill-me.

Les décisions ne sont pas inférées automatiquement par le script : traiter ensuite les décisions explicitement confirmées avec la skill `decisions`, en citant la source et en préservant les points ouverts.
