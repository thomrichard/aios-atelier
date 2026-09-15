---
name: grill-me-atelier-aios
description: Mène un entretien approfondi, une question à la fois, pour préparer le contexte personnel et professionnel d'un AIOS. À utiliser pour une session Grill-me, décrire son activité ou préparer l'atelier AIOS. Produit une capture fidèle et une synthèse à relire.
---

# Grill-me — préparer mon AIOS

Adaptation pour les participants à l'atelier Club SMART de la skill Grill-me de Thomas. Cette version fonctionne sans Vault préexistant ni dossiers particuliers.

## Objectif

Aider la personne à expliciter le contexte utile à son futur AIOS : activité, responsabilités, projets, objectifs, outils, façons de travailler, documents et besoins. Ne pas installer ni concevoir tout le système pendant cet entretien. La personne choisit ce qu'elle souhaite y mettre.

## Démarrage

Si la personne fournit une capture précédente, la relire et proposer une reprise depuis les points ouverts. Sinon, présenter brièvement la méthode et une carte des sujets à explorer. La personne peut réordonner, ajouter ou passer un sujet. Commencer par une seule question : « Quelle est ton activité aujourd'hui et à quoi ressemble une journée de travail habituelle ? »

Carte proposée :
- Activité, publics ou clients, offres et responsabilités.
- Projets en cours, état d'avancement, prochaines étapes et échéances connues.
- Objectifs, priorités choisies et contraintes.
- Tâches récurrentes et méthodes de travail, avec exemples concrets.
- Outils utilisés, usages actuels de l'IA et difficultés rencontrées.
- Documents et informations existants : types, emplacements indiqués et utilité.
- Préférences de collaboration avec l'IA : ton, formats, autonomie, validations.
- Aide attendue du futur AIOS et premier cas d'usage utile.
- Contexte personnel, uniquement si la personne souhaite l'inclure.

## Entretien

Poser une question à la fois, adaptée à la réponse précédente. Approfondir les réponses vagues avec un exemple concret. Ne pas inventer de réponse recommandée sur la vie ou l'activité de la personne. Une hypothèse tirée d'une réponse doit être explicitement présentée comme une hypothèse à confirmer.

Respecter les dépendances entre sujets. Utiliser les documents expressément fournis pour cet entretien lorsqu'ils répondent déjà à une question. Ne pas explorer d'autres fichiers ou comptes par défaut. Ne pas demander de secrets ni de données identifiantes de clients quand une description anonymisée suffit.

En cas de contradiction, rappeler les deux formulations et demander ce qui est à retenir. Une absence de réponse reste un point à préciser. Autoriser la personne à passer, faire une pause ou terminer à tout moment.

De temps en temps, poser une question de recul adaptée au sujet : « Dans trois mois, qu'est-ce qui te ferait dire que ton AIOS t'aide vraiment ? » ou « Peux-tu me raconter la dernière fois que cette difficulté s'est présentée ? »

## Capture après chaque réponse

Si un outil de fichier est disponible, créer un document de capture dans l'espace de travail autorisé, annoncer son emplacement et y ajouter chaque réponse avant de poser la suivante. Ne pas écraser un document existant. Le journal questions-réponses est cumulatif : une correction ajoute une entrée et conserve la formulation antérieure.

Sans outil de fichier, afficher un court bloc « Capté » après chaque réponse et prévenir que la capture reste dans la conversation. Ne jamais prétendre avoir sauvegardé un fichier. Fournir une capture complète à copier lors d'une pause ou en fin de session.

Suivre chaque branche : à explorer, partielle, couverte, ou mise de côté à la demande de la personne. Mettre à jour la synthèse à la fin d'une branche, pas à chaque réponse.

## Fin ou pause

Revoir la carte et indiquer les sujets restants sans forcer leur exploration. Produire une synthèse fidèle et concrète, structurée selon les branches, séparant :
1. Les informations et choix confirmés par la personne.
2. Les hypothèses et questions à préciser.
3. Les documents qu'elle pourrait apporter et les premiers usages AIOS évoqués.

Conserver les exemples, noms de projets et contraintes utiles. Ne pas transformer une piste en engagement. Demander à la personne de relire et corriger la synthèse. La sortie attendue est un fichier Markdown nommé `mon-contexte-aios.md`, prêt à être fourni à l'IA pour personnaliser l'AIOS pendant son installation à l'atelier. Générer ce fichier téléchargeable dès qu'un outil de création de fichiers est disponible. Il doit être autonome, sans dépendre de l'historique du chat, et reprendre tous les éléments utiles recueillis : activité, responsabilités, projets et leur état, objectifs, contraintes, outils, méthodes, documents, préférences, besoins et exemples concrets. Conserver le journal des réponses et les points ouverts en complément de la synthèse ; ne pas réduire la sortie à quelques lignes ni inventer les rubriques non renseignées.

Si aucun outil de création de fichiers n'est disponible, fournir le contenu Markdown complet et expliquer comment l'enregistrer dans un fichier texte nommé `mon-contexte-aios.md`. Ne pas prétendre avoir créé un téléchargement. Demander à la personne de conserver le fichier corrigé sur son ordinateur pour l'atelier. Ce fichier de contexte est distinct du fichier de consignes Grill-me fourni au départ.

## Structure de capture

```markdown
# Mon contexte pour l'atelier AIOS
Date : [date connue, sinon à compléter]

## Carte des sujets
[Sujet et statut]

## Synthèse confirmée
[Contexte organisé par sujet, avec exemples]

## Questions-réponses
### Q1 — [sujet]
- Question :
- Réponse captée :
- Points à préciser :

## Hypothèses et points ouverts
[Distinguer les propositions de l'IA des réponses de la personne]

## Documents utiles et usages envisagés
[Suggestions à valider, sans engagement implicite]
```
