# Missions

Version : 0.1
Statut : En cours de conception

---

# 1. Objectif

Les missions représentent les sessions de révision Anki transformées en opérations militaires.

Chaque mission donne un objectif clair, mesurable et adapté au niveau du joueur.

Le système doit transformer une simple session de révision en un moment structuré et motivant.

---

# 2. Principes fondamentaux

Les missions reposent sur les règles suivantes :

* elles sont générées automatiquement ;
* elles s’adaptent à la discipline et aux performances ;
* elles ne doivent jamais bloquer la révision ;
* elles sont courtes à comprendre ;
* elles reflètent la réalité des cartes à réviser.

---

# 3. Types de missions

## Mission standard

Mission de base quotidienne.

Objectif :

* réviser un nombre défini de cartes ;
* maintenir un niveau de précision correct.

---

## Mission de discipline

Mission orientée régularité.

Objectifs possibles :

* maintenir une série de jours consécutifs ;
* réduire les absences ;
* stabiliser les performances.

---

## Mission de précision

Mission orientée performance.

Objectifs possibles :

* atteindre un taux de réussite minimum ;
* réduire les erreurs ;
* améliorer la qualité des réponses.

---

## Mission avancée

Débloquée à partir d’un certain grade.

Objectifs :

* combiner volume + précision ;
* intégrer plusieurs escadrons ;
* imposer des contraintes de temps.

---

## Mission spéciale

Mission rare générée par le Commandement.

Objectifs variables :

* événement exceptionnel ;
* rattrapage de retard ;
* opération stratégique.

---

# 4. Génération des missions

Les missions sont générées automatiquement à partir de plusieurs paramètres :

* discipline actuelle ;
* historique des 10 derniers jours ;
* charge de cartes Anki ;
* taux de réussite ;
* régularité des sessions.

---

# 5. Structure d’une mission

Chaque mission contient :

## 1. Identifiant

Numéro de mission unique.

---

## 2. Objectif principal

Exemple :

* réviser 35 cartes
* atteindre 90% de réussite

---

## 3. Contraintes

Exemples :

* temps recommandé ;
* interdiction de pause excessive ;
* limite d’erreurs tolérées.

---

## 4. Difficulté

* facile
* normale
* élevée
* critique

---

## 5. Récompenses

* XP de base ;
* bonus de discipline ;
* déblocage potentiel.

---

# 6. Déroulement d’une mission

1. Le Commandement génère la mission
2. Le joueur accepte automatiquement ou manuellement
3. La révision Anki commence
4. Le système observe les performances
5. Un rapport est généré à la fin

---

# 7. Adaptation dynamique

Les missions évoluent selon le joueur :

## Si discipline élevée

* missions plus ambitieuses ;
* bonus XP augmentés ;
* accès à missions avancées.

---

## Si discipline faible

* missions simplifiées ;
* focus sur la régularité ;
* réduction des contraintes.

---

# 8. Choix tactiques

Certaines missions peuvent proposer des choix :

Exemple :

```
MISSION 142

Options :

A) Mode standard
B) Mode intensif (+XP, plus strict)
C) Mode récupération (moins de pression)
```

Ces choix n’influencent pas la mission elle-même, mais la manière dont elle est évaluée.

---

# 9. Anti-répétition

Le système doit éviter :

* les mêmes missions consécutives ;
* les patterns prévisibles ;
* les charges identiques répétées.

Les missions doivent sembler naturelles.

---

# 10. Limite importante

Les missions ne doivent jamais :

* interrompre une session Anki ;
* ralentir la révision ;
* forcer une interaction longue.

Le joueur doit pouvoir ignorer la couche “jeu” et continuer à apprendre.

---

# 11. Règle fondamentale

La mission est une couche de lecture au-dessus d’Anki, pas une barrière.

Le joueur révise d’abord.

Le système analyse ensuite.
