---
name: decisions
description: Préparer un arbitrage, mémoriser une décision confirmée avec ses motifs, retrouver un choix ou réviser une décision de cet AIOS en préservant son historique.
---

# Décisions et arbitrages

Lire `../../context.md` et `../../decisions/index.md`, puis rechercher les décisions et objets concernés. Un index incomplet n'exclut pas une décision existante.

## Préparer un choix

Exposer le problème concret, les options réellement utiles, leurs conséquences et une recommandation motivée. Séparer faits, contraintes confirmées et hypothèses. La décision reste à la personne. Une option évoquée dans un Grill-me n'est pas un accord.

## Enregistrer un choix confirmé

Créer une fiche datée unique dans `.ai/decisions/`, ou enrichir la fiche existante s'il s'agit du même choix. Métadonnées : id, type decision, title, created, updated, status active.

La fiche contient : **choix**, **contexte et portée**, **motifs exprimés**, **alternatives écartées et raisons lorsqu'elles sont connues**, **conséquences**, **source de confirmation** et **conditions éventuelles de réexamen**. Si un motif manque, l'écrire ; ne pas le fabriquer. Identifier séparément une interprétation de l'IA.

Ajouter la décision à l'index et une trace courte au journal. Relier le projet, contexte ou méthode concernés. Ne modifier une règle du noyau que si le choix confirmé la concerne effectivement. L'enregistrement n'exécute pas automatiquement les conséquences externes du choix.

## Réviser et retrouver

Une révision conserve la décision antérieure avec status remplacee et un lien vers la nouvelle ; la nouvelle explique le changement et cite l'ancienne. Une exception bornée conserve la règle générale. Ne pas effacer une contradiction sans arbitrage.

Pour répondre « pourquoi avons-nous choisi cela ? », citer la fiche et distinguer raisons exprimées, inférences et informations absentes. Vérifier l'état le plus récent et son périmètre. Un accord explicite peut être enregistré immédiatement, sans répétition de confirmation.
