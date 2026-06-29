# Gameplay Loop

Version : 0.1
Statut : En cours de conception

---

# 1. Objectif

Définir la boucle principale de gameplay d'AnkArmy.

Chaque ouverture d'Anki doit être perçue comme une prise de service au sein d'une organisation militaire.

La boucle doit être simple, rapide, motivante et ne jamais ralentir les révisions.

---

# 2. Boucle principale

```text
Ouverture d'Anki
        │
        ▼
Connexion au Commandement
        │
        ▼
Analyse de la situation
        │
        ▼
Génération de l'ordre de mission
        │
        ▼
Début de la mission (révision)
        │
        ▼
Suivi de la mission en temps réel
        │
        ▼
Mission terminée
        │
        ▼
Rapport militaire
        │
        ▼
Calcul des performances
        │
        ▼
XP • Discipline • Promotions
        │
        ▼
Déblocages éventuels
        │
        ▼
Fin de mission
```

---

# 3. Déroulement détaillé

## 3.1 Connexion

À l'ouverture d'Anki, le joueur est accueilli par le terminal militaire.

Exemple :

```
===================================================

AIR COMMAND TERMINAL

Connexion...

Bienvenue Aviateur.

Analyse des opérations...

===================================================
```

Cette étape doit durer moins d'une seconde.

---

## 3.2 Analyse

Le Commandement analyse automatiquement :

* la moyenne des performances récentes ;
* la discipline ;
* les cartes en attente ;
* les missions précédentes ;
* les séries de jours consécutifs.

Aucune intervention du joueur n'est nécessaire.

---

## 3.3 Ordre de mission

Le système génère automatiquement un ordre.

Exemple :

```
MISSION N°248

Objectif :

Réviser 35 cartes.

Précision minimale :

90 %

Difficulté :

Normale

Autorisation :

MISSION VALIDÉE
```

Le joueur peut :

* accepter immédiatement ;
* consulter les détails.

---

## 3.4 Exécution

Pendant la révision :

Le jeu reste discret.

Le joueur voit uniquement :

* progression ;
* état de la mission ;
* discipline actuelle.

Aucune fenêtre ne doit interrompre la révision.

---

## 3.5 Fin de mission

Lorsque la session est terminée :

Le Commandement prépare automatiquement le rapport.

---

## 3.6 Rapport

Exemple :

```
MISSION TERMINÉE

Cartes :

38

Réussite :

94 %

Temps :

12 min

Discipline :

Excellent

XP :

+348
```

Le rapport doit être lisible en moins de cinq secondes.

---

## 3.7 Évaluation

Le système vérifie automatiquement :

* promotion ;
* médaille ;
* amélioration de discipline ;
* avertissement éventuel.

---

## 3.8 Déblocages

Si le joueur progresse :

Le terminal annonce :

```
PROMOTION

Félicitations.

Vous êtes désormais :

Caporal.

Nouvelle mécanique débloquée :

Missions avancées.
```

---

# 4. Durée idéale

Connexion : < 1 seconde

Mission : variable

Rapport : < 5 secondes

L'ensemble de la couche "jeu" ne doit jamais ralentir les révisions.

---

# 5. Règles fondamentales

* Aucun hasard.
* Aucune récompense gratuite.
* Les missions sont générées automatiquement.
* Les sanctions sont automatiques et proportionnelles.
* Toutes les décisions reposent sur les performances réelles.
* Le joueur garde toujours le contrôle de ses révisions.

---

# 6. Conditions de réussite

La boucle est réussie si :

* elle est comprise en moins d'une minute ;
* elle devient une habitude quotidienne ;
* elle renforce la motivation sans détourner l'attention des cartes Anki.

---

# 7. Questions ouvertes

À définir ultérieurement :

* Peut-on enchaîner plusieurs missions dans une même journée ?
* Existe-t-il des opérations spéciales hebdomadaires ?
* Les missions peuvent-elles concerner plusieurs escadrons (decks) à la fois ?
* Quels critères déclenchent une promotion exceptionnelle ?
